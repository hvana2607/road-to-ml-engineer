import os
from dotenv import load_dotenv
import asyncio
import aiohttp
import json 

load_dotenv()

NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
GNEWS_KEY = os.getenv("GNEWS_KEY")
GUARDIAN_KEY = os.getenv("GUARDIAN_KEY")


SOURCES = [{"name": "NewsAPI", "url": "https://newsapi.org/v2/top-headlines", "params": {"apiKey": NEWSAPI_KEY, "country": "us"}},
           {"name": "GNews", "url": "https://gnews.io/api/v4/top-headlines", "params": {"apikey":GNEWS_KEY, "lang":"en"}},
           {"name": "Guardian", "url": "https://content.guardianapis.com/search", "params": {"api-key":GUARDIAN_KEY,"show-fields":"trailText"}}]

async def fetch_source(session,source):
    try:
        async with session.get(source["url"],params= source["params"]) as response:
                data = await response.json()
                return(data)
    except Exception as e:
        print(f"[{source['name']}] failed: {e}")
        return None 

async def run_cycle(): 
    async with aiohttp.ClientSession() as session:
        task = [fetch_source(session,s_dic) for s_dic in SOURCES]
        result= await asyncio.gather(*task)
        all_articles = []
        for src,res in zip(SOURCES,result):
            if res is None:        # ← new
                continue 
            all_articles.extend(parse_articles(src["name"], res))

        print(len(all_articles))
        display_articles(all_articles )
        save_to_json(all_articles)
        display_articles(filter_by_category(all_articles,"world cup"))
        # print(result)
        #print(result[0].keys())
        #print(result[1].keys())
        # print(result[2]["response"]["results"])
        # return result

def parse_articles(name,raw_json):
    articles=[]
    if name == "NewsAPI":
        raw_list = raw_json["articles"]
        for item in raw_list:
            articles.append({"title": item["title"], "source_api": name,
                             "url": item["url"], "published": item["publishedAt"]})
    elif name == "GNews":
        raw_list = raw_json["articles"]
        for item in raw_list:
            articles.append({"title": item["title"], "source_api": name,
                             "url": item["url"], "published": item["publishedAt"]})

    elif name == "Guardian":
        raw_list = raw_json["response"]["results"]
        for item in raw_list:
            articles.append({"title": item["webTitle"], "source_api": name,
                             "url": item["webUrl"], "published": item["webPublicationDate"]})

    return articles
 
def display_articles(articles):
    for i,art in enumerate(articles,start=1):
        print( f"{i}. [{ art['source_api']}] {art['title']}")


def save_to_json(articles):
    with open("news.json", "w", encoding="utf-8") as f:
        json.dump(articles, f, indent=2, ensure_ascii=False)


def filter_by_category(articles, keyword):
    result=[art for art in articles if keyword.lower() in art['title'].lower()]
    return result

async def main():                           # ← new, tiny
    while True:
        await run_cycle()
        print("Next refresh in 1 hour...")
        await asyncio.sleep(3600)

asyncio.run(main())