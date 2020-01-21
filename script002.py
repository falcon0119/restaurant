def act2():

    from food import Food
    from drink import Drink

    food1 = Food('Thaliya Bento', 680, 870)
    food2 = Food('Indian Curry Box', 500, 650)
    food3 = Food('Keema Curry Lunch Box', 720, 760)
    food4 = Food('Chicken Pakora Lunch Box', 720, 650)
    food5 = Food('Tandori Chicken Lunch Box', 1020, 870)
    food6 = Food('Skip', 0, 0)

    foods = [food1, food2, food3, food4, food5, food6]

    drink1 = Drink('Mango Lassi', 350, 300)
    drink2 = Drink('Chai Milk Tea Tapioca', 350, 300)
    drink3 = Drink('Strawberry Lassi', 350, 300)
    drink4 = Drink('Melon Milk Tapioca', 350, 300)
    drink5 = Drink('Matcha Lassi', 350, 300)
    drink6 = Drink('Skip', 0, 0)

    drinks = [drink1, drink2, drink3, drink4, drink5, drink6]
    
    print()
    print('***** FOOD MENU *****')
    index = 0
    for food in foods:
        print(str(index) + '. ' + food.info())
        index += 1

    print()
    print('***** DRINK MENU *****')
    index = 0
    for drink in drinks:
        print(str(index) + '. ' + drink.info())
        index += 1

#if choose invalid numbers
        
    print('--------------------')


    while True:
        food_order = input('Please select a number from the food menu: ')

        if food_order == '0' or food_order == '1' or food_order == '2' or food_order == '3' or food_order == '4' or food_order == '5':
            selected_food = foods[int(food_order)]

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
     

# コンソールから入力を受け取り、変数countに代入してください
    count = int(input('How many sets would you like to purchase？(10% off when you purchase 3 sets): '))


# selected_foodとselected_drinkのそれぞれに対して、get_total_priceメソッドを呼び出してください
    result = selected_food.get_total_price(count) + selected_drink.get_total_price(count)

# 「合計は〇〇円です」となるように出力してください
    print()
    print('----------------------------------------------------------')
    print('Here is your total order:')
    print()
    print(str(selected_food.name) + ' ¥' + str(selected_food.price) + ' x ' + str(count))
    print(str(selected_drink.name) + ' ¥' + str(selected_drink.price) + ' x ' + str(count))
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


