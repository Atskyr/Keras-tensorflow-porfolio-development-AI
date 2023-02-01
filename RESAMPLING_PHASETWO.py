###giATIMER


from __future__ import division
import pandas as pd
import numpy as np

import time
import matplotlib.pyplot as plt

from datetime import datetime, timedelta


df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/eurusdH_raw.csv",)


#f = (columns=['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty'])



#df2['date'] = df1['date'].values
#df2['hour'] = df1['hour'].values

df=df.rename(columns = {'date':'Date'})

df=df.rename(columns = {'bidclose':'Close'})
df=df.rename(columns = {'bidhigh':'High'})
df=df.rename(columns = {'bidlow':'Low'})
df=df.rename(columns = {'bidopen':'Open'})
df=df.rename(columns = {'tickqty':'Volume'})


#df = pd.DataFrame({'xxx': days,})
#df['DOB1'] = df['xxx'].dt.strftime('%Y-%m-%d')


del df['Date']
del df['askopen']
del df['askclose']
del df['askhigh']
del df['asklow']

#f.insert(2, "Age", days)
date_today = datetime.now()

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'Date': days,})
df['Date'] = df2['Date'].dt.strftime('%Y-%m-%d')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['Date', 'Open', 'Close', 'High', 'Low', 'Volume']]
#df = df.set_index('Date')

#df = df.set_index('DOB1')
#print(df)


#del df['Date']
#df['Date'] = [x[:-22] for x in df['Date']]

#df.index=pd.to_datetime(df["Date"])
#df=df.drop("Date",axis=1)


#dfm=df.resample("M").mean()

#dfm=dfm[:-1] # As we said, we do not consider the month of end_date
df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/validated/eurusdH_val.csv')
print(df.tail(10))


##########

df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/gbpusdH_raw.csv",)


#f = (columns=['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty'])



#df2['date'] = df1['date'].values
#df2['hour'] = df1['hour'].values

df=df.rename(columns = {'date':'Date'})

df=df.rename(columns = {'bidclose':'Close'})
df=df.rename(columns = {'bidhigh':'High'})
df=df.rename(columns = {'bidlow':'Low'})
df=df.rename(columns = {'bidopen':'Open'})
df=df.rename(columns = {'tickqty':'Volume'})


#df = pd.DataFrame({'xxx': days,})
#df['DOB1'] = df['xxx'].dt.strftime('%Y-%m-%d')


del df['Date']
del df['askopen']
del df['askclose']
del df['askhigh']
del df['asklow']

#f.insert(2, "Age", days)
date_today = datetime.now()

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'Date': days,})
df['Date'] = df2['Date'].dt.strftime('%Y-%m-%d')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['Date', 'Open', 'Close', 'High', 'Low', 'Volume']]
#df = df.set_index('Date')

#df = df.set_index('DOB1')
#print(df)


#del df['Date']
#df['Date'] = [x[:-22] for x in df['Date']]

#df.index=pd.to_datetime(df["Date"])
#df=df.drop("Date",axis=1)


#dfm=df.resample("M").mean()

#dfm=dfm[:-1] # As we said, we do not consider the month of end_date
df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/validated/gbpusdH_val.csv')
print(df.tail(10))


###

df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/usdchfH_raw.csv",)


#f = (columns=['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty'])



#df2['date'] = df1['date'].values
#df2['hour'] = df1['hour'].values

df=df.rename(columns = {'date':'Date'})

df=df.rename(columns = {'bidclose':'Close'})
df=df.rename(columns = {'bidhigh':'High'})
df=df.rename(columns = {'bidlow':'Low'})
df=df.rename(columns = {'bidopen':'Open'})
df=df.rename(columns = {'tickqty':'Volume'})


#df = pd.DataFrame({'xxx': days,})
#df['DOB1'] = df['xxx'].dt.strftime('%Y-%m-%d')


del df['Date']
del df['askopen']
del df['askclose']
del df['askhigh']
del df['asklow']

#f.insert(2, "Age", days)
date_today = datetime.now()

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'Date': days,})
df['Date'] = df2['Date'].dt.strftime('%Y-%m-%d')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['Date', 'Open', 'Close', 'High', 'Low', 'Volume']]
#df = df.set_index('Date')

#df = df.set_index('DOB1')
#print(df)


#del df['Date']
#df['Date'] = [x[:-22] for x in df['Date']]

#df.index=pd.to_datetime(df["Date"])
#df=df.drop("Date",axis=1)


#dfm=df.resample("M").mean()

#dfm=dfm[:-1] # As we said, we do not consider the month of end_date
df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/validated/usdchfH_val.csv')
print(df.tail(10))

###

df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/usdjpyH_raw.csv",)


#f = (columns=['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty'])



#df2['date'] = df1['date'].values
#df2['hour'] = df1['hour'].values

df=df.rename(columns = {'date':'Date'})

df=df.rename(columns = {'bidclose':'Close'})
df=df.rename(columns = {'bidhigh':'High'})
df=df.rename(columns = {'bidlow':'Low'})
df=df.rename(columns = {'bidopen':'Open'})
df=df.rename(columns = {'tickqty':'Volume'})


#df = pd.DataFrame({'xxx': days,})
#df['DOB1'] = df['xxx'].dt.strftime('%Y-%m-%d')


del df['Date']
del df['askopen']
del df['askclose']
del df['askhigh']
del df['asklow']

#f.insert(2, "Age", days)
date_today = datetime.now()

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'Date': days,})
df['Date'] = df2['Date'].dt.strftime('%Y-%m-%d')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['Date', 'Open', 'Close', 'High', 'Low', 'Volume']]
#df = df.set_index('Date')

#df = df.set_index('DOB1')
#print(df)


#del df['Date']
#df['Date'] = [x[:-22] for x in df['Date']]

#df.index=pd.to_datetime(df["Date"])
#df=df.drop("Date",axis=1)


