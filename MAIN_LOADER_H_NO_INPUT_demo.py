import fxcmpy
import pandas as pd
import datetime as dt
tonoumero = 4001
TOKEN="2be81885764d91b442c47502cf588f43bcb25081"
df=fxcmpy.fxcmpy(access_token=TOKEN,log_level='error',server='demo')
x = df.get_candles('EUR/USD', period='H1', number=tonoumero)

#print(df())
x.to_csv(r'C:/xampp/htdocs/nasiasense/hist/h/eurusdH_raw.csv')
#fxcmpy.to_csv(r'C:\Users\atsal\GGGGG.csv')
print(x.tail())

df=fxcmpy.fxcmpy(access_token=TOKEN,log_level='error',server='demo')
x = df.get_candles('GBP/USD', period='H1', number=tonoumero)

#print(df())
x.to_csv(r'C:/xampp/htdocs/nasiasense/hist/h/gbpusdH_raw.csv')
#fxcmpy.to_csv(r'C:\Users\atsal\GGGGG.csv')
print(x.tail())

df=fxcmpy.fxcmpy(access_token=TOKEN,log_level='error',server='demo')
x = df.get_candles('USD/CHF', period='H1', number=tonoumero)

#print(df())
x.to_csv(r'C:/xampp/htdocs/nasiasense/hist/h/usdchfH_raw.csv')
#fxcmpy.to_csv(r'C:\Users\atsal\GGGGG.csv')
print(x.tail())

df=fxcmpy.fxcmpy(access_token=TOKEN,log_level='error',server='demo')
x = df.get_candles('USD/JPY', period='H1', number=tonoumero)

#print(df())
x.to_csv(r'C:/xampp/htdocs/nasiasense/hist/h/usdjpyH_raw.csv')
#fxcmpy.to_csv(r'C:\Users\atsal\GGGGG.csv')
print(x.tail())

df=fxcmpy.fxcmpy(access_token=TOKEN,log_level='error',server='demo')
x = df.get_candles('GBP/JPY', period='H1', number=tonoumero)

#print(df())
x.to_csv(r'C:/xampp/htdocs/nasiasense/hist/h/gbpjpyH_raw.csv')
#fxcmpy.to_csv(r'C:\Users\atsal\GGGGG.csv')
print(x.tail())

df=fxcmpy.fxcmpy(access_token=TOKEN,log_level='error',server='demo')
x = df.get_candles('EUR/CHF', period='H1', number=tonoumero)

#print(df())
x.to_csv(r'C:/xampp/htdocs/nasiasense/hist/h/eurchfH_raw.csv')
#fxcmpy.to_csv(r'C:\Users\atsal\GGGGG.csv')
print(x.tail())

df=fxcmpy.fxcmpy(access_token=TOKEN,log_level='error',server='demo')
x = df.get_candles('CHF/JPY', period='H1', number=tonoumero)

#print(df())
x.to_csv(r'C:/xampp/htdocs/nasiasense/hist/h/chfjpyH_raw.csv')
#fxcmpy.to_csv(r'C:\Users\atsal\GGGGG.csv')
print(x.tail())

df=fxcmpy.fxcmpy(access_token=TOKEN,log_level='error',server='demo')
x = df.get_candles('EUR/JPY', period='H1', number=tonoumero)

#print(df())
x.to_csv(r'C:/xampp/htdocs/nasiasense/hist/h/eurjpyH_raw.csv')
#fxcmpy.to_csv(r'C:\Users\atsal\GGGGG.csv')
print(x.tail())

df=fxcmpy.fxcmpy(access_token=TOKEN,log_level='error',server='demo')
x = df.get_candles('EUR/GBP', period='H1', number=tonoumero)

#print(df())
x.to_csv(r'C:/xampp/htdocs/nasiasense/hist/h/eurgbpH_raw.csv')
#fxcmpy.to_csv(r'C:\Users\atsal\GGGGG.csv')
print(x.tail())

df=fxcmpy.fxcmpy(access_token=TOKEN,log_level='error',server='demo')
x = df.get_candles('EUR/CAD', period='H1', number=tonoumero)

#print(df())
x.to_csv(r'C:/xampp/htdocs/nasiasense/hist/h/eurcadH_raw.csv')
#fxcmpy.to_csv(r'C:\Users\atsal\GGGGG.csv')
print(x.tail())


df=fxcmpy.fxcmpy(access_token=TOKEN,log_level='error',server='demo')
x = df.get_candles('AUD/USD', period='H1', number=tonoumero)

