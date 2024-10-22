from blog import generate_blog_text
from txt4img import generate_image_text
from img import create_img
from res import save_res
from news import get_news

def run_assistant():
    news_articles = get_news()

    for article in news_articles[1:2]:
        blog_text = generate_blog_text(article["title"] + " " + article["description"])
        image_text = generate_image_text(blog_text)
        create_img(image_text)
        save_res(blog_text, image_text)
        print(f"выбранная статья: {article['title']}")


if __name__ == "__main__":
    run_assistant()