#dfm=df.resample("M").mean()

#dfm=dfm[:-1] # As we said, we do not consider the month of end_date
df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/validated/usdjpyH_val.csv')
print(df.tail(10))


##


df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/gbpjpyH_raw.csv",)


#f = (columns=['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty'])



#df2['date'] = df1['date'].values
#df2['hour'] = df1['hour'].values

df=df.rename(columns = {'date':'Date'})

df=df.rename(columns = {'bidclose':'Close'})
df=df.rename(columns = {'bidhigh':'High'})
df=df.rename(columns = {'bidlow':'Low'})
df=df.rename(columns = {'bidopen':'Open'})
df=df.rename(columns = {'tickqty':'Volume'})


#df = pd.DataFrame({'xxx': days,})
#df['DOB1'] = df['xxx'].dt.strftime('%Y-%m-%d')


del df['Date']
del df['askopen']
del df['askclose']
del df['askhigh']
del df['asklow']

#f.insert(2, "Age", days)
date_today = datetime.now()

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'Date': days,})
df['Date'] = df2['Date'].dt.strftime('%Y-%m-%d')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['Date', 'Open', 'Close', 'High', 'Low', 'Volume']]
#df = df.set_index('Date')

#df = df.set_index('DOB1')
#print(df)


#del df['Date']
#df['Date'] = [x[:-22] for x in df['Date']]

#df.index=pd.to_datetime(df["Date"])
#df=df.drop("Date",axis=1)


#dfm=df.resample("M").mean()

#dfm=dfm[:-1] # As we said, we do not consider the month of end_date
df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/validated/gbpjpyH_val.csv')
print(df.tail(10))

###


df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/eurchfH_raw.csv",)


#f = (columns=['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty'])



#df2['date'] = df1['date'].values
#df2['hour'] = df1['hour'].values

df=df.rename(columns = {'date':'Date'})

df=df.rename(columns = {'bidclose':'Close'})
df=df.rename(columns = {'bidhigh':'High'})
df=df.rename(columns = {'bidlow':'Low'})
df=df.rename(columns = {'bidopen':'Open'})
df=df.rename(columns = {'tickqty':'Volume'})


#df = pd.DataFrame({'xxx': days,})
#df['DOB1'] = df['xxx'].dt.strftime('%Y-%m-%d')


del df['Date']
del df['askopen']
del df['askclose']
del df['askhigh']
del df['asklow']

#f.insert(2, "Age", days)
date_today = datetime.now()

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'Date': days,})
df['Date'] = df2['Date'].dt.strftime('%Y-%m-%d')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['Date', 'Open', 'Close', 'High', 'Low', 'Volume']]
#df = df.set_index('Date')

#df = df.set_index('DOB1')
#print(df)


#del df['Date']
#df['Date'] = [x[:-22] for x in df['Date']]

#df.index=pd.to_datetime(df["Date"])
#df=df.drop("Date",axis=1)


#dfm=df.resample("M").mean()

#dfm=dfm[:-1] # As we said, we do not consider the month of end_date
df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/validated/eurchfH_val.csv')
print(df.tail(10))

####


df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/chfjpyH_raw.csv",)


#f = (columns=['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty'])



#df2['date'] = df1['date'].values
#df2['hour'] = df1['hour'].values

df=df.rename(columns = {'date':'Date'})

df=df.rename(columns = {'bidclose':'Close'})
df=df.rename(columns = {'bidhigh':'High'})
df=df.rename(columns = {'bidlow':'Low'})
df=df.rename(columns = {'bidopen':'Open'})
df=df.rename(columns = {'tickqty':'Volume'})


#df = pd.DataFrame({'xxx': days,})
#df['DOB1'] = df['xxx'].dt.strftime('%Y-%m-%d')


del df['Date']
del df['askopen']
del df['askclose']
del df['askhigh']
del df['asklow']

#f.insert(2, "Age", days)
date_today = datetime.now()

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'Date': days,})
df['Date'] = df2['Date'].dt.strftime('%Y-%m-%d')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['Date', 'Open', 'Close', 'High', 'Low', 'Volume']]
#df = df.set_index('Date')

#df = df.set_index('DOB1')
#print(df)


#del df['Date']
#df['Date'] = [x[:-22] for x in df['Date']]

#df.index=pd.to_datetime(df["Date"])
#df=df.drop("Date",axis=1)


#dfm=df.resample("M").mean()

#dfm=dfm[:-1] # As we said, we do not consider the month of end_date
df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/validated/chfjpyH_val.csv')
print(df.tail(10))


####


df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/eurjpyH_raw.csv",)


#f = (columns=['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty'])



#df2['date'] = df1['date'].values
#df2['hour'] = df1['hour'].values

df=df.rename(columns = {'date':'Date'})

df=df.rename(columns = {'bidclose':'Close'})
df=df.rename(columns = {'bidhigh':'High'})
df=df.rename(columns = {'bidlow':'Low'})
df=df.rename(columns = {'bidopen':'Open'})
df=df.rename(columns = {'tickqty':'Volume'})


#df = pd.DataFrame({'xxx': days,})
#df['DOB1'] = df['xxx'].dt.strftime('%Y-%m-%d')


del df['Date']
del df['askopen']
del df['askclose']
del df['askhigh']
del df['asklow']

#f.insert(2, "Age", days)
date_today = datetime.now()

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'Date': days,})
df['Date'] = df2['Date'].dt.strftime('%Y-%m-%d')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['Date', 'Open', 'Close', 'High', 'Low', 'Volume']]
#df = df.set_index('Date')

#df = df.set_index('DOB1')
#print(df)


#del df['Date']
#df['Date'] = [x[:-22] for x in df['Date']]

#df.index=pd.to_datetime(df["Date"])
#df=df.drop("Date",axis=1)


#dfm=df.resample("M").mean()

