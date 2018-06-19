
# coding: utf-8

# In[48]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
right_now = datetime.datetime.now()
date_string = right_now.strftime("%Y-%M")


# In[36]:


response = requests.get("https://api.darksky.net/forecast/d2a29949964481ead00da5a5f5f9b0de/40.730610,-73.935242?units=si")
doc = BeautifulSoup(response.text, 'html.parser')


# In[8]:


doc


# In[13]:


data = response.json()
data


# In[38]:


#right_now_time = data["currently"]['time']
right_now_temp = data["currently"]['temperature']
today_summary = data["currently"]["summary"]

temp_feeling = data["daily"]["data"][0]["apparentTemperatureHigh"]
if temp_feeling > float(85):
    temp_feeling_word = "hot" 
elif temp_feeling < float(70):
    temp_feeling_word = "mild"
else:
    temp_feeling_word = "cold"

low_temp = data["daily"]["data"][0]["temperatureLow"]
rain_warning = data["daily"]["data"][0]["precipType"]
if rain_warning == "rain":
    rain_warning = "Bring your umbrella."


print("Right now it is", right_now_temp, "degrees and it is", today_summary +". Today will be", temp_feeling_word, 
      "with temperatures reaching", str(temp_feeling) + " degrees. Low temperature will be at", str(low_temp), 
      rain_warning)


# In[49]:


response =  requests.post(
        "https://api.mailgun.net/v3/sandboxbed486ceeeea4a4486e001e46204e37f.mailgun.org/messages",
        auth=("api", "8c24b1a94e84c41024bf44871236f499-0470a1f7-60fa2e91"),
        data={"from": "Excited User <mailgun@sandboxbed486ceeeea4a4486e001e46204e37f.mailgun.org>",
              "to": ["ht2494@columbia.edu"],
              "subject": "8AM Weather forecast" +right_now.strftime("%B-%d-%Y"),
              "text": "Testing some Mailgun awesomness!"})
response.text

