
# coding: utf-8

# In[14]:


import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

import datetime
right_now = datetime.datetime.now()
date_string = right_now.strftime("%Y-%M")


# In[2]:


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
raw_html = requests.get("http://old.reddit.com", headers=headers).content
#raw_html = (requests.get("http://old.reddit.com").content


# In[3]:


reddit = BeautifulSoup(raw_html, "html.parser")


# In[4]:


print(reddit.prettify())


# In[5]:


articles = reddit.find_all(class_="thing")
articles[0]


# In[19]:


articles = reddit.find_all(class_="thing")

post_info = []

for article in articles:
    post_dict = {}

    post_dict['title'] = article.find(class_="title").text
    post_dict['author'] = article.find(class_="author").string
    try:
        post_dict['score'] = article.find(class_="score unvoted")['title']
    except:
        pass
    post_dict['subreddit'] = article.find(class_="subreddit").string
    post_dict['comments'] = article.find(class_='first').string
    post_dict['link'] = article.find("a")['href']

    post_info.append(post_dict)

reddit_posts = post_info
reddit_posts


# In[11]:


df = pd.DataFrame(reddit_posts)
df.head()


# In[16]:


filename = "reddit_briefing" + right_now.strftime("%Y-%m-%d_%H_%M_%S") + ".csv"
df.to_csv(filename, index=False)


# In[17]:


response =  requests.post(
        "https://api.mailgun.net/v3/XXXXXXXXXXX.mailgun.org/messages",
        auth=("api", "XXXXX"),
        files=[("attachment", open(filename))],
        data={"from": "Excited User <mailgun@XXXXX.mailgun.org>",
              "to": ["XXX"],
              "subject": "Here is your 6PM briefing" +right_now.strftime("%B-%d-%Y"),
              "text": reddit_posts})
response.text

