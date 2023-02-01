from __future__ import division
import pandas as pd
import numpy as np
import datetime
import time
import matplotlib.pyplot as plt

import keras
from keras.models import Sequential
from keras.layers import Dense,Dropout,BatchNormalization,Conv1D,Flatten,MaxPooling1D,LSTM
from keras.callbacks import EarlyStopping,ModelCheckpoint,TensorBoard
from keras.wrappers.scikit_learn import KerasRegressor
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

######getstartday
arxhdate=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/xagusdH_raw.csv")
pd.to_datetime(arxhdate['date'],format='%Y-%m-%d %H:%M:%S')


arxhdate['date'] = [x[8:11] for x in arxhdate['date']]

arxhday=arxhdate['date'].iloc[0]

arxhdayt=(int(arxhday))
######getstartmonth

arxhmonth=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/xagusdH_raw.csv")
pd.to_datetime(arxhmonth['date'],format='%Y-%m-%d %H:%M:%S')


arxhmonth['date'] = [x[5:7] for x in arxhmonth['date']]
arxhmonth1=arxhmonth['date'].iloc[0]
arxhmonth2=(int(arxhmonth1))
#################getstartyear

arxhyear=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/xagusdH_raw.csv")
pd.to_datetime(arxhyear['date'],format='%Y-%m-%d %H:%M:%S')


arxhyear['date'] = [x[:-15] for x in arxhyear['date']]

arxhyear1=arxhyear['date'].iloc[0]

arxhyear2=(int(arxhyear1))
####getelosday
telosdate=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/xagusdH_raw.csv")
pd.to_datetime(telosdate['date'],format='%Y-%m-%d %H:%M:%S')


telosdate['date'] = [x[8:11] for x in telosdate['date']]

telosday1=telosdate['date'].iloc[-1]
telosday2=(int(telosday1))
#gettelosmonth
telosmonth=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/xagusdH_raw.csv")
pd.to_datetime(telosmonth['date'],format='%Y-%m-%d %H:%M:%S')


telosmonth['date'] = [x[5:7] for x in telosmonth['date']]
telosmonth1=telosmonth['date'].iloc[-1]
telosmonth2=(int(telosmonth1))
####telosyear
telosyear=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/data_preparation/xagusdH_raw.csv")
pd.to_datetime(telosyear['date'],format='%Y-%m-%d %H:%M:%S')


telosyear['date'] = [x[:-15] for x in telosyear['date']]

telosyear1=telosyear['date'].iloc[-1]

telosyear2=(int(telosyear1))
######





start_date=datetime.datetime(arxhyear2, arxhmonth2, arxhdayt)
end_date=datetime.datetime(telosyear2,telosmonth2,telosday2)


df=pd.read_csv(r"C:/xampp/htdocs/nasiasense/resamplersH/validated/xagusdH_val.csv")
#df=df.rename(columns = {'time':'Date'})

df.index=pd.to_datetime(df["Date"])

df=df.drop("Date",axis=1)


dfm=df.resample("M").mean()

dfm=dfm[:-1] # As we said, we do not consider the month of end_date

print(dfm.head())
print(dfm.tail())

start_year=start_date.year
start_month=start_date.month
end_year=end_date.year
end_month=end_date.month

first_days=[]
# First year
for month in range(start_month,13):
    first_days.append(min(df[str(start_year)+"-"+str(month)].index))
# Other years
for year in range(start_year+1,end_year):
    for month in range(1,13):
        first_days.append(min(df[str(year)+"-"+str(month)].index))
# Last year
for month in range(1,end_month+1):
    first_days.append(min(df[str(end_year)+"-"+str(month)].index))
    
dfm["fd_cm"]=first_days[:-1]
dfm["fd_nm"]=first_days[1:]
dfm["fd_cm_open"]=np.array(df.loc[first_days[:-1],"Open"])
dfm["fd_nm_open"]=np.array(df.loc[first_days[1:],"Open"])
dfm["rapp"]=dfm["fd_nm_open"].divide(dfm["fd_cm_open"])

print(dfm.head())
print(dfm.tail())

