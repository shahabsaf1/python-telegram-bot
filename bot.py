# -*- coding: utf-8 -*-
from utils import *

TOKEN = 'your token'


bot = telebot.TeleBot("TOKEN")


#https://github.com/SEEDTEAM/jack-telegram-bot/blob/master/plugins/linkshortener.moon :D
@bot.message_handler(commands=['bitly'])
def bitly(m):
    text = m.text.split(' ')[1]
    url = 'https://api-ssl.bitly.com/v3/shorten'
    params = {
        'access_token': 'f94d249d269f5ae4af107d9fdfddd36a6a88327e',
        'longUrl': text,
    }  
    jstr = requests.get(url, params=params, headers=None, files=None, data=None)       
    data = json.loads(jstr.text)
    cid = m.chat.id
    tex = data['data']['url']
    bot.send_message(cid, tex)

#https://github.com/SEEDTEAM/jack-telegram-bot/blob/master/plugins/lmgtfy.moon :D
@bot.message_handler(commands=['lmgtfy'])
def lmg(m):
    text = m.text.split(' ')[1]
    url = 'http://lmgtfy.com/?q=' + text
    cid = m.chat.id
    bot.send_chat_action(cid, 'typing')
    bot.send_message(cid, url)       

#https://github.com/SEEDTEAM/jack-telegram-bot/blob/master/plugins/ipinfo.moon :D
@bot.message_handler(commands=['ip','check'])
def ip(m):
    text = m.text.split(' ')[1]
    url = 'http://api.ipinfodb.com/v3/ip-city/'
    params = {
        'key': 'bd36e5c11b78ac040a0858df1df61b3ac9fe6d1717bfe073690617557dd9dc42',
        'ip': text,
        'format': 'json',
    }  
    jstr = requests.get(url, params=params, headers=None, files=None, data=None)       
    data = json.loads(jstr.text)
    cid = m.chat.id
 
    bot.send_chat_action(cid, 'find_location')
    lat = data['latitude']
    lag = data['longitude']
    text = '*Ip Address:* ' + data['ipAddress'] + '\n*Country:* ' + data['countryName'] + '\n*City Name:* ' + data['cityName'] + '\n*Zip Code:* ' + data['zipCode'] + '\n*Region Name:* ' + data['regionName']
    bot.send_location(cid,lat,lag)
    bot.send_message(cid,text,parse_mode="Markdown")       

#https://github.com/SEEDTEAM/jack-telegram-bot/blob/master/plugins/cat.moon :D
@bot.message_handler(commands=['cat'])
def cats(m):
    url = 'http://thecatapi.com/api/images/get?format=src&type=jpg'
    cid = m.chat.id
    file = download(url)
    bot.send_photo(cid,file) 

#https://github.com/SEEDTEAM/jack-telegram-bot/blob/master/plugins/qrcode.moon :D
@bot.message_handler(commands=['qr'])
def qr(m):
    text = m.text.split(' ')[1]
    url = 'https://api.qrserver.com/v1/create-qr-code/?size=500x500&data=' + text
    cid = m.chat.id
    file = download(url)
    bot.send_photo(cid,file)  

#https://github.com/luksireiku/polaris/blob/master/plugins/search.py :D :|
@bot.message_handler(commands=['g','google'])
def google(m):
    text = m.text.split(' ')[1]
    url = 'http://ajax.googleapis.com/ajax/services/search/web'
    params = {
        'v': '1.0',
        'rsz': 6,
        'q': text,
    }
    jstr = requests.get(url, params=params, headers=None, files=None, data=None)       
    data = json.loads(jstr.text)
    cid = m.chat.id
    text = '' 
    for i in range(0, len(data['responseData']['results'])):
        result_url = data['responseData']['results'][i]['unescapedUrl']
        result_title = data['responseData']['results'][i]['titleNoFormatting']
        text += '~> [' + result_title + '](' + result_url + ')\n\n'
    bot.send_message(cid,text,parse_mode="Markdown")
 
#https://github.com/SEEDTEAM/jack-telegram-bot/blob/master/plugins/talk.moon :D
@bot.message_handler(commands=['tts', 'voice'])
def tts(m):
    text = m.text.split(' ')[1]
    url = 'http://tts.baidu.com/text2audio'
    params = {'lan': 'en','ie': 'UTF-8','text': text,}
    cid = m.chat.id
    file = download(url,params=params)
    bot.send_voice(cid,file)

#https://github.com/SEEDTEAM/jack-telegram-bot/blob/master/plugins/urbandictionary.moon :D
@bot.message_handler(commands=['ud','dic'])
def ud(m):
    text = m.text.split(' ')[1]
    cid = m.chat.id
    url = 'http://api.urbandictionary.com/v0/define'
    params = {'term': text}  
    jstr = requests.get(url, params=params, headers=None, files=None, data=None)       
    data = json.loads(jstr.text)
    if data['result_type'] == 'no_results':
       bot.send_message(cid,'_Nothing Found_',parse_mode="Markdown") 
    else:
       definition = data['list'][1]['definition']
       definition = definition.replace('^%s*(.-)%s*$', '%1')
       example = data['list'][1]['example'].replace('^%s*(.-)%s*$', '%1')
       text = data['list'][1]['word'] + '\n' + definition + '\n\n*Example:*\n' + example
       bot.send_message(cid,text,parse_mode="Markdown") 

#https://github.com/SEEDTEAM/jack-telegram-bot/blob/master/plugins/webshot.moon ;D
@bot.message_handler(commands=['webshot'])
def shot(m):
    text = m.text.split(' ')[1]
    url = 'http://api.screenshotmachine.com/?key=b645b8&size=X&url=' + text + '&format=png'
    file = download(url)
    bot.send_photo(m.chat.id,file) 

bot.polling(none_stop=True)

#Amir
