
# coding: utf-8

# In[117]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd

import requests
import datetime
right_now = datetime.datetime.now()
date_string = right_now.strftime("%Y-%M")


# In[82]:


driver = webdriver.Chrome()
url = "https://old.reddit.com"
driver.get(url)


# In[ ]:


#time.sleep(2)
#skip_button = driver.find_element_by_class_name("skip-for-now")
#driver.execute_script("arguments[0].scrollIntoView(true)", skip_button)
#skip_button.click()

#skip_button = driver.find_elements_by_tag_name('a')
#for skip in skip_button:
#    print(skip.text)
skip_button = driver.find_elements_by_tag_name('a')[2].click
skip_button()


# In[109]:


each_post = driver.find_elements_by_class_name("thing")

posts = []

for post in each_post[1:]: 
    post_info = {}
    
    title = post.find_element_by_class_name("title").text
    post_info["title"] = title

    author = post.find_element_by_class_name("author").text
    post_info['author'] = author
    
    link = post.find_element_by_tag_name('a').get_attribute('href')
    post_info['url'] = link
    
    score = post.find_elements_by_tag_name('div')[0].text
    post_info['score'] = score
    
    subreddit = post.find_element_by_class_name('subreddit').text
    post_info['subreddit'] = subreddit.replace("r/", "")
    
    comments = post.find_element_by_class_name('comments').text
    post_info['comments'] = comments
    
    posts.append(post_info)


posts


# In[110]:


df = pd.DataFrame(posts)
df.head()


# In[111]:


df.to_csv("reddit_frontpage.csv", index=False)


# In[133]:


filename = "reddit_briefing" + right_now.strftime("%Y-%m-%d_%H_%M_%S") + ".csv"
df.to_csv(filename, index=False)


# In[134]:


response =  requests.post(
        "https://api.mailgun.net/v3/XXXXX.mailgun.org/messages",
        auth=("api", "XXXXXXX"),
        files=[("attachment", open(filename))],
        data={"from": "Excited User <mailgun@XXXXXXXX.mailgun.org>",
              "to": ["XXXXXX@XXXXXX.XXXXXX"],
              "subject": "Here is your 6PM briefing" +right_now.strftime("%B-%d-%Y"),
              "text": "Testing some Mailgun awesomness!"})
response.text

