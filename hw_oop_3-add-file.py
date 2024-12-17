list_f = ['1.txt', '2.txt', '3.txt']
all_wrt_txt = []
txt_to_file_out = ''

for name_file in list_f:
    file_list = []
    with open(name_file, 'rt', encoding='utf-8') as f:
        read_txt = f.read()
        row_count = len(read_txt.rstrip().split('\n'))
        file_list.append(read_txt.rstrip())
        file_list.append(str(row_count))
        file_list.append(name_file)
        all_wrt_txt += [file_list]


for row_, qua_list, f_name in sorted(all_wrt_txt, key=lambda f_txt: len(f_txt[0])):
    txt_to_file_out += (f_name + '\n' + qua_list + '\n' + row_ + '\n')


with open('all_wrt_txt.txt', 'w', encoding='utf-8') as fo:
    fo.write(txt_to_file_out)
