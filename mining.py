import urllib3
import telebot
import pandas as pd
import numpy as np
from datetime import datetime
import csv
from telebot import types
from datetime import timedelta
from poloniex import Poloniex
import krakenex
polo = Poloniex()
k = krakenex.API()
from bitfinex.client import Client
from bittrex import Bittrex
my_bittrex = Bittrex(None, None)
import urllib.parse
import helper
import time
import requests
from selenium import webdriver
import time
from pyvirtualdisplay import Display
from PIL import Image
from selenium.webdriver import Chrome
BOT_TOKEN = '409235131:AAEzihcaNnMsIyD1lWMnTEPrBA9aHQ7RnYA'
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message,):
 try:
  chat_id = message.chat.id
  print(message.text)
  if (data.applymap(lambda x: x == str(message.from_user.id)).any().any()==True):
   print ('yeah')
  else :
   print(message.from_user.id)
 except:
      print(1)
 try:
    with open('/home/weblanss/mysite/users1.txt','a') as f:
     f.write(str(message.from_user.id,))
     try:
      f.write(',@'+message.from_user.username+',')
     except:
        print(2)
 except:
     z=bot.send_message(chat_id, 'Добро пожаловать в крипто-мир , нажмите  команду /menu ,чтоыбы перейти в главное меню ')
     menu(z)


@bot.message_handler(commands=['menu'])
def menu(message,):
    chat_id = message.chat.id

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add('??Рассчитать хешрейт')

    markup.add('?? Биржи', '?? Профиль')
    markup.add('?? Пулы:', ' ??Поддержка')
    mess='Тщательно изучая рынок криптовалют ,  наш бот способен стать проводником в мир больших возможностей '
    bot.send_message(chat_id, mess, reply_markup = markup)

@bot.message_handler(func = lambda message: '??Рассчитать хешрейт'in message.text)
def hash(message,):
     chat_id = message.chat.id
     mes='?? GPU алгоритмы:\n /Ethash /CryptoNight /Equihash /X11Gost /LBRY /Groestl/n /Lyra2REv2 /NeoScrypt /Decred /SiaCoin /Pascal/Skunkhash\n ?? ASIC алгоритмы:\n /Sha256 /Scrypt /X11 /Qubit /Quark\n ?? DUAL ETH | ETC | EXP\n/DCR /SIA /LBC /PASC /PASL /\n ?? AMD:/\n /HD7870 /HD7950 /280x /290x /380 /390 /460 /470 /480 /550 /570/n /580 /Fur/\n ?? Nvidi:/n /750Ti /960 /970 /980 /980Ti /1050 /1050Ti /1060 /1070 /1080 /1080Ti/n'
     bot.send_message(chat_id, mes)

@bot.message_handler(func = lambda message: '??Поддержка'in message.text)
def support(message,):
     chat_id = message.chat.id
     sp='Нашли баг или ошибку?\n Хотите предложить свою идею?\nЗнаете,что мы должны добавить?\n ?? Напишите @CryptoMininghelpbot'
     z=bot.send_message(chat_id,sp )

@bot.message_handler(func = lambda message: '?? Профиль'in message.text)
def prof(message,):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add('??Хешрейт')

    markup.add('?? Потребление', '??Биржы')
    markup.add('??Стоимость кв/ч:', ' ??Потребление')
    sp='?? Сохраните ваши данные в боте, чтобы начать.\n\n ?? Настройки:\n\nБиржа для расчётов: Poloniex.com'
    z=bot.send_message(chat_id,sp, reply_markup = markup )


def ecran (url,size,adr):
        display = Display(visible=0, size=(800, 600))
        display.start()

        browser = webdriver.PhantomJS()
        print(4)
        browser.implicitly_wait(15)


        browser.get(url)
        browser.implicitly_wait(15)
        try:
            browser.find_element_by_xpath("//a[contains(@class,'closeModal')]").click()
        except Exception as e:
            print(e)

        print(3)
        browser.save_screenshot(adr)

        browser.quit()
        img = Image.open(adr)
        crop_rectangle = size
        cropped_img = img.crop(crop_rectangle)

        cropped_img.save(adr)
        display.stop()


@bot.message_handler(func = lambda message: '/Ethash'in message.text)
def etra(message,):

        z=bot.send_message(message.chat.id,'Введите ?? Хешрейт Ethash (Mh/s): ' )


        bot.register_next_step_handler(z, send_hash)