#dfm=dfm[:-1] # As we said, we do not consider the month of end_date
df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/validated/eurjpyH_val.csv')
print(df.tail(10))

##


df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/eurgbpH_raw.csv",)


#f = (columns=['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty'])



#df2['date'] = df1['date'].values
#df2['hour'] = df1['hour'].values

df=df.rename(columns = {'date':'Date'})

df=df.rename(columns = {'bidclose':'Close'})
df=df.rename(columns = {'bidhigh':'High'})
df=df.rename(columns = {'bidlow':'Low'})
df=df.rename(columns = {'bidopen':'Open'})
df=df.rename(columns = {'tickqty':'Volume'})


#df = pd.DataFrame({'xxx': days,})
#df['DOB1'] = df['xxx'].dt.strftime('%Y-%m-%d')


del df['Date']
del df['askopen']
del df['askclose']
del df['askhigh']
del df['asklow']

#f.insert(2, "Age", days)
date_today = datetime.now()

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'Date': days,})
df['Date'] = df2['Date'].dt.strftime('%Y-%m-%d')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['Date', 'Open', 'Close', 'High', 'Low', 'Volume']]
#df = df.set_index('Date')

#df = df.set_index('DOB1')
#print(df)


#del df['Date']
#df['Date'] = [x[:-22] for x in df['Date']]

#df.index=pd.to_datetime(df["Date"])
#df=df.drop("Date",axis=1)


#dfm=df.resample("M").mean()

#dfm=dfm[:-1] # As we said, we do not consider the month of end_date
df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/validated/eurgbpH_val.csv')
print(df.tail(10))

######


df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/eurcadH_raw.csv",)


#f = (columns=['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty'])



#df2['date'] = df1['date'].values
#df2['hour'] = df1['hour'].values

df=df.rename(columns = {'date':'Date'})

df=df.rename(columns = {'bidclose':'Close'})
df=df.rename(columns = {'bidhigh':'High'})
df=df.rename(columns = {'bidlow':'Low'})
df=df.rename(columns = {'bidopen':'Open'})
df=df.rename(columns = {'tickqty':'Volume'})


#df = pd.DataFrame({'xxx': days,})
#df['DOB1'] = df['xxx'].dt.strftime('%Y-%m-%d')


del df['Date']
del df['askopen']
del df['askclose']
del df['askhigh']
del df['asklow']

#f.insert(2, "Age", days)
date_today = datetime.now()

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'Date': days,})
df['Date'] = df2['Date'].dt.strftime('%Y-%m-%d')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['Date', 'Open', 'Close', 'High', 'Low', 'Volume']]
#df = df.set_index('Date')

#df = df.set_index('DOB1')
#print(df)


#del df['Date']
#df['Date'] = [x[:-22] for x in df['Date']]

#df.index=pd.to_datetime(df["Date"])
#df=df.drop("Date",axis=1)


#dfm=df.resample("M").mean()

#dfm=dfm[:-1] # As we said, we do not consider the month of end_date
df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/validated/eurcadH_val.csv')
print(df.tail(10))


####


df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/audusdH_raw.csv",)


#f = (columns=['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty'])



#df2['date'] = df1['date'].values
#df2['hour'] = df1['hour'].values

df=df.rename(columns = {'date':'Date'})

df=df.rename(columns = {'bidclose':'Close'})
df=df.rename(columns = {'bidhigh':'High'})
df=df.rename(columns = {'bidlow':'Low'})
df=df.rename(columns = {'bidopen':'Open'})
df=df.rename(columns = {'tickqty':'Volume'})


#df = pd.DataFrame({'xxx': days,})
#df['DOB1'] = df['xxx'].dt.strftime('%Y-%m-%d')


del df['Date']
del df['askopen']
del df['askclose']
del df['askhigh']
del df['asklow']

#f.insert(2, "Age", days)
date_today = datetime.now()

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'Date': days,})
df['Date'] = df2['Date'].dt.strftime('%Y-%m-%d')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['Date', 'Open', 'Close', 'High', 'Low', 'Volume']]
#df = df.set_index('Date')

#df = df.set_index('DOB1')
#print(df)


#del df['Date']
#df['Date'] = [x[:-22] for x in df['Date']]

#df.index=pd.to_datetime(df["Date"])
#df=df.drop("Date",axis=1)


#dfm=df.resample("M").mean()

#dfm=dfm[:-1] # As we said, we do not consider the month of end_date
df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/validated/audusdH_val.csv')
print(df.tail(10))

#####

df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/audchfH_raw.csv",)


#f = (columns=['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty'])



#df2['date'] = df1['date'].values
#df2['hour'] = df1['hour'].values

df=df.rename(columns = {'date':'Date'})

df=df.rename(columns = {'bidclose':'Close'})
df=df.rename(columns = {'bidhigh':'High'})
df=df.rename(columns = {'bidlow':'Low'})
df=df.rename(columns = {'bidopen':'Open'})
df=df.rename(columns = {'tickqty':'Volume'})


#df = pd.DataFrame({'xxx': days,})
#df['DOB1'] = df['xxx'].dt.strftime('%Y-%m-%d')


del df['Date']
del df['askopen']
del df['askclose']
del df['askhigh']
del df['asklow']

#f.insert(2, "Age", days)
date_today = datetime.now()

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'Date': days,})
df['Date'] = df2['Date'].dt.strftime('%Y-%m-%d')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['Date', 'Open', 'Close', 'High', 'Low', 'Volume']]
#df = df.set_index('Date')

#df = df.set_index('DOB1')
#print(df)


#del df['Date']
#df['Date'] = [x[:-22] for x in df['Date']]

#df.index=pd.to_datetime(df["Date"])
#df=df.drop("Date",axis=1)


#dfm=df.resample("M").mean()

#dfm=dfm[:-1] # As we said, we do not consider the month of end_date
df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/validated/audchfH_val.csv')
print(df.tail(10))


