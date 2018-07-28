#!/usr/bin/env python
import tweepy

#Coloca dentro de las comillas tus claves...
CONSUMER_KEY = 'xiHlth8bVMiFmxGt741g' 
CONSUMER_SECRET = 'pnSyIx7awxtB3BRCArdfZ5neebAAokzhmPQgzerqlU'
ACCESS_KEY = '90926098-Wk4hKn2VnpbbpIKTeJeVCpa2KA45pXTyUGILJYUPp'
ACCESS_SECRET = 'C64SHvQUPaCalYgTc6kwOeGcHtUtWgLXHmRXYOCkhPqo3'

#En esta parte nos identifica para poder realizar operaciones
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

#update_status('mensaje' o variable) es para actualizar nuestro estado
x = tweepy.API(auth)

for tweets in x.search(q='gdloacev',count=4, result_type='recent'):
    print(tweets.created_at)
    print(tweets.user.screen_name)
    print(tweets.text)
    print(' *'*40)