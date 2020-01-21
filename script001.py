def act1():

    from food import Food
    from drink import Drink

    food1 = Food('High Five Power Salad', 1580, 476)
    food2 = Food('Smoked Duck & Honey Nut Salad', 1080, 220)
    food3 = Food("Grilled Chicken & Egg Salad", 980, 262)
    food4 = Food('Prosciutto & Mimolette Cheese Salad', 980, 139)
    food5 = Food('Garlic Shrimp Salad', 1280, 113)
    food6 = Food('Skip', 0, 0)

    foods = [food1, food2, food3, food4, food5, food6]
    
    drink1 = Drink('Classic Caesar',0,73)
    drink2 = Drink('Onion Soy',0,107)
    drink3 = Drink('Creamy Seasame',0,67)
    drink4 = Drink('Skip',0, 0)

    drinks = [drink1, drink2, drink3, drink4]
    
    print('Salad Menu')
    index = 0
    for food in foods:
        print(str(index) + '. ' + food.info())
        index += 1

    print('Dressing Menu')
    index = 0
    for drink in drinks:
        print(str(index) + '. ' + drink.info())
        index += 1

    print('--------------------')

    food_order = int(input('Please select a number from the food menu: '))
    selected_food = foods[food_order]

    drink_order = int(input('Please select a number from the drink menu: '))
    selected_drink = drinks[drink_order]

# コンソールから入力を受け取り、変数countに代入してください
    count = int(input('何セット買いますか？(3つ以上で1割引): '))

# selected_foodとselected_drinkのそれぞれに対して、get_total_priceメソッドを呼び出してください
    result = selected_food.get_total_price(count) + selected_drink.get_total_price(count)

# 「合計は〇〇円です」となるように出力してください
    print('Your total is ' + str(result) + ' Yen')