######

df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/nzdjpyH_raw.csv",)


#f = (columns=['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty'])



#df2['date'] = df1['date'].values
#df2['hour'] = df1['hour'].values

df=df.rename(columns = {'date':'Date'})

df=df.rename(columns = {'bidclose':'Close'})
df=df.rename(columns = {'bidhigh':'High'})
df=df.rename(columns = {'bidlow':'Low'})
df=df.rename(columns = {'bidopen':'Open'})
df=df.rename(columns = {'tickqty':'Volume'})


#df = pd.DataFrame({'xxx': days,})
#df['DOB1'] = df['xxx'].dt.strftime('%Y-%m-%d')


del df['Date']
del df['askopen']
del df['askclose']
del df['askhigh']
del df['asklow']

#f.insert(2, "Age", days)
date_today = datetime.now()

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'Date': days,})
df['Date'] = df2['Date'].dt.strftime('%Y-%m-%d')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['Date', 'Open', 'Close', 'High', 'Low', 'Volume']]
#df = df.set_index('Date')

#df = df.set_index('DOB1')
#print(df)


#del df['Date']
#df['Date'] = [x[:-22] for x in df['Date']]

#df.index=pd.to_datetime(df["Date"])
#df=df.drop("Date",axis=1)


#dfm=df.resample("M").mean()

#dfm=dfm[:-1] # As we said, we do not consider the month of end_date
df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/validated/nzdjpyH_val.csv')
print(df.tail(10))


###########



df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/xauusdH_raw.csv",)


#f = (columns=['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty'])



#df2['date'] = df1['date'].values
#df2['hour'] = df1['hour'].values

df=df.rename(columns = {'date':'Date'})

df=df.rename(columns = {'bidclose':'Close'})
df=df.rename(columns = {'bidhigh':'High'})
df=df.rename(columns = {'bidlow':'Low'})
df=df.rename(columns = {'bidopen':'Open'})
df=df.rename(columns = {'tickqty':'Volume'})


#df = pd.DataFrame({'xxx': days,})
#df['DOB1'] = df['xxx'].dt.strftime('%Y-%m-%d')


del df['Date']
del df['askopen']
del df['askclose']
del df['askhigh']
del df['asklow']

#f.insert(2, "Age", days)
date_today = datetime.now()

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'Date': days,})
df['Date'] = df2['Date'].dt.strftime('%Y-%m-%d')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['Date', 'Open', 'Close', 'High', 'Low', 'Volume']]
#df = df.set_index('Date')

#df = df.set_index('DOB1')
#print(df)


#del df['Date']
#df['Date'] = [x[:-22] for x in df['Date']]

#df.index=pd.to_datetime(df["Date"])
#df=df.drop("Date",axis=1)


#dfm=df.resample("M").mean()

#dfm=dfm[:-1] # As we said, we do not consider the month of end_date
df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/validated/xauusdH_val.csv')
print(df.tail(10))


##########


###########



df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/xagusdH_raw.csv",)


#f = (columns=['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty'])



#df2['date'] = df1['date'].values
#df2['hour'] = df1['hour'].values

df=df.rename(columns = {'date':'Date'})

df=df.rename(columns = {'bidclose':'Close'})
df=df.rename(columns = {'bidhigh':'High'})
df=df.rename(columns = {'bidlow':'Low'})
df=df.rename(columns = {'bidopen':'Open'})
df=df.rename(columns = {'tickqty':'Volume'})


#df = pd.DataFrame({'xxx': days,})
#df['DOB1'] = df['xxx'].dt.strftime('%Y-%m-%d')


del df['Date']
del df['askopen']
del df['askclose']
del df['askhigh']
del df['asklow']

#f.insert(2, "Age", days)
date_today = datetime.now()

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'Date': days,})
df['Date'] = df2['Date'].dt.strftime('%Y-%m-%d')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['Date', 'Open', 'Close', 'High', 'Low', 'Volume']]
#df = df.set_index('Date')

#df = df.set_index('DOB1')
#print(df)


#del df['Date']
#df['Date'] = [x[:-22] for x in df['Date']]

#df.index=pd.to_datetime(df["Date"])
#df=df.drop("Date",axis=1)


#dfm=df.resample("M").mean()

#dfm=dfm[:-1] # As we said, we do not consider the month of end_date
df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/validated/xagusdH_val.csv')
print(df.tail(10))


##########

###########



df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/usdcadH_raw.csv",)


#f = (columns=['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty'])



#df2['date'] = df1['date'].values
#df2['hour'] = df1['hour'].values

df=df.rename(columns = {'date':'Date'})

df=df.rename(columns = {'bidclose':'Close'})
df=df.rename(columns = {'bidhigh':'High'})
df=df.rename(columns = {'bidlow':'Low'})
df=df.rename(columns = {'bidopen':'Open'})
df=df.rename(columns = {'tickqty':'Volume'})


#df = pd.DataFrame({'xxx': days,})
#df['DOB1'] = df['xxx'].dt.strftime('%Y-%m-%d')


del df['Date']
del df['askopen']
del df['askclose']
del df['askhigh']
del df['asklow']

#f.insert(2, "Age", days)
date_today = datetime.now()

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'Date': days,})
df['Date'] = df2['Date'].dt.strftime('%Y-%m-%d')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['Date', 'Open', 'Close', 'High', 'Low', 'Volume']]
#df = df.set_index('Date')

#df = df.set_index('DOB1')
#print(df)


#del df['Date']
#df['Date'] = [x[:-22] for x in df['Date']]

#df.index=pd.to_datetime(df["Date"])
#df=df.drop("Date",axis=1)


#dfm=df.resample("M").mean()

#dfm=dfm[:-1] # As we said, we do not consider the month of end_date
df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/validated/usdcadH_val.csv')
print(df.tail(10))


##########


###########



df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/audcadH_raw.csv",)


