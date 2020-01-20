from restaurant_name import Restaurant_name

restaurant1 = Restaurant_name('High Five Salad', "サラダ", "早稲田駅")
restaurant2 = Restaurant_name('Thaliya', "カレー", "早稲田駅")
restaurant3 = Restaurant_name('Toden Table', "カフェ", "早稲田駅")
restaurant4 = Restaurant_name('Dondondon', "韓国料理", "早稲田駅")
restaurant5 = Restaurant_name('Good Morning Cafe', "カフェ", "早稲田駅")
restaurant6 = Restaurant_name('where is a dog','カフェ','早稲田駅')

restaurants = [restaurant1, restaurant2, restaurant3,restaurant4,restaurant5, restaurant6]


print('あなたにオススメのレストラン')
index = 0
for restaurant_name in restaurants:
    print(str(index) + '. ' + restaurant_name.info())
    index += 1

print('--------------------')

restaurant_order = int(input('行きたいレストランの番号を選択してください: '))
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

    
    
    




    
