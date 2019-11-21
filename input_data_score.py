import sys
import MeCab
##kadai6->p(w|s)bunnbo
##list->p(w|s)bunnsi
input_file_name = sys.argv[1]

mails_firstwords_list = []

mails_firstwords_count = {}
with open(input_file_name, 'r') as f:
	input_file = f.read()
	for mails in f.readlines():
   		mails_words_list = list(mails)
    		mails_firstwords_list.append(mails_words_list[0])

firstwords_count_number = 0

for firstword in mails_firstwords_list:
	mails_firstwords_count[firstword] = mails_firstwords_count.get(firstword,0)+1
	firstwords_count_number+=1

for key,value in mails_firstwords_count.items():
	print(f'P({key}) = {value}/{firstwords_count_number}')

mecab=MeCab.Tagger("-Owakati")
words=mecab.parse(input_file)
split_words=words.split('\n')












