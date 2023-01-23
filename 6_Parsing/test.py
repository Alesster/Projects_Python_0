# url = "https://www.securitylab.ru/news/535898.php"

# article_id = url.split("/")[-1]
# article_id = article_id[:-4]
# print(article_id)

import json

with open("news_dict.json") as file:
    news_dict = json.load(file)
    
search_id = "5358945328"

if search_id in news_dict:
    print("The new is already extsts")
else:
    print("The latest new, add to dictionary")