import sys

input_file_name = sys.argv[1]

mails_firstwords_list = []

mails_firstwords_count = {}
with open(input_file_name, 'r') as f:
    for mails in f.readlines():
        mails_words_list = list(mails)
        mails_firstwords_list.append(mails_words_list[0])

for firstword in mails_firstwords_list:
    mails_firstwords_count[firstword] = mails_firstwords_count.get(firstword,0)+1

print(mails_firstwords_count)
