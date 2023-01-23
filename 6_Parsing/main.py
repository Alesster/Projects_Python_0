import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

def get_first_news():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0"
    }
    
    url = "https://www.securitylab.ru/news/"
    r = requests.get(url = url, headers=headers)
    
    soup = BeautifulSoup(r.text, "lxml")
    article_cards = soup.find_all("a", class_ = "article-card")
    
    news_dict = {}
    for article in article_cards:
        article_title = article.find("h2", class_="article-card-title").text.strip()
        article_desc = article.find("p").text.strip()
        article_url = f'https://www.securitylab.ru{article.get("href")}'
        
        article_date_time = article.find("time").get("datetime")
        date_from_iso = datetime.fromisoformat(article_date_time)
        date_time = datetime.strftime(date_from_iso, "%d-%m-%Y %H:%M:%S")
        article_date_timestamp = time.mktime(datetime.strptime(date_time, "%d-%m-%Y %H:%M:%S").timetuple())
        
        article_id = article_url.split("/")[-1]
        article_id = article_id[:-4]
        
        #print(f"{article_title} | {article_url} | {article_date_timestamp}")
        
        news_dict[article_id] = {
            "article_date_timestamp": article_date_timestamp,
            "article_title":  article_title,
            "article_url": article_url,
            "article_desc": article_desc
        }
        
    with open("news_dict.json", "w") as file:
        json.dump(news_dict, file, indent=4, ensure_ascii=False)
    
    return news_dict
        
def check_news_update():
    with open("news_dict.json") as file:
        news_dict = json.load(file)
        
#    print(news_list)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0"
    }
    
    url = "https://www.securitylab.ru/news/"
    r = requests.get(url = url, headers=headers)
    
    soup = BeautifulSoup(r.text, "lxml")
    article_cards = soup.find_all("a", class_ = "article-card")
    
    fresh_news = {}
    for article in article_cards:
        article_url = f'https://www.securitylab.ru{article.get("href")}'
        article_id = article_url.split("/")[-1]
        article_id = article_id[:-4]
        
        if article_id in news_dict:
            continue
        else:
            article_title = article.find("h2", class_="article-card-title").text.strip()
            article_desc = article.find("p").text.strip()
            
            article_date_time = article.find("time").get("datetime")
            date_from_iso = datetime.fromisoformat(article_date_time)
            date_time = datetime.strftime(date_from_iso, "%d-%m-%Y %H:%M:%S")
            article_date_timestamp = time.mktime(datetime.strptime(date_time, "%d-%m-%Y %H:%M:%S").timetuple())
            
            news_dict[article_id] = {
            "article_date_timestamp": article_date_timestamp,
            "article_title":  article_title,
            "article_url": article_url,
            "article_desc": article_desc
            }
            
            fresh_news[article_id] = {
            "article_date_timestamp": article_date_timestamp,
            "article_title":  article_title,
            "article_url": article_url,
            "article_desc": article_desc                
            }      
            
    with open("news_dict.json", "w") as file:
        json.dump(news_dict, file, indent=4, ensure_ascii=False)
        
    return fresh_news

def main():
    get_first_news()
    print(check_news_update())
        
if __name__=='__main__':
    main()