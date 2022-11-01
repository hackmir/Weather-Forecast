import requests

while True:

    city = input("which city's weather do you want to forecast?:\n")

    print(f"Displaying weather report for: {city}")

    url = 'https://wttr.in/{}'.format(city)

    res = requests.get(url)

    print(res.text)

    if input("Would you like to know the forecast for another city? Y/N\n") in {"n", "N"}:
        break