#print(df())
x.to_csv(r'C:/xampp/htdocs/nasiasense/hist/h/audusdH_raw.csv')
#fxcmpy.to_csv(r'C:\Users\atsal\GGGGG.csv')
print(x.tail())

df=fxcmpy.fxcmpy(access_token=TOKEN,log_level='error',server='demo')
x = df.get_candles('AUD/CHF', period='H1', number=tonoumero)

#print(df())
x.to_csv(r'C:/xampp/htdocs/nasiasense/hist/h/audchfH_raw.csv')
#fxcmpy.to_csv(r'C:\Users\atsal\GGGGG.csv')
print(x.tail())

df=fxcmpy.fxcmpy(access_token=TOKEN,log_level='error',server='demo')
x = df.get_candles('NZD/CHF', period='H1', number=tonoumero)

#print(df())
x.to_csv(r'C:/xampp/htdocs/nasiasense/hist/h/nzdchfH_raw.csv')
#fxcmpy.to_csv(r'C:\Users\atsal\GGGGG.csv')
print(x.tail())

df=fxcmpy.fxcmpy(access_token=TOKEN,log_level='error',server='demo')
x = df.get_candles('NZD/JPY', period='H1', number=tonoumero)

#print(df())
x.to_csv(r'C:/xampp/htdocs/nasiasense/hist/h/nzdjpyH_raw.csv')
#fxcmpy.to_csv(r'C:\Users\atsal\GGGGG.csv')
print(x.tail())


df=fxcmpy.fxcmpy(access_token=TOKEN,log_level='error',server='demo')
x = df.get_candles('XAU/USD', period='H1', number=tonoumero)

#print(df())
x.to_csv(r'C:/xampp/htdocs/nasiasense/hist/h/xauusdH_raw.csv')
#fxcmpy.to_csv(r'C:\Users\atsal\GGGGG.csv')
print(x.tail())


df=fxcmpy.fxcmpy(access_token=TOKEN,log_level='error',server='demo')
x = df.get_candles('XAG/USD', period='H1', number=tonoumero)

#print(df())
x.to_csv(r'C:/xampp/htdocs/nasiasense/hist/h/xagusdH_raw.csv')
#fxcmpy.to_csv(r'C:\Users\atsal\GGGGG.csv')
print(x.tail())


df=fxcmpy.fxcmpy(access_token=TOKEN,log_level='error',server='demo')
x = df.get_candles('USD/CAD', period='H1', number=tonoumero)

#print(df())
x.to_csv(r'C:/xampp/htdocs/nasiasense/hist/h/usdcadH_raw.csv')
#fxcmpy.to_csv(r'C:\Users\atsal\GGGGG.csv')
print(x.tail())


df=fxcmpy.fxcmpy(access_token=TOKEN,log_level='error',server='demo')
x = df.get_candles('AUD/CAD', period='H1', number=tonoumero)

#print(df())
x.to_csv(r'C:/xampp/htdocs/nasiasense/hist/h/audcadH_raw.csv')
#fxcmpy.to_csv(r'C:\Users\atsal\GGGGG.csv')
print(x.tail())



df=fxcmpy.fxcmpy(access_token=TOKEN,log_level='error',server='demo')
x = df.get_candles('AUD/JPY', period='H1', number=tonoumero)

#print(df())
x.to_csv(r'C:/xampp/htdocs/nasiasense/hist/h/audjpyH_raw.csv')
#fxcmpy.to_csv(r'C:\Users\atsal\GGGGG.csv')
print(x.tail())


df=fxcmpy.fxcmpy(access_token=TOKEN,log_level='error',server='demo')
x = df.get_candles('AUD/NZD', period='H1', number=tonoumero)

#print(df())
x.to_csv(r'C:/xampp/htdocs/nasiasense/hist/h/audnzdH_raw.csv')
#fxcmpy.to_csv(r'C:\Users\atsal\GGGGG.csv')
print(x.tail())



df=fxcmpy.fxcmpy(access_token=TOKEN,log_level='error',server='demo')
x = df.get_candles('CAD/CHF', period='H1', number=tonoumero)

#print(df())
x.to_csv(r'C:/xampp/htdocs/nasiasense/hist/h/cadchfH_raw.csv')
#fxcmpy.to_csv(r'C:\Users\atsal\GGGGG.csv')
print(x.tail())



df=fxcmpy.fxcmpy(access_token=TOKEN,log_level='error',server='demo')
x = df.get_candles('CAD/JPY', period='H1', number=tonoumero)

#print(df())
x.to_csv(r'C:/xampp/htdocs/nasiasense/hist/h/cadjpyH_raw.csv')
#fxcmpy.to_csv(r'C:\Users\atsal\GGGGG.csv')
print(x.tail())


