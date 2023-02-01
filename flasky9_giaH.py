from flask import Flask

import urllib.request

########################################################
with urllib.request.urlopen("http://127.0.0.2/nasiasense/hist/h/h_phase2/audchfH_phasethree.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    orderaudchf = "sell"
    #print(sel)
if i > 0:        
    orderaudchf = "buy"
#########################################################

############################

###############################
with urllib.request.urlopen("http://127.0.0.2/nasiasense/hist/h/h_phase2/chfjpyH_phasethree.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    orderchfjpy = "sell"
    #print(sel)
if i > 0:        
    orderchfjpy = "buy"

with urllib.request.urlopen("http://127.0.0.2/nasiasense/hist/h/h_phase2/eurcadH_phasethree.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    ordereurcad = "sell"
    #print(sel)
if i > 0:        
    ordereurcad = "buy"
####################################
with urllib.request.urlopen("http://127.0.0.2/nasiasense/hist/h/h_phase2/eurchfH_phasethree.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    ordereurchf = "sell"
    #print(sel)
if i > 0:        
    ordereurchf = "buy"
###############################

with urllib.request.urlopen("http://127.0.0.2/nasiasense/hist/h/h_phase2/eurjpyH_phasethree.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    ordereurjpy = "sell"
    #print(sel)
if i > 0:        
    ordereurjpy = "buy"
################################

#################################
with urllib.request.urlopen("http://127.0.0.2/nasiasense/hist/h/h_phase2/eurusdH_phasethree.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    ordereurusd = "sell"
    #print(sel)
if i > 0:        
    ordereurusd = "buy"
################################
####
################################
#
##################################
with urllib.request.urlopen("http://127.0.0.2/nasiasense/hist/h/h_phase2/gbpchfH_phasethree.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    ordergbpchf = "sell"
    #print(sel)
if i > 0:        
    ordergbpchf = "buy"
################################
##################################
with urllib.request.urlopen("http://127.0.0.2/nasiasense/hist/h/h_phase2/gbpjpyH_phasethree.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    ordergbpjpy = "sell"
    #print(sel)
if i > 0:        
    ordergbpjpy = "buy"
################################
##

##################################
with urllib.request.urlopen("http://127.0.0.2/nasiasense/hist/h/h_phase2/gbpusdH_phasethree.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    ordergbpusd = "sell"
    #print(sel)
if i > 0:        
    ordergbpusd = "buy"
################################
##
################################
##################################
with urllib.request.urlopen("http://127.0.0.2/nasiasense/hist/h/h_phase2/nzdchfH_phasethree.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    ordernzdchf = "sell"
    #print(sel)
if i > 0:        
    ordernzdchf = "buy"
################################

##################################
with urllib.request.urlopen("http://127.0.0.2/nasiasense/hist/h/h_phase2/nzdjpyH_phasethree.csv") as url:
    x = url.read().decode('utf-8')
         
    i = int(x)     
if i == 0:
    ordernzdjpy = "sell"
    #print(sel)
if i > 0:        
    ordernzdjpy = "buy"
################################

#####


##################################

app = Flask(__name__)

@app.route("/")
def home():
    return "C4R4NCIA_CAPITAL"
   
@app.route("/audchf")
def audchf():
    return (orderaudchf)

    
@app.route("/chfjpy")
def chfjpy():
    return (orderchfjpy)  

@app.route("/eurcad")
def eurcad():
    return (ordereurcad)  

@app.route("/eurchf")
def eurchf():
    return (ordereurchf)      


@app.route("/eurjpy")
def eurjpy():
    return (ordereurjpy)  



@app.route("/eurusd")
def eurusd():
    return (ordereurusd)    

@app.route("/gbpchf")
def gbpchf():
    return (ordergbpchf)    

@app.route("/gbpjpy")
def gbpjpy():
    return (ordergbpjpy)    
 
@app.route("/gbpusd")
def gbpusd():
    return (ordergbpusd)    

@app.route("/nzdchf")
def nzdchf():
    return (ordernzdchf)    

@app.route("/nzdjpy")
def nzdjpy():
    return (ordernzdjpy)    



@app.route("/usdjpy")
def usdjpy():
    return (orderusdjpy)    




if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80, debug=True) 