from flask import Flask, jsonify, request
from selenium import webdriver
from scrapper import selenium_code
app = Flask(__name__)

# Route to handle API requests
@app.route('/search', methods=['GET'])
def get_detail():

    args = request.args
    
    requireField = set(['CaseType', 'CaseNumber', 'CaseYear'])
    availableFields =  set(args.keys())
    if(availableFields.issubset(requireField)):
        res = selenium_code(args['CaseType'],args['CaseNumber'],args['CaseYear'])
        print(res.keys())
        return jsonify(res)

        
    else:    
      return jsonify({'error': 'Invalid Query'})

if __name__ == '__main__':
    app.run(debug=True)
# CaseType: For example, “Original Application”
# CaseNumber: A numerical value.
# CaseYear: The year when the case was filed.