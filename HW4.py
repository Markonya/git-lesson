count_lines = {}

for line in open('q4_urls.txt', encoding='utf8'):
    clean_line = line.strip()
    # print(clean_line)
    if clean_line not in count_lines:
        count_lines[clean_line] = 0
    count_lines[clean_line] += 1

out = open('q4_urls_result.txt', 'w', encoding='utf8')
for key in sorted(count_lines.keys()):
    out.write(f'{key.strip()}\t{count_lines[key]}\n')

out.close()
