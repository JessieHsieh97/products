import os #作業系統

products = [] #大清單
if os.path.isfile('products.csv'): #檢查檔案在不在
	print('找到檔案！')
	with open('products.csv', 'r', encoding = 'utf-8') as f: #讀取檔案
		for line in f:
			if '商品, 價格' in line:
				continue #跳到下一次迴圈_跳過商品價個那一行，其他行繼續
			name, price = line.strip().split(',') #strip()去掉\n_split()檔案中遇到逗點就split
			products.append([name, price])
	print(products)
else:
	print('找不到檔案')

#讓使用者輸入
while True:
	name = input('請輸入商品名稱:')
	if name == 'q': #quit
		break
	price = input('請輸入商品價個:')
	p = [] #小清單
	p.append(name)
	p.append(price) #8,9行等同於 p = [name, product]
	products.append(p) #大清單裝小清單_二維清單

#印出所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1]) #每一個小清單的第０格都是name,第一格是price

#寫入程式
#生成csv檔可以excel讀取
with open('products.csv', 'w', encoding = 'utf-8') as f: #將編碼寫為utf-8格式
	f.write('商品, 價格 \n')
	for p in products:
		f.write(p[0] + ',' + p[1] +  '\n')

