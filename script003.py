def act3():

    from food import Food
    from drink import Drink

    food1 = Food('Miso Soup with Pork and Vegetables Set Menu', 1000, 510)
    food2 = Food('Chicken and Deep-fried Tofu Set Menu ', 1000, 400)
    food3 = Food('Grilled Saba Fish Set Menu', 1100, 550)
    food4 = Food('Deep-fried Oyster Set Menu', 1200, 620)
    food5 = Food('Curry Rice', 900, 600)
    food6 = Food('Skip', 0, 0) 

    foods = [food1, food2, food3, food4, food5]

    drink1 = Drink('100% Apple Juice', 500, 50)
    drink2 = Drink('100% Mikan Juice', 500, 50)
    drink3 = Drink(' Ginger Soda', 400, 40)
    drink4 = Drink('Skip', 0, 0) 

    drinks = [drink1, drink2, drink3]
    
    print('FOOD MENU')
    index = 0
    for food in foods:
        print(str(index) + '. ' + food.info())
        index += 1

    print('DRINK MENU')
    index = 0
    for drink in drinks:
        print(str(index) + '. ' + drink.info())
        index += 1

    print('--------------------')

    food_order = int(input('食べ物の番号を選択してください: '))
    selected_food = foods[food_order]

    drink_order = int(input('ドリンクの番号を選択してください: '))
    selected_drink = drinks[drink_order]

# コンソールから入力を受け取り、変数countに代入してください
    count = int(input('How many sets would you like to purchase？(10% off when you purchase 3 or more sets): '))

# selected_foodとselected_drinkのそれぞれに対して、get_total_priceメソッドを呼び出してください
    result = selected_food.get_total_price(count) + selected_drink.get_total_price(count)

# 「合計は〇〇円です」となるように出力してください
    print('Your total is ' + str(result) + ' Yen')