#f = (columns=['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty'])



#df2['date'] = df1['date'].values
#df2['hour'] = df1['hour'].values

df=df.rename(columns = {'date':'Date'})

df=df.rename(columns = {'bidclose':'Close'})
df=df.rename(columns = {'bidhigh':'High'})
df=df.rename(columns = {'bidlow':'Low'})
df=df.rename(columns = {'bidopen':'Open'})
df=df.rename(columns = {'tickqty':'Volume'})


#df = pd.DataFrame({'xxx': days,})
#df['DOB1'] = df['xxx'].dt.strftime('%Y-%m-%d')


del df['Date']
del df['askopen']
del df['askclose']
del df['askhigh']
del df['asklow']

#f.insert(2, "Age", days)
date_today = datetime.now()

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'Date': days,})
df['Date'] = df2['Date'].dt.strftime('%Y-%m-%d')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['Date', 'Open', 'Close', 'High', 'Low', 'Volume']]
#df = df.set_index('Date')

#df = df.set_index('DOB1')
#print(df)


#del df['Date']
#df['Date'] = [x[:-22] for x in df['Date']]

#df.index=pd.to_datetime(df["Date"])
#df=df.drop("Date",axis=1)


#dfm=df.resample("M").mean()

#dfm=dfm[:-1] # As we said, we do not consider the month of end_date
df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/validated/audcadH_val.csv')
print(df.tail(10))


##########

###########



df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/audjpyH_raw.csv",)


#f = (columns=['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty'])



#df2['date'] = df1['date'].values
#df2['hour'] = df1['hour'].values

df=df.rename(columns = {'date':'Date'})

df=df.rename(columns = {'bidclose':'Close'})
df=df.rename(columns = {'bidhigh':'High'})
df=df.rename(columns = {'bidlow':'Low'})
df=df.rename(columns = {'bidopen':'Open'})
df=df.rename(columns = {'tickqty':'Volume'})


#df = pd.DataFrame({'xxx': days,})
#df['DOB1'] = df['xxx'].dt.strftime('%Y-%m-%d')


del df['Date']
del df['askopen']
del df['askclose']
del df['askhigh']
del df['asklow']

#f.insert(2, "Age", days)
date_today = datetime.now()

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'Date': days,})
df['Date'] = df2['Date'].dt.strftime('%Y-%m-%d')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['Date', 'Open', 'Close', 'High', 'Low', 'Volume']]
#df = df.set_index('Date')

#df = df.set_index('DOB1')
#print(df)


#del df['Date']
#df['Date'] = [x[:-22] for x in df['Date']]

#df.index=pd.to_datetime(df["Date"])
#df=df.drop("Date",axis=1)


#dfm=df.resample("M").mean()

#dfm=dfm[:-1] # As we said, we do not consider the month of end_date
df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/validated/audjpyH_val.csv')
print(df.tail(10))


##########


###########



df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/audnzdH_raw.csv",)


#f = (columns=['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty'])



#df2['date'] = df1['date'].values
#df2['hour'] = df1['hour'].values

df=df.rename(columns = {'date':'Date'})

df=df.rename(columns = {'bidclose':'Close'})
df=df.rename(columns = {'bidhigh':'High'})
df=df.rename(columns = {'bidlow':'Low'})
df=df.rename(columns = {'bidopen':'Open'})
df=df.rename(columns = {'tickqty':'Volume'})


#df = pd.DataFrame({'xxx': days,})
#df['DOB1'] = df['xxx'].dt.strftime('%Y-%m-%d')


del df['Date']
del df['askopen']
del df['askclose']
del df['askhigh']
del df['asklow']

#f.insert(2, "Age", days)
date_today = datetime.now()

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'Date': days,})
df['Date'] = df2['Date'].dt.strftime('%Y-%m-%d')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['Date', 'Open', 'Close', 'High', 'Low', 'Volume']]
#df = df.set_index('Date')

#df = df.set_index('DOB1')
#print(df)


#del df['Date']
#df['Date'] = [x[:-22] for x in df['Date']]

#df.index=pd.to_datetime(df["Date"])
#df=df.drop("Date",axis=1)


#dfm=df.resample("M").mean()

#dfm=dfm[:-1] # As we said, we do not consider the month of end_date
df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/validated/audnzdH_val.csv')
print(df.tail(10))


##########


###########



df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/cadchfH_raw.csv",)


#f = (columns=['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty'])



#df2['date'] = df1['date'].values
#df2['hour'] = df1['hour'].values

df=df.rename(columns = {'date':'Date'})

df=df.rename(columns = {'bidclose':'Close'})
df=df.rename(columns = {'bidhigh':'High'})
df=df.rename(columns = {'bidlow':'Low'})
df=df.rename(columns = {'bidopen':'Open'})
df=df.rename(columns = {'tickqty':'Volume'})


#df = pd.DataFrame({'xxx': days,})
#df['DOB1'] = df['xxx'].dt.strftime('%Y-%m-%d')


del df['Date']
del df['askopen']
del df['askclose']
del df['askhigh']
del df['asklow']

#f.insert(2, "Age", days)
date_today = datetime.now()

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'Date': days,})
df['Date'] = df2['Date'].dt.strftime('%Y-%m-%d')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['Date', 'Open', 'Close', 'High', 'Low', 'Volume']]
#df = df.set_index('Date')

#df = df.set_index('DOB1')
#print(df)


#del df['Date']
#df['Date'] = [x[:-22] for x in df['Date']]

#df.index=pd.to_datetime(df["Date"])
#df=df.drop("Date",axis=1)


#dfm=df.resample("M").mean()

#dfm=dfm[:-1] # As we said, we do not consider the month of end_date
df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/validated/cadchfH_val.csv')
print(df.tail(10))


##########


###########



df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/cadjpyH_raw.csv",)


#f = (columns=['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty'])



