def act6():

    from food import Food
    from drink import Drink

    food1 = Food('Asian Curry Plate (soup and mini desert set)', 1200, 590)
    food2 = Food(' Rice Bowl with Vegetables (soup and mini desert set)', 1200, 370)
    food3 = Food('Pizza Toast (soup and mini desert set)', 1000, 310)
    food4 = Food('Vegan Plate (soup and mini dessert set)', 1200, 310)
    food5 = Food('Herb Fragrant Salt Pork Bowl (soup and mini dessert set)', 1000, 680)

    foods = [food1, food2, food3, food4, food5]

    drink1 = Drink('Decaf Coffee', 450, 0)
    drink2 = Drink('Organic Black Tea', 450, 0)
    drink3 = Drink('Morinaga Tea', 500, 0)
    drink4 = Drink('Citrus Unshiu Juice', 450, 35) 
    drink5 = Drink('Perrier', 350, 0)
               
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
