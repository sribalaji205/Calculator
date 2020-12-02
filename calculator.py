from flask import Flask,url_for,render_template,redirect,request
from threading import Timer
import webbrowser
import  math
import math

def enum1(res):
      str1="+-/%x^√"
      g=(index for index,char in enumerate(res) if char in str1)
      n=next(g)
      return n

def checking(res):
      for index,char in enumerate(res):
            str1="0123456789."
            if(char in str1):
                  res=res
            else:
                  res="b"
      return res

def check(res):
      res=res+"+1+1"
      res=list(res)
      str1="+-/%x^√"
      g=(index for index,char in enumerate(res) if char in str1)
      n=next(g)
      l=res[n]
      char=res[n+1]
      str2="/x^%"
      if(char in str2):
            res="ERROR"
      return(res)


def checksqrt(res):
      res="+111+"+res+"1+1"
      for index,char in enumerate(res):
            if (char=="√"):
                  n=index
                  char=res[n-1]
                  str1="0123456789."
                  if(char in str1):
                        res="ERROR"
      return res


def checkdivbyzero(res):
      res=res+"1+1"
      for index,char in enumerate(res) :
            if (char=="/"):
                n=index
                if(res[n+1]=="0"):
                      if(res[n+2]!="."):
                            res="ERROR"
      return(res)

def checkzero(res):
      res="+"+res+"+11"
      res=list(res)
      str1="+-/x^%.√"
      g=(index for index,char in enumerate(res) if char in str1)
      n=next(g)
      l=res[n]
      char=res[n+1]
      if(char=="0"):
            str2="123456789"
            if(res[n+2] in str2):
                  res="ERROR"
      return res

def start(res):
      res=list(res)
      char=res[0]
      str1="/%^x"
      if(char in str1):
            res="ERROR"
      return res
def repeatdot(res):
      global d,resu,count 
      res="+"+res+"111"
      res=list(res)
      ab=len(res)
      str1=""
      resu=[]
      str1="+-/%x^√"
      g=(index for index,char in enumerate(res) if char in str1)
      n=next(g)
      m=res[n+1:ab]
      g=enum1(m)
      resu=res[n+1:n+1+g]
      count=0
      for index,char in enumerate(resu):
            if(char=="."):
                  count+=1
      if(count>1):
            resu="ERROR"
      return resu

def squareroot(res):
      global d
      res=res+"+11+"
      res=list(res)
      ab=len(res)
      str1=""
      rep=""
      for index,char in enumerate(res):
            if(char=="√"):
                  n=index+1
                  m=res[n:ab]
                  g=enum1(m)
                  d=n+g
                  res.insert(d,")")
                  resu=str1.join(res)
                  resu=resu[0:-4]
      return resu
app = Flask(__name__)

@app.route("/")
def home():
      return render_template("load.html")
@app.route("/calculate",methods=["GET","POST"])
def calculate():
      global value, text,res
      
      if(request.method=="POST"):
            value=request.form.get("code")
            text=request.form.get("textbox")
            str1='+-x/%^√9876543210.'
            if(value in str1):
                  if(text=="ERROR CHECK AGAIN"):
                        text=""
                  res=text+value
                  
            elif(value=="="and checking(text)==text):
                  res=text 
                  
            elif(value =="="):
                  string="+-/x^%.√"
                  a="ERROR"
                  if(checkzero(text)==a or start(text)==a or text[-1] in string or
                     check(text)==a or checkdivbyzero(text)==a or repeatdot(text)==a or
                     checksqrt(text)==a):
                        res="ERROR CHECK AGAIN"
                  
                  else:
                        if(text.find("√")!=-1):
                              text=squareroot(text)
                              text=text.replace('√','math.sqrt(')
                        if(text.find("^")!=-1):
                              text=text.replace("^","**")
                        if(text.find("x")!=-1):
                              text=text.replace("x","*")
                        res=eval(text)
                        
            elif(value=="DEL"):
                  res=text[0:-1]
            elif(value=="C"):
                  res=""
            else:
                  res=eval(text)  
            
      return render_template("load.html",tot=res)


def open_browser():
      webbrowser.open_new('http://127.0.0.1:2000/')
      
if __name__ == "__main__":
      Timer(1,open_browser).start();
      app.run(port=2000)
