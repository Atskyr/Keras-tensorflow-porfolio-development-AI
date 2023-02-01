from flask import Flask

import urllib.request


with urllib.request.urlopen("http://127.0.0.2/files/eurusd.csv") as url:
    y = url.read().decode('utf-8')
         
    u = int(y)     
if u == 0:
    ordereurusd = "sell"
    #print(sel)
if u > 0:        
    ordereurusd = "buy"
########################################################
with urllib.request.urlopen("http://127.0.0.2/files/gbpusd.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    ordergbpusd = "sell"
    #print(sel)
if i > 0:        
    ordergbpusd = "buy"
#########################################################
with urllib.request.urlopen("http://127.0.0.2/files/usdchf.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    orderusdchf = "sell"
    #print(sel)
if i > 0:        
    orderusdchf = "buy"
############################

with urllib.request.urlopen("http://127.0.0.2/files/usdjpy.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    orderusdjpy = "sell"
    #print(sel)
if i > 0:        
    orderusdjpy = "buy"
############################
with urllib.request.urlopen("http://127.0.0.2/files/gbpjpy.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    ordergbpjpy = "sell"
    #print(sel)
if i > 0:        
    ordergbpjpy = "buy"
############################

with urllib.request.urlopen("http://127.0.0.2/files/eurchf.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    ordereurchf = "sell"
    #print(sel)
if i > 0:        
    ordereurchf = "buy"
###############################
with urllib.request.urlopen("http://127.0.0.2/files/chfjpy.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    orderchfjpy = "sell"
    #print(sel)
if i > 0:        
    orderchfjpy = "buy"
###############################
with urllib.request.urlopen("http://127.0.0.2/files/eurjpy.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    ordereurjpy = "sell"
    #print(sel)
if i > 0:        
    ordereurjpy = "buy"
#######################################
with urllib.request.urlopen("http://127.0.0.2/files/eurgbp.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    ordereurgbp = "sell"
    #print(sel)
if i > 0:        
    ordereurgbp = "buy"
####################################
with urllib.request.urlopen("http://127.0.0.2/files/eurcad.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    ordereurcad = "sell"
    #print(sel)
if i > 0:        
    ordereurcad = "buy"
####################################
with urllib.request.urlopen("http://127.0.0.2/files/audusd.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    orderaudusd = "sell"
    #print(sel)
if i > 0:        
    orderaudusd = "buy"
###############################

with urllib.request.urlopen("http://127.0.0.2/files/audchf.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    orderaudchf = "sell"
    #print(sel)
if i > 0:        
    orderaudchf = "buy"
##################################
with urllib.request.urlopen("http://127.0.0.2/files/nzdjpy.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    ordernzdjpy = "sell"
    #print(sel)
if i > 0:        
    ordernzdjpy = "buy"
################################



app = Flask(__name__)

@app.route("/")
def home():
    return "C4R4NCIA_CAPITAL"
    

@app.route("/eurusd")
def eurusd():
    return (ordereurusd)    

@app.route("/gbpusd")
def gbpusd():
    return (ordergbpusd)

@app.route("/usdchf")
def usdchf():
    return (orderusdchf)  


@app.route("/usdjpy")
def usdjpy():
    return (orderusdjpy)   


@app.route("/gbpjpy")
def gbpjpy():
    return (ordergbpjpy) 

@app.route("/eurchf")
def eurchf():
    return (ordereurchf)  

@app.route("/chfjpy")
def chfjpy():
    return (orderchfjpy)      

    
@app.route("/eurjpy")
def eurjpy():
    return (ordereurjpy)  

@app.route("/eurgbp")
def eurgbp():
    return (ordereurgbp) 

@app.route("/eurcad")
def eurcad():
    return (ordereurcad)  

@app.route("/audusd")
def audusd():
    return (orderaudusd)      


@app.route("/audchf")
def audchf():
    return (orderaudchf)  


@app.route("/nzdjpy")
def nzdjpy():
    return (ordernzdjpy)  

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80, debug=True) 