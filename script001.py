def act1():

    from food import Food
    from drink import Drink
    from dressing import Dressing

    food1 = Food('High Five Power Salad', 1580, 476)
    food2 = Food('Smoked Duck & Honey Nut Salad', 1080, 220)
    food3 = Food("Grilled Chicken & Egg Salad", 980, 262)
    food4 = Food('Prosciutto & Mimolette Cheese Salad', 980, 139)
    food5 = Food('Garlic Shrimp Salad', 1280, 113)
    food6 = Food('Skip', 0, 0)

    foods = [food1, food2, food3, food4, food5, food6]
    
    dressing1 = Dressing('Classic Caesar',0,73)
    dressing2 = Dressing('Onion Soy',0,107)
    dressing3 = Dressing('Creamy Seasame',0,67)
    dressing4 = Dressing('Honey Mustard',0,127)
    dressing5 = Dressing('Balsamic Vinaigrette',0,127)
    dressing6 = Dressing('Skip',0,0)

    dressings = [dressing1, dressing2, dressing3, dressing4, dressing5, dressing6]
    
    drink1 = Drink('Green Smoothie', 360, 126)
    drink2 = Drink('Homemade Soup', 360, 234)
    drink3 = Drink('Iced Coffee', 100, 15)
    drink4 = Drink('Seasonal Smoothie', 500, 245)
    drink5 = Drink('Skip',0, 0) 

    drinks = [drink1, drink2, drink3, drink4, drink5]
    
    print()
    print('***** FOOD MENU *****')
    index = 0
    for food in foods:
        print(str(index) + '. ' + food.info())
        index += 1

    print()    
    print('***** DRESSING MENU *****')
    index = 0
    for dressing in dressings:
        print(str(index) + '. ' + dressing.info())
        index += 1

    print()
    print('***** DRINK MENU *****')
    index = 0
    for drink in drinks:
        print(str(index) + '. ' + drink.info())
        index += 1

    print('--------------------')

   #if choose invalid numbers
        
    print('--------------------')


    while True:
        food_order = input('Please select a number from the food menu: ')

        if food_order == '0' or food_order == '1' or food_order == '2' or food_order == '3' or food_order == '4' or food_order == '5' or food_order == '6':
            selected_food = foods[int(food_order)]

        else:
            print("Please insert a valid number.")
            print()
            continue
        
        break
        
    while True:
        dressing_order = input('Please select a number from the dressing menu: ')

        if dressing_order == '0' or dressing_order == '1' or dressing_order == '2' or dressing_order == '3' or dressing_order == '4' or dressing_order == '5':
            selected_dressing = dressings[int(dressing_order)]

        else:
            print("Please insert a valid number.")
            print()
            continue
        
        break        

    while True:
        drink_order = input('Please select a number from the drink menu: ')

        if drink_order == '0' or drink_order == '1' or drink_order == '2' or drink_order == '3' or drink_order == '4' or drink_order == '5':
            selected_drink = drinks[int(drink_order)]

        else:
            print("Please insert a valid number.")
            print()
            continue
        
        break
     
    count = int(input('How many sets would you like to purchase？(10% off when you purchase 3 sets): '))


    result = selected_food.get_total_price(count) + selected_drink.get_total_price(count)

#print total

    print()
    print('----------------------------------------------------------')
    print('Here is your total order:')
    print()
    print(str(selected_food.name) + ' ¥' + str(selected_food.price) + ' x ' + str(count))
    print(str(selected_dressing.name) + ' ¥' + str(selected_dressing.price) + ' x ' + str(count))
    print(str(selected_drink.name) + ' ¥' + str(selected_drink.price) + ' x ' + str(count))
    
    if count>=3:
        print ('10% discount')

    else:
        print('    ')

    print('----------------------------------------------------------')
    print('Your total is ' + str(result) + ' Yen')
    print()
    print('Thank you for using W-Delivers! We hope to serve you again soon!')
    print('----------------------------------------------------------')
    print()
    print('Your order is on its way')

    import time

    for i in range(100):
        print('.', end='')
        time.sleep(1)



