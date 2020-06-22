from flask import Flask,request,render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def home():
    if request.method == 'POST':
        url = request.form.get('URL')
        
        #url = "https://www.timeanddate.com/weather/india/"+city_name+"/ext"
        page = requests.get(url).text
        soup = BeautifulSoup(page.content,'html.parser')
        
    # print(soup.prettify())

        product_name = soup.find('h1').text.strip()
        page = requests.get(url)
        
      
        price = soup.find("div", {"class": "_3qQ9m1"}).text
        price = price[1:]
    
    # This is used to remove the , in between the prices to make it a number
        price_ar = price.split(",")
        price = ''.join(price_ar)
    
    # Conver the price which is string to an integer to compare
        price = int(price)
    

        
        return render_template("flask_weather_app.html", price=price,product_name=product_name )
    return render_template("flask_weather_app.html")

app.run(debug=True)
