count_lines = {}
for line in open(r'C:\Games\Python\q4_urls.txt', encoding='utf8'):
    clean_line = line.rstrip()
    if clean_line not in count_lines:
        count_lines[clean_line] = 0
    count_lines[clean_line] += 1

out = open(r'C:\Games\Python\q4_urls_result.txt', 'w', encoding='utf8')
for line in open(r'C:\Games\Python\q4_urls.txt', encoding='utf8'):
    count = count_lines[line.rstrip()]
    out.write(f'{line.strip()}\t{count}\n')

out.close()

