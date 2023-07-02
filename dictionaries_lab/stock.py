stock_list = input().split()
stock_dict = {}

for i in range(0, len(stock_list), 2):
    key = stock_list[i]
    value = int(stock_list[i + 1])
    stock_dict[key] = value

search_list = input().split()

for product in search_list:
    if product in stock_dict:
        print(f'We have {stock_dict[product]} of {product} left')
    else:
        print(f"Sorry, we don't have {product}")



