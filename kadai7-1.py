import sys
import MeCab
##kadai6->p(w|s)bunnbo
##list->p(w|s)bunnsi
input_file_name = sys.argv[1]

mecab = MeCab.Tagger("-Owakati")
mails_firstwords_list = []

words_count = {}
mails_firstwords_count = {}
firstwords_count_number = 0
words_count_number = 0
label2words_count_number = {}
label2words = {}

##input_fileの読み込み、単語に分割
with open(input_file_name, 'r') as f:
	for mail in f:
		words = mecab.parse(mail)
		words = words.rstrip('\n')
		split_words=words.split()
		##labelの数のカウント
		mails_firstwords_count[split_words[0]] = mails_firstwords_count.get(split_words[0],0)+1
		firstwords_count_number+=1
		##labelごとの単語wの出現数
		for word in split_words:
			label2words[split_words[0]] = words_count
			##label2words[split_words[0]][word] = label2words[split_words[0]].get(word,0)+1
			label2words_count_number[split_words[0]] = label2words_count_number.get(split_words[0],0)+1 
	##print(f'P({word}|{split_words[0]}) = {label2words[split_words[0]][word]}/{label2words_count_number[split_words[0]]}')
##for key,value in label2words.items():
	##print(f'P({key}|')
for key,value in mails_firstwords_count.items():
	print(f'P({key}) = {value}/{firstwords_count_number}')
print(label2words_count_number)
##print(f'P({key}|{value} = {number}/{label2words_count_number{key}}

