def act4():

    from food import Food
    from drink import Drink

    food1 = Food('Bibimpa', 600, 600)
    food2 = Food('Shin Ramen Noodles Set Menu', 600, 700)
    food3 = Food('Cold Noodles ', 800, 500)
    food4 = Food('Spicy Tofu Soup', 800, 520)
    food5 = Food('Bulgogi Set Menu', 1000, 890)
    food6 = Food('Skip', 0, 0)
             
    foods = [food1, food2, food3, food4, food5]

    drink1 = Drink('Mineral Water', 200, 0)
    drink2 = Drink('Oolong Tea', 200, 0)
    drink3 = Drink('Skip',0 ,0) 

    drinks= [drink1, drink2]
    
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

    print('--------------------')

    food_order = int(input('Please select a number from the food menu: '))
    selected_food = foods[food_order]

    drink_order = int(input('Please select a number from the drink menu: '))
    selected_drink = drinks[drink_order]

    count = int(input('How many sets would you like to purchase？(10% off when you purchase 3 sets): '))

    result = selected_food.get_total_price(count) + selected_drink.get_total_price(count)

    print()
    print('----------------------------------------------------------')
    print('Here is your total order:')
    print()
    print(str(selected_food.name) + ' ¥' + str(selected_food.price) + ' x ' + str(count))
    print(str(selected_dressing.name) + ' ¥' + str(selected_dressing.price) + ' x ' + str(count))
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
