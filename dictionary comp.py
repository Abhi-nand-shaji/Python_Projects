cities_in_F = {'New York': 30, 'Boston': 40, 'Kaipamangalam': 60}
cities_in_C = {key: round((value-32)*5/9) for (key,value) in cities_in_F.items()}
print(cities_in_C)


weather = {'Boston': 'sunny', 'Kaipamangalam': 'rainy', 'Kodungallur': 'tsunami'}
tsunami_cities = {key: value for (key,value) in weather.items() if value == "tsunami"}
print(tsunami_cities)

# using if/else

desc_cities = {key: "Warm" if value >= 35 else "Cold" for (key,value) in cities_in_F.items()}
print(desc_cities)

# using a function
def check_temp(value):
    if value >= 45:
        return "HOT"
    elif 45 >= value >= 35:
        return "Warm"
    else:
        return "Cold"


ad_cities = {key: check_temp(value) for (key,value) in cities_in_F.items()}
print(ad_cities)

