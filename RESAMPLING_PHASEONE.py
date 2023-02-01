from __future__ import division
import pandas as pd
import numpy as np

import time
import matplotlib.pyplot as plt

from datetime import datetime, timedelta

date_today = datetime.now()
df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/hist/h/eurusdH_raw.csv",)



del df['date']

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'date': days,})
df['date'] = df2['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty']]
df = df.set_index('date')

df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/eurusdH_raw.csv')
print(df.tail())
###

date_today = datetime.now()
df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/hist/h/gbpusdH_raw.csv",)



del df['date']

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'date': days,})
df['date'] = df2['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty']]
df = df.set_index('date')

df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/gbpusdH_raw.csv')
print(df.tail())

####
date_today = datetime.now()
df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/hist/h/usdchfH_raw.csv",)



del df['date']

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'date': days,})
df['date'] = df2['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty']]
df = df.set_index('date')

df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/usdchfH_raw.csv')
print(df.tail())


#######date_today = datetime.now()
df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/hist/h/usdjpyH_raw.csv",)



del df['date']

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'date': days,})
df['date'] = df2['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty']]
df = df.set_index('date')

df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/usdjpyH_raw.csv')
print(df.tail())
####

date_today = datetime.now()
df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/hist/h/gbpjpyH_raw.csv",)



del df['date']

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'date': days,})
df['date'] = df2['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty']]
df = df.set_index('date')

df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/gbpjpyH_raw.csv')
print(df.tail())


###

date_today = datetime.now()
df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/hist/h/eurchfH_raw.csv",)



del df['date']

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'date': days,})
df['date'] = df2['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty']]
df = df.set_index('date')

df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/eurchfH_raw.csv')
print(df.tail())


###


date_today = datetime.now()
df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/hist/h/chfjpyH_raw.csv",)



del df['date']

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'date': days,})
df['date'] = df2['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty']]
df = df.set_index('date')

df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/chfjpyH_raw.csv')
print(df.tail())
#######################################


date_today = datetime.now()
df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/hist/h/eurjpyH_raw.csv",)



del df['date']

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'date': days,})
df['date'] = df2['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty']]
df = df.set_index('date')

df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/eurjpyH_raw.csv')
print(df.tail())


########


date_today = datetime.now()
df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/hist/h/eurgbpH_raw.csv",)



del df['date']

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'date': days,})
df['date'] = df2['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty']]
df = df.set_index('date')

df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/eurgbpH_raw.csv')
print(df.tail())

########


date_today = datetime.now()
df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/hist/h/eurcadH_raw.csv",)



del df['date']

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'date': days,})
df['date'] = df2['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty']]
df = df.set_index('date')

df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/eurcadH_raw.csv')
print(df.tail())


####

date_today = datetime.now()
df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/hist/h/audusdH_raw.csv",)



del df['date']

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'date': days,})
df['date'] = df2['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty']]
df = df.set_index('date')

df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/audusdH_raw.csv')
print(df.tail())

date_today = datetime.now()
df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/hist/h/audusdH_raw.csv",)



del df['date']

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'date': days,})
df['date'] = df2['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty']]
df = df.set_index('date')

df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/audusdH_raw.csv')
print(df.tail())


#####


date_today = datetime.now()
df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/hist/h/audchfH_raw.csv",)



del df['date']

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'date': days,})
df['date'] = df2['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty']]
df = df.set_index('date')

df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/audchfH_raw.csv')
print(df.tail())



##########

date_today = datetime.now()
df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/hist/h/nzdjpyH_raw.csv",)



del df['date']

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'date': days,})
df['date'] = df2['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty']]
df = df.set_index('date')

df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/nzdjpyH_raw.csv')
print(df.tail())


##########

date_today = datetime.now()
df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/hist/h/xauusdH_raw.csv",)



del df['date']

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'date': days,})
df['date'] = df2['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty']]
df = df.set_index('date')

df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/xauusdH_raw.csv')
print(df.tail())


##########

date_today = datetime.now()
df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/hist/h/xagusdH_raw.csv",)



del df['date']

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'date': days,})
df['date'] = df2['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty']]
df = df.set_index('date')

df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/xagusdH_raw.csv')
print(df.tail())


##########

