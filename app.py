from flask import Flask, render_template, redirect, jsonify
from flask import request
import requests
from bs4 import BeautifulSoup
import time

app = Flask(__name__)


# Routes
@app.route('/')

def root():
    return redirect('/exchangerate/None')


@app.route('/exchangerate/<string:ticker>', methods=['POST','GET'])

def exchangeRate(ticker):
        
        if request.method == "GET":
            print("ticker:", ticker)
            url = "https://" + "www.google.com/search?q=usd+to+" + ticker 
            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'html5lib')
            table = soup.find('div', attrs={'class':"BNeawe iBp4i AP7Wnd"})
            if table is None:
                return jsonify('Error: The ticker simbol does not exist. Try different ticker')
            content = table.get_text()
            print ("table:", table)
            print("content", table.get_text())
            oneUSD = str()
            for el in content:
                if el == " ":
                    break
                oneUSD += el
            print("oneUSD:", oneUSD)
            return jsonify(float(oneUSD))

# Listener

if __name__ == "__main__":

    #Start the app on port 3000, it will be different once hosted

    app.run(host="localhost", port=3000, debug=True)
