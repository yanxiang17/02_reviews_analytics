data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 5000 == 0:
			print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料。')
print('第2筆留言資料是：------\n', data[2])

sum_len = 0
for line in data:
	sum_len += len(line)
print('留言的平均長度為', sum_len/len(data))