dfm["mv_avg_12"]= dfm["Open"].rolling(window=12).mean().shift(1)
dfm["mv_avg_24"]= dfm["Open"].rolling(window=24).mean().shift(1)


dfm=dfm.iloc[24:,:] # WARNING: DO IT JUST ONE TIME!
print(dfm.index)

mtest=72
train=dfm.iloc[:-mtest,:] 
test=dfm.iloc[-mtest:,:]

# This function returns the total percentage gross yield and the annual percentage gross yield

def yield_gross(df,v):
    prod=(v*df["rapp"]+1-v).prod()
    n_years=len(v)/12
    return (prod-1)*100,((prod**(1/n_years))-1)*100

tax_cg=0.26
comm_bk=0.001

# This function will be used in the function yield_net

# Given any vector v of ones and zeros, this function gives the corresponding vectors of "islands" of ones of v
# and their number. 
# For example, given v = [0,1,1,0,1,0,1], expand_islands2D gives
# out2D = [[0,1,1,0,0,0,0],[0,0,0,0,1,0,0],[0,0,0,0,0,0,1]] and N=3

def expand_islands2D(v):
    
    # Get start, stop of 1s islands
    v1 = np.r_[0,v,0]
    idx = np.flatnonzero(v1[:-1] != v1[1:])
    s0,s1 = idx[::2],idx[1::2]
    if len(s0)==0:
        return np.zeros(len(v)),0
    
    # Initialize 1D id array  of size same as expected o/p and has 
    # starts and stops assigned as 1s and -1s, so that a final cumsum
    # gives us the desired o/p
    N,M = len(s0),len(v)
    out = np.zeros(N*M,dtype=int)

    # Setup starts with 1s
    r = np.arange(N)*M
    out[s0+r] = 1


    # Setup stops with -1s
    if s1[-1] == M:
        out[s1[:-1]+r[:-1]] = -1
    else:
        out[s1+r] -= 1

    # Final cumsum on ID array
    out2D = out.cumsum().reshape(N,-1)
    return out2D,N


    # This function returns the total percentage net yield and the annual percentage net yield

def yield_net(df,v):
    n_years=len(v)/12
    
    w,n=expand_islands2D(v)
    A=(w*np.array(df["rapp"])+(1-w)).prod(axis=1)  # A is the product of each island of ones of 1 for df["rapp"]
    A1p=np.maximum(0,np.sign(A-1)) # vector of ones where the corresponding element if  A  is > 1, other are 0
    Ap=A*A1p # vector of elements of A > 1, other are 0
    Am=A-Ap # vector of elements of A <= 1, other are 0
    An=Am+(Ap-A1p)*(1-tax_cg)+A1p
    prod=An.prod()*((1-comm_bk)**(2*n)) 
    
    return (prod-1)*100,((prod**(1/n_years))-1)*100

def create_window(data, window_size = 1):    
    data_s = data.copy()
    for i in range(window_size):
        data = pd.concat([data, data_s.shift(-(i + 1))], axis = 1)
        
    data.dropna(axis=0, inplace=True)
    return(data)
scaler=MinMaxScaler(feature_range=(0,1))
dg=pd.DataFrame(scaler.fit_transform(dfm[["High","Low","Open","Close","Volume","fd_cm_open",\
                                          "mv_avg_12","mv_avg_24","fd_nm_open"]].values))
dg0=dg[[0,1,2,3,4,5,6,7]]


window=4
dfw=create_window(dg0,window)

X_dfw=np.reshape(dfw.values,(dfw.shape[0],window+1,8))
print(X_dfw.shape)
print(dfw.iloc[:4,:])
print(X_dfw[0,:,:])

y_dfw=np.array(dg[8][window:])

X_trainw=X_dfw[:-mtest-1,:,:]
X_testw=X_dfw[-mtest-1:,:,:]
y_trainw=y_dfw[:-mtest-1]
y_testw=y_dfw[-mtest-1:]    

