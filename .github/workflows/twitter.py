import tweepy
import requests
from bs4 import BeautifulSoup

bearer_token = 'AAAAAAAAAAAAAAAAAAAAABVZmQEAAAAAatqB%2FkOx%2Bp5mn5pv2mh324CqxBs%3DaqjmGOBVmM0CVKAs9IyjUAjEm3gNk5WAg77cx8iH7Os3kfiMO4'
consumer_key = 'pwyZBxzrCn2xkhWV6kYnN5orF'
consumer_secret = 'IPZXeOXw3AmgJDZYVuFpIEh6Rzo3p0CLPgNUew555gVymhLuYt'
access_token = '1528686812130066433-w66qdkFxA8Px2gmXluF5yVQWnSFQ8I'
access_secret = 'ijv2RpvAFzr0a4GK9DmRaRyld6kK4m8Ez7UxFZVOnaUzF'

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
