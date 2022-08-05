from crypt import methods
from flask import Flask, render_template,request,make_response
from flask_cors import CORS
from mosaic_demo import main

app = Flask(__name__)
# CORS(app)
 
@app.route('/')
def fnc_a():
    return render_template("index.html")
 
 
@app.route('/api',methods=['POST'])
def api():
    if request.method == 'POST':
        data = request.json
        data = main(data)
    return data
 
@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

if __name__ == '__main__':
    app.run()