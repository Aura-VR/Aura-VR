collect_file = open('../data/dead_y_info.aura', 'r+')
write_file = open('../data/normalize_dead_y_info.aura', 'w+')
unique_y = []
unique_h = []
for line in collect_file:
    array = line.split(' ')
    if float(array[1]) < 56:
        continue
    if array[0] not in unique_y or array[1] not in unique_h:
        unique_y.append(array[0])
        unique_h.append(array[1])
        write_file.write(line)
