import requests
import json
from datetime import datetime, timedelta


def get_news():
    api_key = "0cb62767d0da4bc095431464212f6039"
    url = f"https://newsapi.org/v2/everything"


    end_date = datetime.now().strftime("%Y-%m-%d")
    start_date = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")

    params = {
        "q": "(early childhood education) AND (parenting)",
        "apiKey": api_key,
        "language": "en",
        "sortBy": "relevancy",
        "pageSize": 3,
        "from": start_date,
        "to": end_date
    }

    response = requests.get(url, params=params)

    # Проверка статуса
    if response.status_code != 200:
        print(f"Ошибка API: {response.status_code}")
        print(response.text)  # Вывод полного ответа (отладка)


    try:
        data = response.json()

        # Проверка наличия ключа 'articles'
        if 'articles' not in data:
            print("Структура ответа изменилась или произошла ошибка.")
            print(json.dumps(data, indent=2))


        articles = data["articles"]

        # Проверка, на количесто статей в списке
        if len(articles) == 0:
            print("Получен пустой список статей.")
            print(json.dumps(data, indent=2))


        return articles

    except json.JSONDecodeError:
        print("Ответ не является валидным JSON.")
        print(response.text)


# тест
def news_cr():
    news_articles = get_news()
    if news_articles:
        for article in news_articles[1:2]:
            return (article['title'])
    else:
        print("Не удалось получить новости.")
