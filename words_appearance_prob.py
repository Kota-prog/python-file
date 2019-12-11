import sys
import MeCab
from fractions import Fraction

path_output = 'output.txt' 
mecab = MeCab.Tagger("-Owakati")

def reading_file(input_file_name):
	
	mails = []
	with open(input_file_name,'r')as f:
		for mail in f:
			mails.append(mail)
	return mails

def split_mails_into_words(mails):
	##\nを消す
	mails_words = []
	for mail in mails:
		label,words = mail.split(',')
		words = words.rstrip()
		words = mecab.parse(words).split(' ')
		mails_words.extend(words)		

	return mails_words

def count_words(mails_words):
	
	w2f = {}
	for word in mails_words:
		w2f[word] = w2f.get(word,0)+1
	
	return w2f

def count_total_words(w2f):
	
	total_w2f = 0
	for value in w2f.values():
		total_w2f+=value
	return total_w2f

def count_word2freq(w2f,total_w2f):
	
	pw = {}
	for key,value in w2f.items():
		pw[key] = Fraction(value,total_w2f)

	return pw

def output_pw(pw):
	with open(path_output,mode = 'w') as f:
		for key,value in pw.items():
			print(f'{key} {value}',file = f)

def main():
	
	input_file_name = sys.argv[1]
	
	mails = reading_file(input_file_name)	
	mails_words = split_mails_into_words(mails)
	w2f = count_words(mails_words)
	total_w2f = count_total_words(w2f)
	pw = count_word2freq(w2f,total_w2f)
	##ファイル出力
	output_pw(pw)

if __name__ == '__main__':
	main()
	
