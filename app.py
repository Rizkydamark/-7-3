from flask import Flask, render_template,jsonify,request
from pymongo import MongoClient

Connection_string = 'mongodb+srv://test:kaina24@cluster0.acicfe4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
client = MongoClient(Connection_string)
db = client.dbsparta

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/diary' , methods=['GET'])
def show_diary():
    articles = list(db.diary.find({}, {'_id': False}))
    return jsonify({'articles': articles})

@app.route('/diary' , methods=['POST'])
def save_diary():
    title_receive = request.form['title_give']
    content_receive = request.form['content_give']
    doc = {
        'title': title_receive,
        'content': content_receive
    }
    db.diary.insert_one(doc)
    return jsonify({'msg': 'data was saved'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)