from flask import Flask

import urllib.request


with urllib.request.urlopen("http://127.0.0.2/files/audcad.csv") as url:
    y = url.read().decode('utf-8')
         
    u = int(y)     
if u == 0:
    orderaudcad = "sell"
    #print(sel)
if u > 0:        
    orderaudcad = "buy"
########################################################
with urllib.request.urlopen("http://127.0.0.2/files/audchf.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    orderaudchf = "sell"
    #print(sel)
if i > 0:        
    orderaudchf = "buy"
#########################################################
with urllib.request.urlopen("http://127.0.0.2/files/audjpy.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    orderaudjpy = "sell"
    #print(sel)
if i > 0:        
    orderaudjpy = "buy"
############################

with urllib.request.urlopen("http://127.0.0.2/files/audnzd.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    orderaudnzd = "sell"
    #print(sel)
if i > 0:        
    orderaudnzd = "buy"
############################
with urllib.request.urlopen("http://127.0.0.2/files/audusd.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    orderaudusd = "sell"
    #print(sel)
if i > 0:        
    orderaudusd = "buy"
############################

with urllib.request.urlopen("http://127.0.0.2/files/cadchf.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    ordercadchf = "sell"
    #print(sel)
if i > 0:        
    ordercadchf = "buy"
###############################
with urllib.request.urlopen("http://127.0.0.2/files/cadjpy.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    ordercadjpy = "sell"
    #print(sel)
if i > 0:        
    ordercadjpy = "buy"
###############################
with urllib.request.urlopen("http://127.0.0.2/files/chfjpy.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    orderchfjpy = "sell"
    #print(sel)
if i > 0:        
    orderchfjpy = "buy"
#######################################
with urllib.request.urlopen("http://127.0.0.2/files/euraud.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    ordereuraud = "sell"
    #print(sel)
if i > 0:        
    ordereuraud = "buy"
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
with urllib.request.urlopen("http://127.0.0.2/files/eurchf.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    ordereurchf = "sell"
    #print(sel)
if i > 0:        
    ordereurchf = "buy"
###############################

with urllib.request.urlopen("http://127.0.0.2/files/eurgbp.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    ordereurgbp = "sell"
    #print(sel)
if i > 0:        
    ordereurgbp = "buy"
##################################
with urllib.request.urlopen("http://127.0.0.2/files/eurjpy.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    ordereurjpy = "sell"
    #print(sel)
if i > 0:        
    ordereurjpy = "buy"
################################

##################################
with urllib.request.urlopen("http://127.0.0.2/files/eurnzd.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    ordereurnzd = "sell"
    #print(sel)
if i > 0:        
    ordereurnzd = "buy"
################################
##################################
with urllib.request.urlopen("http://127.0.0.2/files/eurusd.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    ordereurusd = "sell"
    #print(sel)
if i > 0:        
    ordereurusd = "buy"
################################
##################################
with urllib.request.urlopen("http://127.0.0.2/files/gbpaud.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    ordergbpaud = "sell"
    #print(sel)
if i > 0:        
    ordergbpaud = "buy"
################################
##################################
with urllib.request.urlopen("http://127.0.0.2/files/gbpcad.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    ordergbpcad = "sell"
    #print(sel)
if i > 0:        
    ordergbpcad = "buy"
################################

##################################
with urllib.request.urlopen("http://127.0.0.2/files/gbpchf.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    ordergbpchf = "sell"
    #print(sel)
if i > 0:        
    ordergbpchf = "buy"
################################
##################################
with urllib.request.urlopen("http://127.0.0.2/files/gbpjpy.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    ordergbpjpy = "sell"
    #print(sel)
if i > 0:        
    ordergbpjpy = "buy"
################################
##################################
with urllib.request.urlopen("http://127.0.0.2/files/gbpnzd.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    ordergbpnzd = "sell"
    #print(sel)
if i > 0:        
    ordergbpnzd = "buy"
################################

##################################
with urllib.request.urlopen("http://127.0.0.2/files/gbpusd.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    ordergbpusd = "sell"
    #print(sel)
if i > 0:        
    ordergbpusd = "buy"
################################
##################################
with urllib.request.urlopen("http://127.0.0.2/files/nzdcad.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    ordernzdcad = "sell"
    #print(sel)
if i > 0:        
    ordernzdcad = "buy"
################################
##################################
with urllib.request.urlopen("http://127.0.0.2/files/nzdchf.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    ordernzdchf = "sell"
    #print(sel)
if i > 0:        
    ordernzdchf = "buy"
################################

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

##################################
with urllib.request.urlopen("http://127.0.0.2/files/nzdusd.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    ordernzdusd = "sell"
    #print(sel)
if i > 0:        
    ordernzdusd = "buy"
################################

##################################
with urllib.request.urlopen("http://127.0.0.2/files/usdcad.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    orderusdcad = "sell"
    #print(sel)
if i > 0:        
    orderusdcad = "buy"
################################


##################################
with urllib.request.urlopen("http://127.0.0.2/files/usdchf.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    orderusdchf = "sell"
    #print(sel)
if i > 0:        
    orderusdchf = "buy"
################################

##################################
with urllib.request.urlopen("http://127.0.0.2/files/usdjpy.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    orderusdjpy = "sell"
    #print(sel)
if i > 0:        
    orderusdjpy = "buy"
################################
##################################
with urllib.request.urlopen("http://127.0.0.2/files/usdtry.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    orderusdtry = "sell"
    #print(sel)
if i > 0:        
    orderusdtry = "buy"
##################################################################
with urllib.request.urlopen("http://127.0.0.2/files/usdzar.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    orderusdzar = "sell"
    #print(sel)
if i > 0:        
    orderusdzar = "buy"
################################


##################################
with urllib.request.urlopen("http://127.0.0.2/files/xagusd.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    orderxagusd = "sell"
    #print(sel)
if i > 0:        
    orderxagusd = "buy"
##################################################################
with urllib.request.urlopen("http://127.0.0.2/files/xauusd.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    orderxauusd= "sell"
    #print(sel)
if i > 0:        
    orderxauusd = "buy"
################################
app = Flask(__name__)

@app.route("/")
def home():
    return "C4R4NCIA_CAPITAL"
    

@app.route("/audcad")
def audcad():
    return (orderaudcad)    

@app.route("/audchf")
def audchf():
    return (orderaudchf)

@app.route("/audjpy")
def audjpy():
    return (orderaudjpy)  


@app.route("/audnzd")
def audnzd():
    return (orderaudnzd)   


@app.route("/audusd")
def audusd():
    return (orderaudusd) 

@app.route("/cadchf")
def cadchf():
    return (ordercadchf)  

@app.route("/cadjpy")
def cadjpy():
    return (ordercadjpy)      

    
@app.route("/chfjpy")
def chfjpy():
    return (orderchfjpy)  

@app.route("/euraud")
def euraud():
    return (ordereuraud) 

@app.route("/eurcad")
def eurcad():
    return (ordereurcad)  

@app.route("/eurchf")
def eurchf():
    return (ordereurchf)      


@app.route("/eurgbp")
def eurgbp():
    return (ordereurgbp)  


@app.route("/eurjpy")
def eurjpy():
    return (ordereurjpy)  



@app.route("/eurnzd")
def eurnzd():
    return (ordereurnzd)    

@app.route("/eurusd")
def eurusd():
    return (ordereurusd)    

@app.route("/gbpaud")
def gbpaud():
    return (ordergbpaud)   


@app.route("/gbpcad")
def gbpcad():
    return (ordergbpcad)    

@app.route("/gbpchf")
def gbpchf():
    return (ordergbpchf)    

@app.route("/gbpjpy")
def gbpjpy():
    return (ordergbpjpy)    
 

@app.route("/gbpnzd")
def gbpnzd():
    return (ordergbpnzd)    

@app.route("/gbpusd")
def gbpusd():
    return (ordergbpusd)    

@app.route("/nzdcad")
def nzdcad():
    return (ordernzdcad)    

@app.route("/nzdchf")
def nzdchf():
    return (ordernzdchf)    

@app.route("/nzdjpy")
def nzdjpy():
    return (ordernzdjpy)    

@app.route("/nzdusd")
def nzdusd():
    return (ordernzdusd)    


@app.route("/usdcad")
def usdcad():
    return (orderusdcad)    

@app.route("/usdchf")
def usdchf():
    return (orderusdchf)    

@app.route("/usdjpy")
def usdjpy():
    return (orderusdjpy)    



@app.route("/usdtry")
def usdtry():
    return (orderusdtry)    

@app.route("/usdzar")
def usdzar():
    return (orderusdzar)    



@app.route("/xagusd")
def xagusd():
    return (orderxagusd)    

@app.route("/xauusd")
def xauusd():
    return (orderxauusd)    





if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80, debug=True) 