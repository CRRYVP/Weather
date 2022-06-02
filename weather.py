import requests


a=float(input("What is the Latitude?     "))
b=float(input("What is the Longitude?     "))
a=str(a)
b=str(b)
url="https://api.openweathermap.org/data/2.5/onecall?lat="+a+"&lon="+b+"&units=metric&appid=d6ef1ec3e05236bca7b316d599643f80"
p1=requests.get(url)
p2=p1.json()
print("")

print("Temperature:"+str(p2["current"]["temp"])+" C")
print("Feels Like:"+str(p2["current"]["feels_like"])+" C")
print("Humidity:"+str(p2["current"]["humidity"]))
print("Pressure:"+str(p2["current"]["pressure"])+" HPA")
print("Wind Speed:"+str(p2["current"]["wind_speed"])+" MPH")
print("Dew Point:"+str(p2["current"]["dew_point"])+" C")