@bot.message_handler(func = lambda message: '/CryptoNight'in message.text)
def  CryptoNight(message,):

        z=bot.send_message(message.chat.id,'Введите ?? Хешрейт CryptoNight (Mh/s): ' )


        bot.register_next_step_handler(z,  CryptoNight)
def CryptoNight(m):
    #try:
        #z=int(m.text())

        url='https://www.coinwarz.com/cryptocurrency/?sha256hr=9460.00&sha256p=2600.00&sha256pc=0.1000&sha256c=false&scrypthr=110000.00&scryptp=1000.00&scryptpc=0.1000&scryptc=false&x11hr=450.00&x11p=120.00&x11pc=0.1000&x11c=false&quarkhr=450000.00&quarkp=75.00&quarkpc=0.1000&quarkc=false&groestlhr=45.00&groestlp=825.00&groestlpc=0.1000&groestlc=false&blake256hr=11.20&blake256p=600.00&blake256pc=0.1000&blake256c=false&neoscrypthr=400.00&neoscryptp=400.00&neoscryptpc=0.1000&neoscryptc=false&lyra2rev2hr=30.00&lyra2rev2p=600.00&lyra2rev2pc=0.1000&lyra2rev2c=false&cryptonighthr= '+str(m.text)+'&cryptonightp=600.00&cryptonightpc=0.1000&cryptonightc=true&ethashhr=250.00&ethashp=600.00&ethashpc=0.1000&ethashc=false&equihashhr=23234.00&equihashp=600.00&equihashpc=0.1000&equihashc=false&e=CEX.io'


        adr='c:\\1\\1.png'
        size=(10 ,1060, 1150, 1645 )
        ecran(url,size,adr)
        w2=open(adr,'rb')
        bot.send_photo(m.chat.id,w2)



def send_hash(m):
    #try:
        #z=int(m.text())

        url='http://whattomine.com/coins?utf8=%E2%9C%93&adapt_q_280x='+str(m.text)+'&adapt_q_380=0&adapt_q_fury=0&adapt_q_470=0&adapt_q_480=3&adapt_q_570=0&adapt_q_580=0&adapt_q_750Ti=0&adapt_q_10606=0&adapt_q_1070=0&adapt_q_1080=0&adapt_q_1080Ti=0&eth=true&factor%5Beth_hr%5D=0.0&factor%5Beth_p%5D=0.0&factor%5Bgro_hr%5D=0.0&factor%5Bgro_p%5D=0.0&factor%5Bx11g_hr%5D=0.0&factor%5Bx11g_p%5D=0.0&factor%5Bcn_hr%5D=0.0&factor%5Bcn_p%5D=0.0&factor%5Beq_hr%5D=0.0&factor%5Beq_p%5D=0.0&factor%5Blrev2_hr%5D=0.0&factor%5Blrev2_p%5D=0.0&factor%5Bns_hr%5D=0.0&factor%5Bns_p%5D=0.0&factor%5Blbry_hr%5D=0.0&factor%5Blbry_p%5D=0.0&factor%5Bbk2b_hr%5D=0.0&factor%5Bbk2b_p%5D=0.0&factor%5Bbk14_hr%5D=0.0&factor%5Bbk14_p%5D=0.0&factor%5Bpas_hr%5D=0.0&factor%5Bpas_p%5D=0.0&factor%5Bskh_hr%5D=0.0&factor%5Bskh_p%5D=0.0&factor%5Bl2z_hr%5D=420.0&factor%5Bl2z_p%5D=300.0&factor%5Bcost%5D=0.1&sort=Profitability24&volume=0&revenue=24h&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=bleutrade&factor%5Bexchanges%5D%5B%5D=bter&factor%5Bexchanges%5D%5B%5D=c_cex&factor%5Bexchanges%5D%5B%5D=cryptopia&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=yobit&dataset=Main&commit=Calculate'


        adr='c:\\1\\etash1.png'
        size=(10 ,1060, 1150, 1645 )
        ecran(url,size,adr)
        w2=open(adr,'rb')
        bot.send_photo(m.chat.id,w2)

    #except  Exception as e:
         #print(e)
         #bot.send_message(m.chat.id,'Неверный формат ' )

