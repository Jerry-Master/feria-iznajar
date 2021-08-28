from flask import Flask, render_template, request, url_for
from flask_assets import Environment, Bundle
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select, desc
import hashlib

def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha512(hash_string.encode()).hexdigest()
    return sha_signature

app = Flask(__name__)

assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('style.scss', 'myStyle.scss', filters='pyscss', output='all.css')
assets.register('scss_all', scss)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mzsikswffqeubk:b07d1ce16562f7febccbae0540f635713675957cd54de5868820b8f698e610f3@ec2-54-72-155-238.eu-west-1.compute.amazonaws.com:5432/d5rqdr8k39dtqb'

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'

    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), primary_key=True, nullable=False)
    password = db.Column(db.String(10000), nullable=False)
    money = db.Column(db.Integer(), nullable=False)

    def __init__(self, username, password, money):
        self.username = username
        self.password = password
        self.money = money

@app.route('/')
def init():
    return render_template('login.html')

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/checkLog/', methods=['GET', 'POST'])
def chekLog():
    if request.method == 'POST':
        user = db.session.execute(
            select(User.username, User.password).where(User.username==request.form['username'])
            ).first()
        user_password = encrypt_string(request.form['password'])
        return str(user[1] == user_password)

@app.route('/signup/')
def signup():
    return render_template('signup.html')

@app.route('/check/', methods=['GET', 'POST'])
def check():
    if request.method == 'POST':
        users = [x[0] for x in db.session.query(User.username).all()]
        return str(request.form['user'] in users)

@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        username = data['username']
        password = encrypt_string(data['password'])

        new_data = User(username, password, 0)
        db.session.add(new_data)
        db.session.commit()
    return render_template('login.html')

@app.route('/money/', methods=['GET', 'POST'])
def money():
    if request.method == 'POST':
        money = db.session.execute(
                select(User.username, User.money).where(User.username==request.form['username'])
                ).first()[1]
        return url_for('money2', username=request.form['username'], money=money)
    return None

@app.route('/money2/<username>/<money>')
def money2(username, money):
    return render_template('ui.html', username=username, money=money)

@app.route('/c7ad44cbad762a5da0a452f9e854fdc1e0e7a52a38015f23f3eab1d80b931dd472634dfac71cd34ebc35d16ab7fb8a90c81f975113d6c7538dc69dd8de9077ec/')
def admin():
    return render_template('admin.html')

@app.route('/admin-data/')
def admin_data():
    ret = [{'username': x[0], 'money': x[1]} for x in db.session.execute(select(User.username, User.money).order_by(desc(User.money))).all()][1:]
    return {'body': ret, 'status': '200'}

@app.route('/add/', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if request.form['quantity'] != '':
            user.money += int(request.form['quantity'])
            db.session.commit()
    return url_for('c7ad44cbad762a5da0a452f9e854fdc1e0e7a52a38015f23f3eab1d80b931dd472634dfac71cd34ebc35d16ab7fb8a90c81f975113d6c7538dc69dd8de9077ec')

@app.route('/remove/', methods=['GET', 'POST'])
def remove():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if request.form['quantity'] != '':
            user.money -= int(request.form['quantity'])
            db.session.commit()
    return url_for('c7ad44cbad762a5da0a452f9e854fdc1e0e7a52a38015f23f3eab1d80b931dd472634dfac71cd34ebc35d16ab7fb8a90c81f975113d6c7538dc69dd8de9077ec')