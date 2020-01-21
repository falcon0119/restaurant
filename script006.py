def act6():

    from food import Food
    from drink import Drink
    from dessert import Dessert

    food1 = Food('Asian Curry Plate (soup and mini desert set)', 1200, 590)
    food2 = Food(' Rice Bowl with Vegetables (soup and mini desert set)', 1200, 370)
    food3 = Food('Pizza Toast (soup and mini desert set)', 1000, 310)
    food4 = Food('Vegan Plate (soup and mini dessert set)', 1200, 310)
    food5 = Food('Herb Fragrant Salt Pork Bowl (soup and mini dessert set)', 1000, 680)
    food6 = Food('Skip',0,0)

    foods = [food1, food2, food3, food4, food5, food6]

    drink1 = Drink('Decaf Coffee', 450, 0)
    drink2 = Drink('Organic Black Tea', 450, 0)
    drink3 = Drink('Morinaga Tea', 500, 0)
    drink4 = Drink('Citrus Unshiu Juice', 450, 35) 
    drink5 = Drink('Perrier', 350, 0)
    drink6 = Drink('Skip',0,0)
               
    drinks = [drink1, drink2, drink3, drink4, drink5, drink6]

    dessert1 = Dessert('Pancake with Vegan Butter and Fruits', 880, 105)
    dessert2 = Dessert('Waffles with Soy Milk Whipped Cream and Fruits', 880, 180)
    dessert3 = Dessert('Brownie Soy Milk Whipped', 650, 200)
    dessert4 = Dessert('Clafoutis with Shanti Sauce', 700, 250)
    dessert5 = Dessert('Coconut Kudzu Pudding', 650, 140)
    dessert6 = Dessert('Skip',0,0)

    desserts = [dessert1, dessert2, dessert3, dessert4, dessert5, dessert6]
    
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

    print()
    print('***** DESSERT MENU *****')
    index = 0
    for dessert in desserts:
        print(str(index) + '. ' + dessert.info())
        index += 1
    

    print('--------------------')

    food_order = int(input('Please select a number from the food menu: '))
    selected_food = foods[food_order]

    drink_order = int(input('Please select a number from the drink menu: '))
    selected_drink = drinks[drink_order]
    
    dessert_order = int(input('Please select a number from the dessert menu: '))
    selected_dessert = desserts[dessert_order]

# コンソールから入力を受け取り、変数countに代入してください
    count = int(input('何セット買いますか？(3つ以上で1割引): '))

# selected_foodとselected_drinkのそれぞれに対して、get_total_priceメソッドを呼び出してください
    result =selected_food.get_total_price(count) + selected_drink.get_total_price(count) + selected_dessert.get_total_price(count)

# 「合計は〇〇円です」となるように出力してください
    print()
    print('----------------------------------------------------------')
    print('Your order is:')
    print(str(selected_food.name) + ' ¥' + str(selected_food.price) + ' x ' + str(count))
    print(str(selected_dressing.name) + ' ¥' + str(selected_dressing.price) + ' x ' + str(count))
    print(str(selected_drink.name) + ' ¥' + str(selected_drink.price) + ' x ' + str(count))
    print('----------------------------------------------------------')
    print('Your total is ' + str(result) + ' Yen')
    print('----------------------------------------------------------')
