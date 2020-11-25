import requests

zip = input("What is the zip code you would like to check? : ")
country_code = input("In Which Country is that zip?")

my_weather = requests.get(
    f"http://api.openweathermap.org/data/2.5/weather?zip={zip},{country_code}&units=imperial&appid=8af2aa7fa978da0c3dc608a85406875c"
)

data = my_weather.json()

'''city = data["name"]
temp = data["main"]["temp"]


print(f"Today in {city} it is {temp} degrees")'''

print(data)