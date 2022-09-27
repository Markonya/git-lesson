count_lines = {}

for line in open('q4_urls.txt', encoding='utf8'):
    clean_line = line.strip()
    if clean_line not in count_lines:
        count_lines[clean_line] = 0
    count_lines[clean_line] += 1

out = open('q4_urls_result.txt', 'w', encoding='utf8')
for line in count_lines:
    sorted_count_lines = dict(sorted(count_lines.items(), key=lambda item: item[0]))
    count = sorted_count_lines[line.rstrip()]
    out.write(f'{line.strip()}\t{count}\n')
    # print(count)
    # print(sorted_count_lines)
out.close()
