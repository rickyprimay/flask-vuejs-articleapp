from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost:5432/flask_article"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text())
    date = db.Column(db.DateTime, default=datetime.now(pytz.timezone('Asia/Jakarta')))

    def __init__(self, title, body):
        self.title = title
        self.body = body
with app.app_context():
    db.create_all()

@app.route('/', methods=["GET"])
def get_articles():
    return jsonify({
        "msg":"starter"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5001)