import sys
import MeCab

mecab = MeCab.Tagger("-Owakati")

def reading_file(mail):
	
	mail = mail.rstrip('\n')
	mail_words = mecab.parse(mail)
	label,words = mail_words.split(',')
			
	return label,words
	
def label_count(label,labels_number):
	
	labels_number[label] = labels_number.get(label,0)+1
	
	return labels_number
def main():

	input_file_name = sys.argv[1]
	labels_number = {}
	total_labels_number = 0
	#input_fileの読み込み
	with open(input_file_name, 'r') as f:
		for mail in f:
			label,words = reading_file(mail)
			labels_number = label_count(label,labels_number)
			total_labels_number+=1
			##labelごとの単語wの出現数			
			L2W = label,words
			##labelごとの単語wの総数
			
		##print(labels_number)
		##print(total_labels_number)
if __name__ == '__main__':
	main()

