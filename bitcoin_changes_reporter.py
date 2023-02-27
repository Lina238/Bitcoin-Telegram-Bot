import requests
import time
#add your api key here that you got from pro.coinmarketcap.com 
api_key='put your api_key here'
#add your bot key here that you got  from https://t.me/BotFather (telegram) 
bot_key='put your bot_key here'
#add your chat id here that you got from https://t.me/myidbot (telegram)
chat_id='put your chat_id here'
actuel=56000 #the actuel value 
update=5*60#do a request every five minutes
##function to get the new price (new value)
# from documentation : https://coinmarketcap.com/api/documentation/v1/#section/Quick-Start-Guide
def get_new_value():
  url='https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
  parameters = {
  'start':'1', #bitcoin is the first one
  'limit':'2',  # ====>you can get all the currency
  'convert':'USD'
   }
  headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': api_key,
 }
  #sent a request to the url 
  res=requests.get(url,headers=headers,params=parameters).json()
  btc=res['data'][0]['quote']['USD']['price']
  
  return btc
def send_new_value(msg):
  #from documentation: https://core.telegram.org/bots/api  
  #https://api.telegram.org/bot<token>/METHOD_NAME
  url=f'https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={chat_id}&text={msg}'
  requests.get(url)
def mainprogram():
 while True:
    price=get_new_value()#get bitcoin price
    if price<actuel:
        send_new_value(f"The Bitcoin price have been reduced to : {price} ")
    time.sleep(update)    #update the date every 5min
mainprogram()    
        