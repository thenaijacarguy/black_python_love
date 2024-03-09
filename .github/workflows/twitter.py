import os
import tweepy
import requests
from bs4 import BeautifulSoup

bearer_token = os.environ.get('BEARER_TOKEN')
consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_secret = os.environ.get('ACCESS_SECRET')

client = tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_secret,
                      access_token=access_token, access_token_secret=access_secret)

article_url = 'https://www.theverge.com/tech'

response = requests.get(article_url)

soup = BeautifulSoup(response.text, 'html.parser')

article = soup.find('a', class_='after:absolute')
title = article.find_next('a').text

body = soup.find_all('p')[1].text

link = article.find_next('a')['href']

tweet = '#DailyTechNews: ' + title + ' - ' + body[:150] + '...Read More Here 👇🏼 https://theverge.com' + link

client.create_tweet(text=tweet)
