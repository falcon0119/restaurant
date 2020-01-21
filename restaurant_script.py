from restaurant_name import Restaurant_name

restaurant1 = Restaurant_name('High Five Salad', "Salad", "Waseda")
restaurant2 = Restaurant_name('Thaliya', "Curry", "Waseda")
restaurant3 = Restaurant_name('Toden Table', "Japanese food", "Waseda")
restaurant4 = Restaurant_name('Dondondon', "Korean food", "Waseda")
restaurant5 = Restaurant_name('Good Morning Cafe', "Western food", "Waseda")
restaurant6 = Restaurant_name('where is a dog','Vegan Cafe','Waseda')

restaurants = [restaurant1, restaurant2, restaurant3,restaurant4,restaurant5, restaurant6]


print('These are the restaurants that we reccomend around Waseda area!')
index = 0
for restaurant_name in restaurants:
    print(str(index) + '. ' + restaurant_name.info())
    index += 1

print('--------------------')

restaurant_order = int(input('Please enter the number of desired restaurant: '))
selected_restaurant = restaurants[restaurant_order]

   
import script001
import script002
import script003
import script004
import script005
import script006


if restaurant_order ==0 :
    script001.act1()

elif restaurant_order ==1 :
    script002.act2()

elif restaurant_order ==2 :
    script003.act3()

elif restaurant_order ==3 :
    script004.act4()

elif restaurant_order ==4 :
    script005.act5()

elif restaurant_order ==5 :
    script006.act6()

    
    
    




    
