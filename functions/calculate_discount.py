#Creating a function that will help to calculate discount when a user enters price and % discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price - price * discount_percent/100
    else:
        return price

#input variables from user side

price = float(input('Enter Price: '))
discount_percent = float(input('Enter Discount Percentage: '))

print('Calculated Price: ', calculate_discount(price, discount_percent))