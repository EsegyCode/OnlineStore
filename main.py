from flask import Flask, render_template
from sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqllite:///OnlineShop.bd'
db=SQLAlchemy


class Item(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100), nullable=False)
    price=db.Column(db.Integer, nullable=False)
    isActive=db.Column(db.Boolean, default=True)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')





if __name__ == "__main__":
    app.run(debug=True)