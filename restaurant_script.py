#lim

from restaurant_name import Restaurant_name

restaurant1 = Restaurant_name("High Five Salad", " / Salad", "Waseda")
restaurant2 = Restaurant_name("Thaliya", " / Indian food", "Waseda")
restaurant3 = Restaurant_name("Toden Table", " / Japanese food", "Waseda")
restaurant4 = Restaurant_name("Dondondon", " / Korean food", "Waseda")
restaurant5 = Restaurant_name("Good Morning Cafe", " / Western food", "Waseda")
restaurant6 = Restaurant_name("Where is a dog"," / Vegan Cafe","Waseda")

restaurants = [restaurant1, restaurant2, restaurant3,restaurant4,restaurant5, restaurant6]

print('----------------------------------------------------------')
print('---------------Hello, welcome to W-Delivers! --------------')
print('----------------------------------------------------------')
input('Please insert your name: ')
input('Please insert your faculty: ')
input('PLease insert your grade: ')
input('Please state the building and classroom number of pick up location (Only available for Waseda or Toyama Campus): ')
input('Please insert preferred time of pickup (specify am or pm) : ')
print('----------------------------------------------------------')
print('Please note that the only payment method available is CASH')
print('Incorrectly filled out order forms will not be accepted')
print('----------------------------------------------------------')
print()
print()

print('These are the restaurants that we recommend around Waseda!')
index = 0
for restaurant_name in restaurants:
    print(str(index) + '. ' + restaurant_name.info())
    index += 1
print()
   
import script001
import script002
import script003
import script004
import script005
import script006

#grace

while True:
    restaurant_order = input('Please enter a number of the restaurant you would like to order from: ')
    print('----------------------------------------------------------')

    if restaurant_order =='0' :
        script001.act1()

    elif restaurant_order =='1' :
        script002.act2()

    elif restaurant_order =='2' :
        script003.act3()

    elif restaurant_order =='3' :
        script004.act4()

    elif restaurant_order =='4' :
        script005.act5()

    elif restaurant_order =='5' :
        script006.act6()
        
    else:
        print('ERROR:Invalid Input. Try Again!')
        print()
        continue
    
    break
    
    
