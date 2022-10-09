# EA FIFA FUT Calculator

buy_price = int(input('Enter the purchase price: '))

while buy_price < 0:
    print('The purchase price must be higher or equal than zero.')
    buy_price = int(input('Enter the purchase price: '))

sell_price = int(input('Enter the sell price: '))

while sell_price <= 0:
    print('The sell price must be higher than zero.')
    sell_price = int(input('Enter the sell price: '))

ea_tax = sell_price * 0.05

result = sell_price - ea_tax - buy_price


def check():
    print(f'Buy price: {buy_price:,.0f}')
    print(f'Sell price: {sell_price:,.0f}')
    print(f'EA Tax: {ea_tax:,.0f}')

    if result > 0:
        print(f'Profit: {result:,.0f}')
    elif result == 0:
        print("You don't have profit.")
    else:
        print(f'Loss: {result:,.0f}')


check()