#df2['date'] = df1['date'].values
#df2['hour'] = df1['hour'].values

df=df.rename(columns = {'date':'Date'})

df=df.rename(columns = {'bidclose':'Close'})
df=df.rename(columns = {'bidhigh':'High'})
df=df.rename(columns = {'bidlow':'Low'})
df=df.rename(columns = {'bidopen':'Open'})
df=df.rename(columns = {'tickqty':'Volume'})


#df = pd.DataFrame({'xxx': days,})
#df['DOB1'] = df['xxx'].dt.strftime('%Y-%m-%d')


del df['Date']
del df['askopen']
del df['askclose']
del df['askhigh']
del df['asklow']

#f.insert(2, "Age", days)
date_today = datetime.now()

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'Date': days,})
df['Date'] = df2['Date'].dt.strftime('%Y-%m-%d')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['Date', 'Open', 'Close', 'High', 'Low', 'Volume']]
#df = df.set_index('Date')

#df = df.set_index('DOB1')
#print(df)


#del df['Date']
#df['Date'] = [x[:-22] for x in df['Date']]

#df.index=pd.to_datetime(df["Date"])
#df=df.drop("Date",axis=1)


#dfm=df.resample("M").mean()

#dfm=dfm[:-1] # As we said, we do not consider the month of end_date
df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/validated/cadjpyH_val.csv')
print(df.tail(10))


##########

###########



df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/euraudH_raw.csv",)


#f = (columns=['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty'])



#df2['date'] = df1['date'].values
#df2['hour'] = df1['hour'].values

df=df.rename(columns = {'date':'Date'})

df=df.rename(columns = {'bidclose':'Close'})
df=df.rename(columns = {'bidhigh':'High'})
df=df.rename(columns = {'bidlow':'Low'})
df=df.rename(columns = {'bidopen':'Open'})
df=df.rename(columns = {'tickqty':'Volume'})


#df = pd.DataFrame({'xxx': days,})
#df['DOB1'] = df['xxx'].dt.strftime('%Y-%m-%d')


del df['Date']
del df['askopen']
del df['askclose']
del df['askhigh']
del df['asklow']

#f.insert(2, "Age", days)
date_today = datetime.now()

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'Date': days,})
df['Date'] = df2['Date'].dt.strftime('%Y-%m-%d')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['Date', 'Open', 'Close', 'High', 'Low', 'Volume']]
#df = df.set_index('Date')

#df = df.set_index('DOB1')
#print(df)


#del df['Date']
#df['Date'] = [x[:-22] for x in df['Date']]

#df.index=pd.to_datetime(df["Date"])
#df=df.drop("Date",axis=1)


#dfm=df.resample("M").mean()

#dfm=dfm[:-1] # As we said, we do not consider the month of end_date
df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/validated/euraudH_val.csv')
print(df.tail(10))


##########

###########



df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/eurnzdH_raw.csv",)


#f = (columns=['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty'])



#df2['date'] = df1['date'].values
#df2['hour'] = df1['hour'].values

df=df.rename(columns = {'date':'Date'})

df=df.rename(columns = {'bidclose':'Close'})
df=df.rename(columns = {'bidhigh':'High'})
df=df.rename(columns = {'bidlow':'Low'})
df=df.rename(columns = {'bidopen':'Open'})
df=df.rename(columns = {'tickqty':'Volume'})


#df = pd.DataFrame({'xxx': days,})
#df['DOB1'] = df['xxx'].dt.strftime('%Y-%m-%d')


del df['Date']
del df['askopen']
del df['askclose']
del df['askhigh']
del df['asklow']

#f.insert(2, "Age", days)
date_today = datetime.now()

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'Date': days,})
df['Date'] = df2['Date'].dt.strftime('%Y-%m-%d')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['Date', 'Open', 'Close', 'High', 'Low', 'Volume']]
#df = df.set_index('Date')

#df = df.set_index('DOB1')
#print(df)


#del df['Date']
#df['Date'] = [x[:-22] for x in df['Date']]

#df.index=pd.to_datetime(df["Date"])
#df=df.drop("Date",axis=1)


#dfm=df.resample("M").mean()

#dfm=dfm[:-1] # As we said, we do not consider the month of end_date
df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/validated/eurnzdH_val.csv')
print(df.tail(10))


##########

###########



df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/gbpaudH_raw.csv",)


#f = (columns=['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty'])



#df2['date'] = df1['date'].values
#df2['hour'] = df1['hour'].values

df=df.rename(columns = {'date':'Date'})

df=df.rename(columns = {'bidclose':'Close'})
df=df.rename(columns = {'bidhigh':'High'})
df=df.rename(columns = {'bidlow':'Low'})
df=df.rename(columns = {'bidopen':'Open'})
df=df.rename(columns = {'tickqty':'Volume'})


#df = pd.DataFrame({'xxx': days,})
#df['DOB1'] = df['xxx'].dt.strftime('%Y-%m-%d')


del df['Date']
del df['askopen']
del df['askclose']
del df['askhigh']
del df['asklow']

#f.insert(2, "Age", days)
date_today = datetime.now()

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'Date': days,})
df['Date'] = df2['Date'].dt.strftime('%Y-%m-%d')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['Date', 'Open', 'Close', 'High', 'Low', 'Volume']]
#df = df.set_index('Date')

#df = df.set_index('DOB1')
#print(df)


#del df['Date']
#df['Date'] = [x[:-22] for x in df['Date']]

#df.index=pd.to_datetime(df["Date"])
#df=df.drop("Date",axis=1)


#dfm=df.resample("M").mean()

#dfm=dfm[:-1] # As we said, we do not consider the month of end_date
df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/validated/gbpaudH_val.csv')
print(df.tail(10))


##########

###########



df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/gbpcadH_raw.csv",)


#f = (columns=['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty'])



#df2['date'] = df1['date'].values
#df2['hour'] = df1['hour'].values

