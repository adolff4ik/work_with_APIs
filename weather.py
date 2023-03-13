import requests
import pandas as pd

misto ="london"

def get_weather(misto):
    api_key = "your_api_key"
    url = "http://api.openweathermap.org/data/2.5/weather?q={misto}&appid={api_key}&units=metric"
    response_get = requests.get(url)
    response_json = response_get.json
    return response_get

result = get_weather(misto)
if result is not None:
    df = pd.DataFrame([result])
    print(df)