def act2():

    from food import Food
    from drink import Drink

    food1 = Food('Thaliya Bento', 680, 870)
    food2 = Food('Indian Curry Box', 500, 650)
    food3 = Food('Keema Curry Lunch Box', 720, 760)
    food4 = Food('Chicken Pakora Lunch Box', 720, 650)
    food5 = Food('Tandori Chicken Lunch Box', 1020, 870)

    foods = [food1, food2, food3, food4, food5]

    drink1 = Drink('Mango Lassi', 350, 300)
    drink2 = Drink('Chai Milk Tea Tapioca', 350, 300)
    drink3 = Drink('Strawberry Lassi', 350, 300)
    drink4 = Drink('Melon Milk Tapioca', 350, 300)
    drink5 = Drink('Matcha Lassi', 350, 300)

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

    drink_order = int(input('ドレッシングの番号を選択してください: '))
    selected_drink = drinks[drink_order]

# コンソールから入力を受け取り、変数countに代入してください
    count = int(input('何セット買いますか？(3つ以上で1割引): '))

# selected_foodとselected_drinkのそれぞれに対して、get_total_priceメソッドを呼び出してください
    result = selected_food.get_total_price(count) + selected_drink.get_total_price(count)

# 「合計は〇〇円です」となるように出力してください
    print('合計は' + str(result) + '円です')
