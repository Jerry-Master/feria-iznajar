from flask import Flask, render_template, request
from flask_assets import Environment, Bundle
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('style.scss', 'myStyle.scss', filters='pyscss', output='all.css')
assets.register('scss_all', scss)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://mzsikswffqeubk:b07d1ce16562f7febccbae0540f635713675957cd54de5868820b8f698e610f3@ec2-54-72-155-238.eu-west-1.compute.amazonaws.com:5432/d5rqdr8k39dtqb'

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'

    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def __init__(self, name, email):
        self.name = name
        self.email = email

@app.route('/')
def init():
    return render_template('login.html')

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/signup/')
def signup():
    return render_template('signup.html')

@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        print(request.form)
    return render_template('login.html')

@app.route('/db/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form
        name = data['name']
        email = data['email']

        new_data = User(name, email)
        db.session.add(new_data)
        db.session.commit()

        user_data = User.query.all()

        return render_template('login.html', user_data = user_data)
    return render_template('login.html')
