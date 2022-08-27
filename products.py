products = [] #大清單
while True:
	name = input('請輸入商品名稱:')
	if name == 'q': #quit
		break
	price = input('請輸入商品價個:')
	p = [] #小清單
	p.append(name)
	p.append(price) #8,9行等同於 p = [name, product]
	products.append(p) #大清單裝小清單_二維清單
print(products)



