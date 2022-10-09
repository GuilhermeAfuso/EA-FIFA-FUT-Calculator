#!/usr/bin/env python
# coding: utf-8

# In[6]:


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

def abc():
    print(f'Buy price: {buy_price:_.0f}'.replace('.',',').replace('_','.'))
    print(f'Sell price: {sell_price:_.0f}'.replace('.',',').replace('_','.'))
    print(f'EA Tax: {ea_tax:_.0f}'.replace('.',',').replace('_','.'))

    if result > 0:
        print(f'Profit: {result:_.0f}'.replace('.',',').replace('_','.'))
    elif result == 0:
        print("You don't have profit.")
    else:
        print(f'Loss: {result:_.0f}'.replace('.',',').replace('_','.'))

abc()


# In[ ]:




