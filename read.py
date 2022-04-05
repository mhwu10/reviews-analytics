data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        count += 1
        data.append(line)
        if count % 1000 == 0:
            print(len(data))
print('Reading is done, there are', len(data), 'comments')

sum_len = 0
for dline in data:
    sum_len = sum_len + len(dline)

print('The average length of comments is', sum_len / len(data), 'digitals')

#print(data[0])
#print('-----------------')
#print(data[1])
