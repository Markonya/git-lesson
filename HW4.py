count_lines = {}

for line in open('q4_urls.txt', encoding='utf8'):
    clean_line = line.strip()
    # print(clean_line)
    if clean_line not in count_lines:
        count_lines[clean_line] = 0
    count_lines[clean_line] += 1

out = open('q4_urls_result.txt', 'w', encoding='utf8')
for line in count_lines:
    sorted_count_lines = dict(sorted(count_lines.items(), key=lambda item: item[1]))
    count = sorted_count_lines[line.rstrip()]
    # print(count)
    out.write(f'{line.strip()}\t{count}\n')
    # print(sorted_count_lines)
out.close()
