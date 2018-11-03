# 留言筆數計算
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

#計算留言的平均度
sum_len = 0
for line in data:
	sum_len += len(line)
print('留言的平均長度為', sum_len/len(data))

# 篩選100字內的留言筆數
new = []
for d in data:
	if len(d.strip()) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100個字')
print(new[0])

# 篩選有good的留言筆數
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')
print(good[0])