date_today = datetime.now()
df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/hist/h/usdcadH_raw.csv",)



del df['date']

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'date': days,})
df['date'] = df2['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty']]
df = df.set_index('date')

df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/usdcadH_raw.csv')
print(df.tail())


##########

date_today = datetime.now()
df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/hist/h/audcadH_raw.csv",)



del df['date']

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'date': days,})
df['date'] = df2['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty']]
df = df.set_index('date')

df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/audcadH_raw.csv')
print(df.tail())


##########

date_today = datetime.now()
df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/hist/h/audjpyH_raw.csv",)



del df['date']

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'date': days,})
df['date'] = df2['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty']]
df = df.set_index('date')

df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/audjpyH_raw.csv')
print(df.tail())

##########

date_today = datetime.now()
df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/hist/h/cadchfH_raw.csv",)



del df['date']

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'date': days,})
df['date'] = df2['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty']]
df = df.set_index('date')

df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/cadchfH_raw.csv')
print(df.tail())



##########

date_today = datetime.now()
df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/hist/h/cadjpyH_raw.csv",)



del df['date']

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'date': days,})
df['date'] = df2['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty']]
df = df.set_index('date')

df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/cadjpyH_raw.csv')
print(df.tail())


##########

date_today = datetime.now()
df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/hist/h/euraudH_raw.csv",)



del df['date']

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'date': days,})
df['date'] = df2['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty']]
df = df.set_index('date')

df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/euraudH_raw.csv')
print(df.tail())


##########

date_today = datetime.now()
df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/hist/h/eurnzdH_raw.csv",)



del df['date']

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'date': days,})
df['date'] = df2['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty']]
df = df.set_index('date')

df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/eurnzdH_raw.csv')
print(df.tail())



##########

date_today = datetime.now()
df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/hist/h/gbpaudH_raw.csv",)



del df['date']

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'date': days,})
df['date'] = df2['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty']]
df = df.set_index('date')

df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/gbpaudH_raw.csv')
print(df.tail())


##########

date_today = datetime.now()
df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/hist/h/gbpcadH_raw.csv",)



del df['date']

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'date': days,})
df['date'] = df2['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty']]
df = df.set_index('date')

df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/gbpcadH_raw.csv')
print(df.tail())


##########

date_today = datetime.now()
df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/hist/h/gbpchfH_raw.csv",)



del df['date']

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'date': days,})
df['date'] = df2['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty']]
df = df.set_index('date')

df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/gbpchfH_raw.csv')
print(df.tail())


##########

date_today = datetime.now()
df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/hist/h/gbpnzdH_raw.csv",)



del df['date']

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'date': days,})
df['date'] = df2['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty']]
df = df.set_index('date')

df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/gbpnzdH_raw.csv')
print(df.tail())


##########

date_today = datetime.now()
df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/hist/h/nzdcadH_raw.csv",)



del df['date']

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'date': days,})
df['date'] = df2['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty']]
df = df.set_index('date')

df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/nzdcadH_raw.csv')
print(df.tail())


##########

date_today = datetime.now()
df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/hist/h/nzdchfH_raw.csv",)



del df['date']

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'date': days,})
df['date'] = df2['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty']]
df = df.set_index('date')

df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/nzdchfH_raw.csv')
print(df.tail())


##########

date_today = datetime.now()
df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/hist/h/nzdusdH_raw.csv",)



del df['date']

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'date': days,})
df['date'] = df2['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty']]
df = df.set_index('date')

df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/nzdusdH_raw.csv')
print(df.tail())


##########

date_today = datetime.now()
df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/hist/h/usdtryH_raw.csv",)



del df['date']

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'date': days,})
df['date'] = df2['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty']]
df = df.set_index('date')

df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/usdtryH_raw.csv')
print(df.tail())



##########

date_today = datetime.now()
df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/hist/h/usdzarH_raw.csv",)



del df['date']

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'date': days,})
df['date'] = df2['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty']]
df = df.set_index('date')

df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/usdzarH_raw.csv')
print(df.tail())




##########

date_today = datetime.now()
df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/hist/h/audnzdH_raw.csv",)



del df['date']

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'date': days,})
df['date'] = df2['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty']]
df = df.set_index('date')

df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/audnzdH_raw.csv')
print(df.tail())










