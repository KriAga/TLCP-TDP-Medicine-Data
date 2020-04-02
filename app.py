import json

from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/medicine_details', methods=['POST'])
def medicine_details():
   if request.method == 'POST':
      medicine = request.json['name']
      data = json.load(open('SimpleDescMedicineData.json', 'r'))
      return data[medicine]


if __name__ == '__main__':
   app.run(debug=True)