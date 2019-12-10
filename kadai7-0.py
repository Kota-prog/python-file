import sys
import MeCab
from fractions import Fraction

mecab = MeCab.Tagger("-Owakati")

def reading_file(input_file_name):
	
	mails = []
	with open(input_file_name,'r')as f:
		for mail in f:
			mails.append(mail)
	return mails

def split_mail_into_words(mails):
	##\nを消す
	mails_words = []
	for mail in mails:
		label,words = mail.split(',')
		words = words.rstrip()
		words = mecab.parse(words).split(' ')
		mails_words.extend(words)		

	return mails_words

def count_words(mails_words):
	
	words_number = {}
	for word in mails_words:
		words_number[word] = words_number.get(word,0)+1
	
	return words_number

def count_total_words(words_number):
	
	total_words_number = 0
	for value in words_number.values():
		total_words_number+=value
	return total_words_number

def count_word2freq(words_number,total_words_number):
	
	w2f = {}
	for key,value in words_number.items():
		w2f[key] = Fraction(value,total_words_number)

	return w2f

def output_w2f(w2f)
	
	for key,value in w2f.items():
		print(f'{key} {value}')

def main():
	
	input_file_name = sys.argv[1]
	##変数名
	mails = reading_file(input_file_name)	
	mails_words = split_mail_into_words(mails)
	words_number = count_words(mails_words)
	total_words_number = count_total_words(words_number)
	w2f = count_word2freq(words_number,total_words_number)
	##ファイル出力
	output_w2f(w2f)

if __name__ == '__main__':
	main()
	
