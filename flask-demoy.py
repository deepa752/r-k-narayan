from flask import Flask, jsonify
from getInstance import getWordOfTheDay

app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login():
    return "Login Hogya."
"http://127.0.0.1:5000/get_word_of_the_day"

@app.route('/get_word_of_the_day', methods=['GET'])
def getNewWord():
    data = {
        "newWord":getWordOfTheDay()
    }
    return jsonify(data)
    
app.run(debug=True) # start the server.