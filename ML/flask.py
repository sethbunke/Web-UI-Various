#https://www.safaribooksonline.com/library/view/intelligent-iot-projects/9781787286429/58ee437d-0d3a-453d-8110-6df635866433.xhtml
from flask import Flask 
app = Flask(__name__) 
 
@app.route("/") 
def hello(): 
    return "Hello,Flask!" 
 
@app.route('/ads/<int:ads_id>') 
def show_post(ads_id):     
    return 'Adversiting id %d' % ads_id 

