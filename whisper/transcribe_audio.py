#!/usr/bin/env python3
 
# --- LIBRARIES --- #
from argparse import ArgumentParser
import whisper
import glob
 
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
	# glob.glob -> list; glob.iglob -> iterator
	globbed_paths = sorted(glob.iglob(args.path[0]))

	# load model
	model = whisper.load_model("base")
	print("'base' model loaded")

	for g in globbed_paths:
		# read in audio
		audio_input = g
 		
		# transcribe audio
		#verbose=False
		result = model.transcribe(g, fp16=False)
		#print(result)   # to see structure of transcribed text
		# print transcribed text
		for segment in result["segments"]:
			print(g, round(segment["start"]), segment["text"], sep='\t')

 
if __name__ == "__main__":
	main()