df=df.rename(columns = {'date':'Date'})

df=df.rename(columns = {'bidclose':'Close'})
df=df.rename(columns = {'bidhigh':'High'})
df=df.rename(columns = {'bidlow':'Low'})
df=df.rename(columns = {'bidopen':'Open'})
df=df.rename(columns = {'tickqty':'Volume'})


#df = pd.DataFrame({'xxx': days,})
#df['DOB1'] = df['xxx'].dt.strftime('%Y-%m-%d')


del df['Date']
del df['askopen']
del df['askclose']
del df['askhigh']
del df['asklow']

#f.insert(2, "Age", days)
date_today = datetime.now()

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'Date': days,})
df['Date'] = df2['Date'].dt.strftime('%Y-%m-%d')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['Date', 'Open', 'Close', 'High', 'Low', 'Volume']]
#df = df.set_index('Date')

#df = df.set_index('DOB1')
#print(df)


#del df['Date']
#df['Date'] = [x[:-22] for x in df['Date']]

#df.index=pd.to_datetime(df["Date"])
#df=df.drop("Date",axis=1)


#dfm=df.resample("M").mean()

#dfm=dfm[:-1] # As we said, we do not consider the month of end_date
df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/validated/gbpcadH_val.csv')
print(df.tail(10))


##########
###########



df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/gbpchfH_raw.csv",)


#f = (columns=['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty'])



#df2['date'] = df1['date'].values
#df2['hour'] = df1['hour'].values

df=df.rename(columns = {'date':'Date'})

df=df.rename(columns = {'bidclose':'Close'})
df=df.rename(columns = {'bidhigh':'High'})
df=df.rename(columns = {'bidlow':'Low'})
df=df.rename(columns = {'bidopen':'Open'})
df=df.rename(columns = {'tickqty':'Volume'})


#df = pd.DataFrame({'xxx': days,})
#df['DOB1'] = df['xxx'].dt.strftime('%Y-%m-%d')


del df['Date']
del df['askopen']
del df['askclose']
del df['askhigh']
del df['asklow']

#f.insert(2, "Age", days)
date_today = datetime.now()

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'Date': days,})
df['Date'] = df2['Date'].dt.strftime('%Y-%m-%d')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['Date', 'Open', 'Close', 'High', 'Low', 'Volume']]
#df = df.set_index('Date')

#df = df.set_index('DOB1')
#print(df)


#del df['Date']
#df['Date'] = [x[:-22] for x in df['Date']]

#df.index=pd.to_datetime(df["Date"])
#df=df.drop("Date",axis=1)


#dfm=df.resample("M").mean()

#dfm=dfm[:-1] # As we said, we do not consider the month of end_date
df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/validated/gbpchfH_val.csv')
print(df.tail(10))


##########


###########



df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/gbpnzdH_raw.csv",)


#f = (columns=['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty'])



#df2['date'] = df1['date'].values
#df2['hour'] = df1['hour'].values

df=df.rename(columns = {'date':'Date'})

df=df.rename(columns = {'bidclose':'Close'})
df=df.rename(columns = {'bidhigh':'High'})
df=df.rename(columns = {'bidlow':'Low'})
df=df.rename(columns = {'bidopen':'Open'})
df=df.rename(columns = {'tickqty':'Volume'})


#df = pd.DataFrame({'xxx': days,})
#df['DOB1'] = df['xxx'].dt.strftime('%Y-%m-%d')


del df['Date']
del df['askopen']
del df['askclose']
del df['askhigh']
del df['asklow']

#f.insert(2, "Age", days)
date_today = datetime.now()

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'Date': days,})
df['Date'] = df2['Date'].dt.strftime('%Y-%m-%d')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['Date', 'Open', 'Close', 'High', 'Low', 'Volume']]
#df = df.set_index('Date')

#df = df.set_index('DOB1')
#print(df)


#del df['Date']
#df['Date'] = [x[:-22] for x in df['Date']]

#df.index=pd.to_datetime(df["Date"])
#df=df.drop("Date",axis=1)


#dfm=df.resample("M").mean()

#dfm=dfm[:-1] # As we said, we do not consider the month of end_date
df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/validated/gbpnzdH_val.csv')
print(df.tail(10))


##########

###########



df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/nzdcadH_raw.csv",)


#f = (columns=['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty'])



#df2['date'] = df1['date'].values
#df2['hour'] = df1['hour'].values

df=df.rename(columns = {'date':'Date'})

df=df.rename(columns = {'bidclose':'Close'})
df=df.rename(columns = {'bidhigh':'High'})
df=df.rename(columns = {'bidlow':'Low'})
df=df.rename(columns = {'bidopen':'Open'})
df=df.rename(columns = {'tickqty':'Volume'})


#df = pd.DataFrame({'xxx': days,})
#df['DOB1'] = df['xxx'].dt.strftime('%Y-%m-%d')


del df['Date']
del df['askopen']
del df['askclose']
del df['askhigh']
del df['asklow']

#f.insert(2, "Age", days)
date_today = datetime.now()

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'Date': days,})
df['Date'] = df2['Date'].dt.strftime('%Y-%m-%d')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['Date', 'Open', 'Close', 'High', 'Low', 'Volume']]
#df = df.set_index('Date')

#df = df.set_index('DOB1')
#print(df)


#del df['Date']
#df['Date'] = [x[:-22] for x in df['Date']]

#df.index=pd.to_datetime(df["Date"])
#df=df.drop("Date",axis=1)


#dfm=df.resample("M").mean()

#dfm=dfm[:-1] # As we said, we do not consider the month of end_date
df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/validated/nzdcadH_val.csv')
print(df.tail(10))


##########

###########



df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/nzdchfH_raw.csv",)


#f = (columns=['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty'])



#df2['date'] = df1['date'].values
#df2['hour'] = df1['hour'].values

df=df.rename(columns = {'date':'Date'})

