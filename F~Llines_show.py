import sys
##指定された行数の表示
input_file_name = sys.argv[1]
first_lines_number = int(sys.argv[2])
last_lines_number = int(sys.argv[3])

lines_number = 0
mails_list = []

with open(input_file_name,'r')as f:
    for mails in f.readlines():
        mails_list.append(mails)

if first_lines_number<=last_lines_number:
    print (mails_list[first_lines_number-1:last_lines_number])
elif last_lines_number<first_lines_number:
    print("エラー")
