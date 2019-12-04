import sys
import MeCab

mecab = MeCab.Tagger("-Owakati")

def reading_file(mail):
	label,words = mail.split(',')
	words = words.rstrip()
	words = mecab.parse(words).split(" ")
			
	return label,words

def w2f_count(words):
	w2f = {}
	for word in words:
		w2f[word] = w2f.get(word,0)+1
	return w2f

def l2f_write(l2f,total_l2f):
	with open('l2f_w.txt',mode = 'w')as f:
		for key,value in l2f.items():
			print(f'P({key}) = {value}/{total_l2f}',file = f)

def l2w2f_write(l2w2f,total_l2w2f):
	with open('l2w2f_w.txt',mode = 'w')as f:
		for label in l2w2f.keys():
			for word,freq in l2w2f[label].items():
				print(f'P({word}|{label}) = {freq}/{total_l2w2f[label]}',file = f)
	
	

def main():

	input_file_name = sys.argv[1]
	l2f = {}
	w2f = {}	
	total_l2f = 0
	l2w2f = {}
	total_l2w2f = {}
	
	#input_fileの読み込み
	with open(input_file_name, 'r') as f:
		for mail in f:
			label,words = reading_file(mail)
			l2f[label] = l2f.get(label,0)+1
			w2f = w2f_count(words)
			total_l2f+=1	
			l2w2f[label] = l2w2f.get(label,{})
			for word in words:
				l2w2f[label][word] = l2w2f[label].get(word,0)+1
				total_l2w2f[label] =total_l2w2f.get(label,0)+1
	##テキストファイルに結果の書き込み
	l2f_write(l2f,total_l2f)
	l2w2f_write(l2w2f,total_l2w2f)
	

if __name__ == '__main__':
	main()

