import os #作業系統

#讀取檔案
def read_file(filename):
	products = [] #大清單
	with open(filename, 'r', encoding = 'utf-8') as f: #讀取檔案
		for line in f:
			if '商品, 價格' in line:
				continue #跳到下一次迴圈_跳過商品價個那一行，其他行繼續
			name, price = line.strip().split(',') #strip()去掉\n_split()檔案中遇到逗點就split
			products.append([name, price])
	return products

#讓使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱:')
		if name == 'q': #quit
			break
		price = input('請輸入商品價個:')
		price = int(price)		
		products.append([name, price]) #大清單裝小清單_二維清單
	print(products)
	return products

#印出所有購買紀錄
def print_product(products):
	for p in products:
		print(p[0], '的價格是', p[1]) #每一個小清單的第０格都是name,第一格是price

#寫入程式
#生成csv檔可以excel讀取
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f: #將編碼寫為utf-8格式
		f.write('商品, 價格 \n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) +  '\n')

#程式的進入點＿執行
def main():
	filename = 'products.csv'
	if os.path.isfile(filename): 
		print('找到檔案！')
		products = read_file(filename) 
	else:
			print('找不到檔案')
	products = user_input(products)
	print_product(products)
	write_file(filename, products)

main()