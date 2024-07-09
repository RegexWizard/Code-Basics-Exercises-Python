
Country_List = {
    "China": 143,
    "India": 136,
    "USA": 32,
    "Pakistan": 21
}

def Print_List_Country():
    for key, value in Country_List.items():
        print(key, "==>", value)

def Add_Populations(country_name):
    populations = int(input(f"Add the populations of {country_name} (in millions): "))
    Country_List[country_name] = populations
    Print_List_Country()
    return country_name, populations

def Check_Dictionary(str, action):
    if action == "add":
        if str in Country_List:
            print(str, "already exists in our database!")
        else:
            Add_Populations(str)

    elif action == "remove":
        if str in Country_List:
            print(str, "has been found in the database and will be removed!")
            Country_List.pop(str)
            Print_List_Country()
        else:
            print(str, "is not found in the database!")
    
    elif action =="query":
        if str in Country_List:
            print(Country_List[str], "is the total populations (in millions) of the", str)
        else:
            print(str, "isn't found in our databases!")

user_input = input("Type what you want (Print, Add, Remove, Query): ").lower()

if user_input == "print":
    Print_List_Country()
    
elif user_input == "add":
    new_country = input("Type the country name: ")
    Check_Dictionary(new_country, "add")
    
elif user_input == "remove":
    remove_country = input("Type the country name: ")
    Check_Dictionary(remove_country, "remove")

elif user_input == "query":
    query = input("Type the country name: ")
    Check_Dictionary(query, "query")

Stock = {
    "info": [600, 630, 620],
    "ril": [1430, 1490, 1567],
    "mtl": [234, 180, 160]
}

user_input = input("Hey, what do you want? (Print, Add): ").lower()

if user_input == "print":
    
    for k, v in Stock.items():
       averages = sum(v) / len(v)
       print(f"{k} ==> {v} ==> {averages}")
       
elif user_input == "add":
    
    add_input = input("What you want to add: ")
    
    if add_input in Stock:
        
        print(f"{add_input} is on the databases!")
        number_input = input(f"How much will you append to {add_input}? ")
        Stock[add_input].append(int(number_input))
        print(Stock[add_input])
        
    else:
        
        print(f"{add_input} isn't on the databases!")
        number_input = input(f"How much will you append to {add_input}? ")
        Stock[add_input] = [int(number_input)]
        print(Stock[add_input])

import math

def circle_calc(radius):
    diameter = radius * 2
    area = math.pi * (radius ** 2)
    print(f"Print the diamter of the circle is {diameter}. & the area of this circle is {area}")
    return area

user_inp = int(input("Type the radius of a circle: "))
circle_calc(user_inp)