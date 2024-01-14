from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost:5432/flask_article"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text())
    date = db.Column(db.DateTime, default=datetime.now(pytz.timezone('Asia/Jakarta')))

    def __init__(self, title, body):
        self.title = title
        self.body = body

class ArticleSchema(ma.Schema):
    date = ma.DateTime(format='%Y-%m-%d %H:%M')
    class Meta:
        fields  = ('id', 'title', 'body', 'date')

article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)

with app.app_context():
    db.create_all()

@app.route('/get', methods=["GET"])
def get_article():
    all_articles = Article.query.all()
    if all_articles:
        results = articles_schema.dump(all_articles)
        return jsonify(results)
    else:
        return jsonify({"message": "No articles found"})

@app.route('/get/<int:id>/', methods=["GET"])
def post_details(id):
    article = Article.query.get(id)
    
    if article:
        return article_schema.jsonify(article)
    else:
        return abort(404, description="Article not found")

@app.route('/add', methods=["POST"])
def add_article():
    title = request.json.get('title')
    body = request.json.get('body')

    if title and body:
        articles = Article(title, body)
        db.session.add(articles)
        db.session.commit()
        return article_schema.jsonify(articles)
    else:
        return jsonify({"message": "Title and body are required"}), 400

@app.route('/update/<int:id>/', methods=["PUT"])
def update_article(id):
    article = Article.query.get(id)

    if article:
        title = request.json.get('title')
        body = request.json.get('body')

        if title and body:
            article.title = title
            article.body = body
            db.session.commit()
            return article_schema.jsonify(article)
        else:
            return jsonify({"message": "Title and body are required"}), 400
    else:
        return abort(404, description="Article not found")

@app.route('/delete/<int:id>/', methods=["DELETE"])
def delete_article(id):
    article = Article.query.get(id)

    if article:
        db.session.delete(article)
        db.session.commit()
        return article_schema.jsonify(article)
    else:
        return abort(404, description="Article not found")

if __name__ == '__main__':
    app.run(debug=True, port=5001)