@bot.message_handler(func = lambda message: '?? Биржи'in message.text)
def stocks(message,):

    kb = types.InlineKeyboardMarkup()
    kb.add(*[types.InlineKeyboardButton(text=name,callback_data=name)for name in ['Poloniex','Kraken']])
    kb.add(*[types.InlineKeyboardButton(text=name,callback_data=name)for name in ['Bitfinex','Bittrex']])

    kb.add(*[types.InlineKeyboardButton(text=name,callback_data=name)for name in ['Yobit','Exmo']])
    mes='Выберите биржу'
    bot.send_message(message.chat.id, mes, reply_markup=kb)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline1(call):
    if call.data == "Poloniex":
       x=(polo('returnTicker')['BTC_ETH']['highestBid'])
       y=(polo('returnTicker')['USDT_REP']['highestBid'])
       z=(polo('returnTicker')['BTC_DOGE']['highestBid'])
       x1=(polo('returnTicker')['BTC_XBC']['highestBid'])
       y2=(polo('returnTicker')['ETH_ETC']['highestBid'])
       z2=(polo('returnTicker')['BTC_MAID']['highestBid'])

       mes='<b>BTC_ETH</b>: '+str(x)+'\n<b>USDT_REP</b>: '+str(y)+'<b>\nBTC_DOGE</b>: '+str(z)+'<b>\nBTC_XBC</b>: '+str(x1)+'<b>\nETH_ETC</b>: '+str(y2)+'<b>\nBTC_MAID</b>: '+str(z2)
       z=bot.send_message(call.message.chat.id, mes,parse_mode='HTML')
    if call.data == "Kraken":

       url='https://api.kraken.com/0/public/Ticker?pair='
       XXBTZUSD=url+'XXBTZUSD'
       r = requests.get(XXBTZUSD)
       x=r.json()
       h=[]
       for i in x['result']['XXBTZUSD'].keys():
            h.append(x['result']['XXBTZUSD'][i])
       z=[]
       for i in range(0,len(h)):
        try:
            w='\n'.join(h[i])
            z.append(w)

        except:
            print(1)
       w='\n'.join(z)
       mes='<b>XXBTZUSD</b>: '+str(w)
       z=bot.send_message(call.message.chat.id, mes,parse_mode='HTML')



    if call.data == "Bitfinex":
        client = Client()
        symbols = client.symbols()
        btcusd=client.ticker(symbols[0])
        ltcusd=client.ticker(symbols[1])
        ltcbtc=client.ticker(symbols[2])
        ethusd=client.ticker(symbols[3])
        ethbtc=client.ticker(symbols[4])
        etcbtc=client.ticker(symbols[5])
        etcusd=client.ticker(symbols[6])
        rrtusd=client.ticker(symbols[7])

        mes='<b>btc_usd</b>: '+str(btcusd['last_price'])+'\n<b>ltc_usd</b>: '+str(ltcusd['last_price'])+'<b>\nltc_btc</b>: '+str(ltcbtc['last_price'])+'<b>\neth_usd</b>: '+str(ethusd['last_price'])+'<b>\neth_btc</b>: '+str(ethbtc['last_price'])+'<b>\netc_btc</b>: '+str(etcbtc['last_price'])+'<b>\netc_btc</b>: '+str(etcusd['last_price'])+'<b>\nrrt_usd=</b>: '+str(rrtusd['last_price'])
        z=bot.send_message(call.message.chat.id, mes,parse_mode='HTML')
    if call.data == "Bittrex":
        url='https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-ltc'
        z=[]
        r = requests.get(url)
        x=r.json()
        for i in x['result'][0]:
            e=x['result'][0][i]
            k=str(i)+' : '+str(e)
            z.append(k)
        w='\n'.join(z)
        mes='<b>btc-ltc</b>: '+str(w)
        z=bot.send_message(call.message.chat.id, mes,parse_mode='HTML')

    if call.data == "Yobit":
        url='https://yobit.net/api/2/ltc_btc/ticker'

        feed = requests.get(url)
        x=feed.json()
        z=[]
        for i in x['ticker']:
            e=x['ticker'][i]
            k=str(i)+' : '+str(e)
            z.append(k)
        w='\n'.join(z)
        mes='<b>ltc_btc</b>: '+str(w)
        z=bot.send_message(call.message.chat.id, mes,parse_mode='HTML')


while True:
    #try:
        bot.polling(none_stop=True)