def model_lstm(window,features):
    
    model=Sequential()
    model.add(LSTM(300, input_shape = (window,features), return_sequences=True))
    model.add(Dropout(0.5))
    model.add(LSTM(200, input_shape=(window,features), return_sequences=False))
    model.add(Dropout(0.5))
    model.add(Dense(100,kernel_initializer='uniform',activation='relu'))        
    model.add(Dense(1,kernel_initializer='uniform',activation='relu'))
    model.compile(loss='mse',optimizer='adam')
    
    
    return model


model=model_lstm(window+1,8)
history=model.fit(X_trainw,y_trainw,epochs=300, batch_size=24, validation_data=(X_testw, y_testw), \
                  verbose=0, callbacks=[],shuffle=False)

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper right')
plt.show()    

y_pr=model.predict(X_trainw)

plt.figure(figsize=(30,10))
plt.plot(y_trainw, label="actual")
plt.plot(y_pr, label="prediction")
plt.legend(fontsize=20)
plt.grid(axis="both")
plt.title("Actual open price and pedicted one on train set",fontsize=25)
plt.show()


y_pred=model.predict(X_testw)


v=np.diff(y_pred.reshape(y_pred.shape[0]),1)
v_lstm=np.maximum(np.sign(v),0)


plt.figure(figsize=(30,10))
plt.plot(y_testw, label="actual")
plt.plot(y_pred, label="prediction")
plt.plot(v_lstm,label="In and out")
plt.legend(fontsize=20)
plt.grid(axis="both")
plt.title("Actual open price, predicted one and vector v_lstm",fontsize=25)
plt.show()


v_bh=np.ones(test.shape[0])
v_ma=test["fd_cm_open"]>test["mv_avg_12"]

def gross_portfolio(df,w):
    portfolio=[ (w*df["rapp"]+(1-w))[:i].prod() for i in range(len(w))]
    return portfolio

plt.figure(figsize=(30,10))
plt.plot(gross_portfolio(test,v_bh),label="Portfolio Buy and Hold")
plt.plot(gross_portfolio(test,v_ma),label="Portfolio Moving Average")
plt.plot(gross_portfolio(test,v_lstm),label="Portfolio LSTM")
plt.legend(fontsize=20)
plt.grid(axis="both")
plt.title("Gross portfolios of three methods", fontsize=25)
plt.show()


print("Test period of {:.2f} years, from {} to {} \n".format(len(v_bh)/12,str(test.loc[test.index[0],"fd_cm"])[:10],\
      str(test.loc[test.index[-1],"fd_nm"])[:10]))

results0=pd.DataFrame({})
results1=pd.DataFrame({})
results2=pd.DataFrame({})
results3=pd.DataFrame({})

results0["Method"]=["Buy and hold","Moving average","LSTM"]
results1["Method"]=["Buy and hold","Moving average","LSTM"]
results2["Method"]=["Buy and hold","Moving average","LSTM"]
results3["Method"]=["Buy and hold","Moving average","LSTM"]

vs=[v_bh,v_ma,v_lstm]
results0["Total gross yield"]=[str(round(yield_gross(test,vi)[0],2))+" %" for vi in vs]
results1["Annual gross yield"]=[str(round(yield_gross(test,vi)[1],2))+" %" for vi in vs]
results2["Total net yield"]=[str(round(yield_net(test,vi)[0],2))+" %" for vi in vs]
results3["Annual net yield"]=[str(round(yield_net(test,vi)[1],2))+" %" for vi in vs]

print(results0)
print("\n")
print(results1)
print("\n")
print(results2)
print("\n")
print(results3)

print((v_lstm))
dd=v_lstm



print(dd)


dd = pd.DataFrame(dd, columns=['g'])

#dd

ee=dd['g'].iloc[-1]
#ee




mystring = str(ee)
mystring

g1 = (mystring[0])
g1
#type(ee)


#g1.to_csv(r'C:/Users/atsal/testcsv/11.csv')

#dd
#x=df['date'].iloc[0]
#x

import csv
from io import StringIO

buffer = StringIO(g1)

reader = csv.reader(buffer, skipinitialspace=True)
with open(r'C:/xampp/htdocs/nasiasense/hist/h/h_phase2/xagusdH_phasethree.csv', 'w') as out_file:
    writer = csv.writer(out_file)
    writer.writerows(reader)