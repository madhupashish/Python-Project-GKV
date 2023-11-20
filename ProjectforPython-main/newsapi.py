import requests
def apple_news():
    url = "https://newsapi.org/v2/everything?q=apple&from=2023-10-28&to=2023-10-28&sortBy=popularity&apiKey=39920781504f49b5b97ef4d2ec9afb7b"

    news = requests.get(url).json()

    articles = news["articles"]

    my_articles = []
    my_news = ""

    for article in articles:
        my_articles.append(article["title"])

    for i in range(10):
        my_news = my_news + my_articles[i] + "\n"


    print(my_news)

def business_news():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=39920781504f49b5b97ef4d2ec9afb7b"

    news = requests.get(url).json()

    articles = news["articles"]

    my_articles = []
    my_news = ""

    for article in articles:
        my_articles.append(article["title"])

    for i in range(10):
        my_news = my_news + my_articles[i] + "\n"


    print(my_news)

def tech_news():
    url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=39920781504f49b5b97ef4d2ec9afb7b"

    news = requests.get(url).json()

    articles = news["articles"]

    my_articles = []
    my_news = ""

    for article in articles:
        my_articles.append(article["title"])

    for i in range(10):
        my_news = my_news + my_articles[i] + "\n"


    print(my_news)


print("Here are the news for you .\n You have to choose what you want to see")
try:
    what_news = int(input("Choose an integer from the option below : \n  1. Apple News   2. Tech News  3.Business News\n==>>"))
    print("Please wait for a second")

except Exception as e:
    print("You're entered something other than an integer")

if what_news == 1:
    apple_news()

elif what_news == 2:
    tech_news()

elif what_news == 3:
    business_news()



