def act5():

    from food import Food
    from drink import Drink

    food1 = Food('GMC Omelette Rice (soup set)', 900, 630)
    food2 = Food('GMC Burger (soup and french fries set)', 1100, 550)
    food3 = Food('Tomato Spaghettini with Bacon and Onions', 950, 590)
    food4 = Food('Bolognese (soup and french fries set)', 1050, 690)
    food5 = Food('Carbonara (soup and french fries set)', 1100, 730)

    foods = [food1, food2, food3, food4, food5]

    drink1 = Drink('Coffee', 150, 0)
    drink2 = Drink('Tea', 150, 2)
    drink3 = Drink('Coca Cola', 200, 140)
    drink4 = Drink('Ginger Ale', 200, 140) 
    drink5 = Drink('Pineapple Juice', 200, 133)
               
    drinks = [drink1, drink2, drink3, drink4, drink5]

    
    
    print('フードメニュー')
    index = 0
    for food in foods:
        print(str(index) + '. ' + food.info())
        index += 1

    print('ドリンクメニュー')
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
    count = int(input('何セット買いますか？(3つ以上で1割引): '))

# selected_foodとselected_drinkのそれぞれに対して、get_total_priceメソッドを呼び出してください
    result =selected_food.get_total_price(count) + selected_drink.get_total_price(count)

# 「合計は〇〇円です」となるように出力してください
    print('合計は' + str(result) + '円です')
