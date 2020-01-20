def act4():

    from food import Food
    from drink import Drink

    food1 = Food('Bibimpa', 600, 600)
    food2 = Food('Shin Ramen Noodles Set Menu', 600, 700)
    food3 = Food('Cold Noodles ', 800, 500)
    food4 = Food('Spicy Tofu Soup', 800, 520)
    food5 = Food('Bulgogi Set Menu', 1000, 890)
             
    foods = [food1, food2, food3, food4, food5]

    drink1 = Drink('Mineral Water', 200, 0)
    drink2 = Drink('Oolong Tea', 200, 0)

    drinks= [drink1, drink2]
    
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
    result = selected_food.get_total_price(count) + selected_drink.get_total_price(count)

# 「合計は〇〇円です」となるように出力してください
    print('合計は' + str(result) + '円です')
