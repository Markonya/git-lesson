count_lines = {}
new_count_lines = {}
for line in open('q4_urls.txt', encoding='utf8'):
    clean_line = line.strip()
    if clean_line not in count_lines:
        count_lines[clean_line] = 0
    count_lines[clean_line] += 1

out = open('q4_urls_result.txt', 'w', encoding='utf8')
for line in count_lines:
    sorted_values = sorted(count_lines.values())
    for i in sorted_values:

        for k in count_lines.keys():
            if count_lines[k] == i:
                new_count_lines[k] = count_lines[k]
            break

count = new_count_lines[line.rstrip()]

out.write(f"{line.strip()}\t{count}\n")

out.close()
