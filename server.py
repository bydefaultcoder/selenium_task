from flask import Flask, jsonify, request
from selenium import webdriver

app = Flask(__name__)

# Route to handle API requests
@app.route('/search', methods=['GET'])
def search_google():

    args = request.args
    print(args)
    
    return jsonify({'error': 'No links found'})

if __name__ == '__main__':
    app.run(debug=True)
# CaseType: For example, “Original Application”
# CaseNumber: A numerical value.
# CaseYear: The year when the case was filed.