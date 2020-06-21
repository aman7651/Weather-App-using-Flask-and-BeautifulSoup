from flask import Flask,request,render_template
import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as bs
import requests as r
#from datetime import datetime

#import requests, time, smtplib
app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def home():
    if request.method == 'POST':
        url = request.form.get('city_name')
        #url = "https://www.timeanddate.com/weather/india/"+city_name+"/ext"
        r = requests.get(url)
        page1 = r.get(url)
        soup = bs(page1.content, "html.parser")
        price = soup.find("div", {"class": "_3qQ9m1"}).text
        price = price[1:]
        price_ar = price.split(",")
        price = ''.join(price_ar)
        price = int(price)
        #data = r.content
       # soup = BeautifulSoup(data,'html.parser')
       # div = soup.find_all('div',class_='h2')[0].get_text()

        #p = soup.find_all('p')[0].get_text()

        #div_five = soup.find_all('div',class_='five columns')

        #for i in div_five:
            #p_div = i.find_all('p')
           # pressure = p_div[4].get_text()
           # humidity = p_div[5].get_text()
                
        return        render_template("flask_weather_app.html", price =price)

    return render_template("flask_weather_app.html")

app.run(debug=True)
