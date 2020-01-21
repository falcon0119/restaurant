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

   #PLEASE TRY IF IT RUNS

    print('--------------------')

    food_order = input('Please select a number from the food menu: ')
    
    while food_order.isalpha():
        print("Please insert a valid number.")
        print()
        food_order = input('Please select a number from the food menu: ')
        
    while int(food_order) > index or int(food_order) < 0:
        print("Please insert a valid number.")
        print()
        food_order = input('Please select a number from the food menu: ')

    selected_food = foods[int(food_order)]
    
    drink_order = input('Please select a number from the drink menu: ')
    
    while drink_order.isalpha():
        print("Please insert a valid number.")
        print()
        food_order = input('Please select a number from the drink menu: ')
        
    while int(drink_order) > index or int(drink_order) < 0:
        print("Please insert a valid number.")
        print()
        drink_order = input('Please select a number from the drink menu: ')
        
    selected_drink= drinks[int(drink_order)]

# コンソールから入力を受け取り、変数countに代入してください
    count = int(input('How many sets would you like to purchase？(10% off when you purchase 3 sets): '))


# selected_foodとselected_drinkのそれぞれに対して、get_total_priceメソッドを呼び出してください
    result = selected_food.get_total_price(count) + selected_drink.get_total_price(count)

# 「合計は〇〇円です」となるように出力してください
    print('Your total is ' + str(result) + ' Yen')


