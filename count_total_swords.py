import sys
import MeCab

input_file_name=sys.argv[1]

with open(input_file_name,'r')as f:
   input_file=f.read()

mecab=MeCab.Tagger("-Ochasen")
words=mecab.parse(input_file)
split_words=words.split('\n')

words_count=0
for word in split_words:
   words_count+=1

print(words_count)
