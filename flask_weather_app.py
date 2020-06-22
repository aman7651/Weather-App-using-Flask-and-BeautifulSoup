from flask import Flask,request,render_template
import requests
from bs4 import BeautifulSoup
#import requests, time, smtplib
from datetime import datetime
from send_email import send_email
app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def home():
    if request.method == 'POST':
        url = request.form.get('URL')
        sender_email = request.form.get('Email')
        desired_price = request.form.get('Desired_price')
        page1 = requests.get(url).text
        soup = BeautifulSoup(page1, 'lxml')
    

        product_name = soup.find('h1').text.strip()
        page = requests.get(url)
        
        soup = BeautifulSoup(page.content,'html.parser')
        
        price = soup.find("div", {"class": "_3qQ9m1"}).text
        price = price[1:]
    
    
        price_ar = price.split(",")
        price = ''.join(price_ar)
    
        price = int(price)
        desired_price =int(desired_price)

        if desired_price >= price:
              send_mail()

        
        return render_template("flask_weather_app.html", price=price,product_name=product_name )
    return render_template("flask_weather_app.html")

app.run(debug=True)