df=df.rename(columns = {'bidclose':'Close'})
df=df.rename(columns = {'bidhigh':'High'})
df=df.rename(columns = {'bidlow':'Low'})
df=df.rename(columns = {'bidopen':'Open'})
df=df.rename(columns = {'tickqty':'Volume'})


#df = pd.DataFrame({'xxx': days,})
#df['DOB1'] = df['xxx'].dt.strftime('%Y-%m-%d')


del df['Date']
del df['askopen']
del df['askclose']
del df['askhigh']
del df['asklow']

#f.insert(2, "Age", days)
date_today = datetime.now()

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'Date': days,})
df['Date'] = df2['Date'].dt.strftime('%Y-%m-%d')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['Date', 'Open', 'Close', 'High', 'Low', 'Volume']]
#df = df.set_index('Date')

#df = df.set_index('DOB1')
#print(df)


#del df['Date']
#df['Date'] = [x[:-22] for x in df['Date']]

#df.index=pd.to_datetime(df["Date"])
#df=df.drop("Date",axis=1)


#dfm=df.resample("M").mean()

#dfm=dfm[:-1] # As we said, we do not consider the month of end_date
df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/validated/nzdchfH_val.csv')
print(df.tail(10))


##########

###########



df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/nzdusdH_raw.csv",)


#f = (columns=['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty'])



#df2['date'] = df1['date'].values
#df2['hour'] = df1['hour'].values

df=df.rename(columns = {'date':'Date'})

df=df.rename(columns = {'bidclose':'Close'})
df=df.rename(columns = {'bidhigh':'High'})
df=df.rename(columns = {'bidlow':'Low'})
df=df.rename(columns = {'bidopen':'Open'})
df=df.rename(columns = {'tickqty':'Volume'})


#df = pd.DataFrame({'xxx': days,})
#df['DOB1'] = df['xxx'].dt.strftime('%Y-%m-%d')


del df['Date']
del df['askopen']
del df['askclose']
del df['askhigh']
del df['asklow']

#f.insert(2, "Age", days)
date_today = datetime.now()

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'Date': days,})
df['Date'] = df2['Date'].dt.strftime('%Y-%m-%d')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['Date', 'Open', 'Close', 'High', 'Low', 'Volume']]
#df = df.set_index('Date')

#df = df.set_index('DOB1')
#print(df)


#del df['Date']
#df['Date'] = [x[:-22] for x in df['Date']]

#df.index=pd.to_datetime(df["Date"])
#df=df.drop("Date",axis=1)


#dfm=df.resample("M").mean()

#dfm=dfm[:-1] # As we said, we do not consider the month of end_date
df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/validated/nzdusdH_val.csv')
print(df.tail(10))


##########

###########



df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/usdtryH_raw.csv",)


#f = (columns=['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty'])



#df2['date'] = df1['date'].values
#df2['hour'] = df1['hour'].values

df=df.rename(columns = {'date':'Date'})

df=df.rename(columns = {'bidclose':'Close'})
df=df.rename(columns = {'bidhigh':'High'})
df=df.rename(columns = {'bidlow':'Low'})
df=df.rename(columns = {'bidopen':'Open'})
df=df.rename(columns = {'tickqty':'Volume'})


#df = pd.DataFrame({'xxx': days,})
#df['DOB1'] = df['xxx'].dt.strftime('%Y-%m-%d')


del df['Date']
del df['askopen']
del df['askclose']
del df['askhigh']
del df['asklow']

#f.insert(2, "Age", days)
date_today = datetime.now()

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'Date': days,})
df['Date'] = df2['Date'].dt.strftime('%Y-%m-%d')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['Date', 'Open', 'Close', 'High', 'Low', 'Volume']]
#df = df.set_index('Date')

#df = df.set_index('DOB1')
#print(df)


#del df['Date']
#df['Date'] = [x[:-22] for x in df['Date']]

#df.index=pd.to_datetime(df["Date"])
#df=df.drop("Date",axis=1)


#dfm=df.resample("M").mean()

#dfm=dfm[:-1] # As we said, we do not consider the month of end_date
df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/validated/usdtryH_val.csv')
print(df.tail(10))


##########
###########



df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/usdzarH_raw.csv",)


#f = (columns=['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty'])



#df2['date'] = df1['date'].values
#df2['hour'] = df1['hour'].values

df=df.rename(columns = {'date':'Date'})

df=df.rename(columns = {'bidclose':'Close'})
df=df.rename(columns = {'bidhigh':'High'})
df=df.rename(columns = {'bidlow':'Low'})
df=df.rename(columns = {'bidopen':'Open'})
df=df.rename(columns = {'tickqty':'Volume'})


#df = pd.DataFrame({'xxx': days,})
#df['DOB1'] = df['xxx'].dt.strftime('%Y-%m-%d')


del df['Date']
del df['askopen']
del df['askclose']
del df['askhigh']
del df['asklow']

#f.insert(2, "Age", days)
date_today = datetime.now()

days = pd.date_range(date_today, date_today + timedelta(4000),freq='D')

df2 = pd.DataFrame({'Date': days,})
df['Date'] = df2['Date'].dt.strftime('%Y-%m-%d')
#df.insert(1, "date", days)
#df = df.set_index('date')

df = df[['Date', 'Open', 'Close', 'High', 'Low', 'Volume']]
#df = df.set_index('Date')

#df = df.set_index('DOB1')
#print(df)


#del df['Date']
#df['Date'] = [x[:-22] for x in df['Date']]

#df.index=pd.to_datetime(df["Date"])
#df=df.drop("Date",axis=1)


#dfm=df.resample("M").mean()

#dfm=dfm[:-1] # As we said, we do not consider the month of end_date
df.to_csv(r'C:/xampp/htdocs/nasiasense/resamplersH/validated/usdzarH_val.csv')
print(df.tail(10))


##########