df=fxcmpy.fxcmpy(access_token=TOKEN,log_level='error',server='demo')
x = df.get_candles('EUR/AUD', period='H1', number=tonoumero)

#print(df())
x.to_csv(r'C:/xampp/htdocs/nasiasense/hist/h/euraudH_raw.csv')
#fxcmpy.to_csv(r'C:\Users\atsal\GGGGG.csv')
print(x.tail())


df=fxcmpy.fxcmpy(access_token=TOKEN,log_level='error',server='demo')
x = df.get_candles('EUR/NZD', period='H1', number=tonoumero)

#print(df())
x.to_csv(r'C:/xampp/htdocs/nasiasense/hist/h/eurnzdH_raw.csv')
#fxcmpy.to_csv(r'C:\Users\atsal\GGGGG.csv')
print(x.tail())



df=fxcmpy.fxcmpy(access_token=TOKEN,log_level='error',server='demo')
x = df.get_candles('GBP/AUD', period='H1', number=tonoumero)

#print(df())
x.to_csv(r'C:/xampp/htdocs/nasiasense/hist/h/gbpaudH_raw.csv')
#fxcmpy.to_csv(r'C:\Users\atsal\GGGGG.csv')
print(x.tail())



df=fxcmpy.fxcmpy(access_token=TOKEN,log_level='error',server='demo')
x = df.get_candles('GBP/CAD', period='H1', number=tonoumero)

#print(df())
x.to_csv(r'C:/xampp/htdocs/nasiasense/hist/h/gbpcadH_raw.csv')
#fxcmpy.to_csv(r'C:\Users\atsal\GGGGG.csv')
print(x.tail())



df=fxcmpy.fxcmpy(access_token=TOKEN,log_level='error',server='demo')
x = df.get_candles('GBP/CHF', period='H1', number=tonoumero)

#print(df())
x.to_csv(r'C:/xampp/htdocs/nasiasense/hist/h/gbpchfH_raw.csv')
#fxcmpy.to_csv(r'C:\Users\atsal\GGGGG.csv')
print(x.tail())



df=fxcmpy.fxcmpy(access_token=TOKEN,log_level='error',server='demo')
x = df.get_candles('GBP/NZD', period='H1', number=tonoumero)

#print(df())
x.to_csv(r'C:/xampp/htdocs/nasiasense/hist/h/gbpnzdH_raw.csv')
#fxcmpy.to_csv(r'C:\Users\atsal\GGGGG.csv')
print(x.tail())



df=fxcmpy.fxcmpy(access_token=TOKEN,log_level='error',server='demo')
x = df.get_candles('NZD/CAD', period='H1', number=tonoumero)

#print(df())
x.to_csv(r'C:/xampp/htdocs/nasiasense/hist/h/nzdcadH_raw.csv')
#fxcmpy.to_csv(r'C:\Users\atsal\GGGGG.csv')
print(x.tail())



df=fxcmpy.fxcmpy(access_token=TOKEN,log_level='error',server='demo')
x = df.get_candles('NZD/CHF', period='H1', number=tonoumero)

#print(df())
x.to_csv(r'C:/xampp/htdocs/nasiasense/hist/h/nzdchfH_raw.csv')
#fxcmpy.to_csv(r'C:\Users\atsal\GGGGG.csv')
print(x.tail())


df=fxcmpy.fxcmpy(access_token=TOKEN,log_level='error',server='demo')
x = df.get_candles('NZD/USD', period='H1', number=tonoumero)

#print(df())
x.to_csv(r'C:/xampp/htdocs/nasiasense/hist/h/nzdusdH_raw.csv')
#fxcmpy.to_csv(r'C:\Users\atsal\GGGGG.csv')
print(x.tail())



df=fxcmpy.fxcmpy(access_token=TOKEN,log_level='error',server='demo')
x = df.get_candles('USD/TRY', period='H1', number=tonoumero)

#print(df())
x.to_csv(r'C:/xampp/htdocs/nasiasense/hist/h/usdtryH_raw.csv')
#fxcmpy.to_csv(r'C:\Users\atsal\GGGGG.csv')
print(x.tail())



df=fxcmpy.fxcmpy(access_token=TOKEN,log_level='error',server='demo')
x = df.get_candles('USD/ZAR', period='H1', number=tonoumero)

#print(df())
x.to_csv(r'C:/xampp/htdocs/nasiasense/hist/h/usdzarH_raw.csv')
#fxcmpy.to_csv(r'C:\Users\atsal\GGGGG.csv')
print(x.tail())














