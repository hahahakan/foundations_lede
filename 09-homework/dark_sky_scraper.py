
# coding: utf-8

# In[12]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
right_now = datetime.datetime.now()
date_string = right_now.strftime("%Y-%M")


# In[13]:


response = requests.get("https://api.darksky.net/forecast/XXXXXX/40.730610,-73.935242?units=si")


# In[14]:


data = response.json()
data


# In[17]:


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

mail_text = "Right now it is", right_now_temp, "degrees and it is", today_summary +". Today will be", temp_feeling_word, "with temperatures reaching", str(temp_feeling) + " degrees. Low temperature will be at", str(low_temp), rain_warning


# In[16]:


response =  requests.post(
        "https://api.mailgun.net/v3/XXXXXXXX.mailgun.org/messages",
        auth=("api", "XXXXXXXXX"),
        data={"from": "Excited User <mailgun@XXXXXXXXXXXXXXX.mailgun.org>",
              "to": ["XXXXXXXXXX"],
              "subject": "8AM Weather forecast" +right_now.strftime("%B-%d-%Y"),
              "text": mail_text})
response.text

