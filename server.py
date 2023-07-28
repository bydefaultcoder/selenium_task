from flask import Flask, jsonify, request
from selenium import webdriver

app = Flask(__name__)

# Route to handle API requests
@app.route('/search', methods=['GET'])
def search_google():

    print(request.args)
    
    # first_link = get_first_google_link(query)
    # if first_link:
    #     return jsonify({'first_link': first_link})
    # else:
    return jsonify({'error': 'No links found'})

if __name__ == '__main__':
    app.run(debug=True)
# CaseType: For example, “Original Application”
# CaseNumber: A numerical value.
# CaseYear: The year when the case was filed.