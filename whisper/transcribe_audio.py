#!/usr/bin/env python3
 
# --- LIBRARIES --- #
from argparse import ArgumentParser
import whisper
import glob
import sys
 
# --- VARIABLES --- #
 
# --- OBJECTS ----- #
 
# --- HELPER FUNCTIONS --- #
 
# --- MAIN --------------- #
def main():
	# create parser
	parser = ArgumentParser(description = 'transcribe an audio file using Whisper')
	# add arguments to parser
	parser.add_argument('path', nargs='+', help='Path of a file or a folder of files.')
	# collate/parse arguments, including glob
	args = parser.parse_args()

	# if args.path is not a string, then only one file gets processed
	for p in args.path:
		if not isinstance(p, str):
			print(p)
			sys.exit('ERROR: The argument p must be a string -> use quotes \
			around the filename or glob.\n\
			       Please fix this and try again.')

	if not isinstance(args.path, list):
		print(args.path)
		exit('ERROR: The argument args.path must be a list -> use quotes \
		around the filename or glob.\n\
		       Please fix this and try again.')

	# glob.glob -> list; glob.iglob -> iterator
	globbed_paths = sorted(glob.glob(args.path[0]))
	#print(globbed_paths)

	# load model
	model = whisper.load_model("base")
	print("'base' model loaded")

	for g in globbed_paths:
		# read in audio
		#print(f'{g=}')
 		
		# transcribe audio
		#verbose=False
		result = model.transcribe(g, fp16=False)
		#print(result)   # to see structure of transcribed text
		# print transcribed text
		for segment in result["segments"]:
			mins = segment["start"] / 60
			secs = round(segment["start"] % 60)
			#print(g, round(segment["start"]), segment["text"], sep='\t')
			# TODO: add in option to print filename
			print(mins, ":", secs, "\t", segment["text"], sep='')

 
if __name__ == "__main__":
	main()


