import requests
import json
import pandas as pd

api_key = "your_api_key"

url = "https://api.yelp.com/v3/businesses/search"

headers = {
    "Authorization": "Bearer {}".format(api_key)
}

city = input("Enter city: ")

params = {
    "term": "food",
    "location": "{}".format(city)
    #"latitude": "37.786882",
    #"longitude": "-122.399972"
}

response = requests.get(url, headers=headers, params=params)

data = json.loads(response.text)

business = data["businesses"]

#print(response.text)

i = input("Type 1 if you want to chosse pd_print: ")

def pd_print(data):
    df = pd.json_normalize(business)
    print(df)

def simple_print(data):
    try:
        for business in data["businesses"]:
            print("{}".format(business["name"]))
            #if business["is_closed"]:
            #    print("is closed now")
            #else:
            #    print("is working now")
            print("Rating: {}".format(business["rating"]))
            print("Address: {}".format(business["location"]["address1"]))
            print("Phone: {}".format(business["phone"]))
            print("For more details: {}\n".format(business["url"]))
    except:
        print("city not found, try to write it more correctly")

if i == str(1):
    pd_print(data)
else:
    simple_print(data)