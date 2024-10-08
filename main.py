from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #Тут настройки бд
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///OnlineShop.bd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Модель товару в Базі данних
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True)

# Головна сторінка мого магазину
@app.route('/')
def index():
    items = Item.query.order_by(Item.price).all()
    return render_template('index.html', data=items)

@app.route('/about') #Інформація про компанію
def about():
    return render_template('about.html')

# Створення товарів в магазе
@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == "POST":
        title = request.form['title']
        price = request.form['price']
        item = Item(title=title, price=price)
        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/')
        except:
            return "Помилка в роботі БД"
    return render_template('create.html')

# Редагування товарів
@app.route('/edit/<int:id>', methods=['POST', 'GET'])
def edit(id):
    item = Item.query.get_or_404(id)
    if request.method == "POST":
        item.title = request.form['title']
        item.price = request.form['price']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "Помилка під час редагування"
    return render_template('edit.html', item=item)

# Видалення товару з магазину
@app.route('/delete/<int:id>')
def delete(id):
    item = Item.query.get_or_404(id)
    try:
        db.session.delete(item)
        db.session.commit()
        return redirect('/')
    except:
        return "Помилка при видаленні товару"

if __name__ == "__main__":
    app.run(debug=True)