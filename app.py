from flask import Flask, render_template, jsonify
#from flask_pymongo import PyMongo

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/update_text')
def update_text():
    # Perform any server-side logic here
    response_data = {'message': 'Text box updated from the server!'}
    return jsonify(response_data)
