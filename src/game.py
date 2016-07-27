'''
This file contains methods for the mastermind word game.

..moduleauthor::Richard D
..moduleauthor::Russ M
..module::game
:synopsis:Game files
'''
import random

def parse_dict_file(fpath, w_length):
	'''
	This function will open a file and parse out all words of the
	given length and return a set.
	
	:param fpath:Dictionary to parse
	:type fpath:str
	:param w_length:The word length
	:type w_length:int
	'''
	
	w_list = []
	with open(fpath) as word_file:
		for line in word_file:
			word = line.strip()
			if len(word) == w_length:
				w_list.append(word)
	return w_list

def main():
	'''behavioral testing'''
	l = parse_dict_file('../data/enable1.txt', 7)
	w = random.sample(l, 7) 
	print(w)

if __name__ == '__main__':
	main()
