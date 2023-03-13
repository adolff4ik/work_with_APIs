import requests

api_key = "your_api_key"

search_word = input("Введіть ключове слово для пошуку книг: ")

url = f"https://www.googleapis.com/books/v1/volumes?q={search_word}&key={api_key}"

response = requests.get(url)

data = response.json()['items']

print(data)

def print_volumeInfo(data):
    for book in data:
        try:
            print("{}".format(book['volumeInfo']['title']))
        except: pass
        try:
            print("{}".format(book['volumeInfo']['subtitle']))
        except: pass
        try:
            print(("author: {}".format(book['volumeInfo']['authors'])))
        except: pass
        try:
            print("publishedDate: {}\n".format(book['volumeInfo']['publishedDate']))
        except: pass
print_volumeInfo(data)