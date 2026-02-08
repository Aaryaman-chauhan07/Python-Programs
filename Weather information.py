import requests
city = input("Enter a city name: ")
# please enter your api key in place of YOUR_API_KEY
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY&units=metric"
r = requests.get(url)
print(r.text)