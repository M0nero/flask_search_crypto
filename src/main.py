from flask import Flask, render_template, request, session
import jwt
from flask_sqlalchemy import SQLAlchemy
from scrapper import Scrapper
from datetime import datetime, timedelta
from flask.helpers import make_response
from functools import wraps

app = Flask(__name__, template_folder='../templates',
            static_url_path='', static_folder='../static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:5258@localhost:5432/news'
app.config['SECRET_KEY'] = 'thisismyflasksecretkey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column('id', db.Integer, primary_key=True)
    login = db.Column('login', db.Unicode)
    password = db.Column('password', db.Unicode)
    token = db.Column('token', db.Unicode)

    def __init__(self, id, login, password, token):
        self.id = id
        self.login = login
        self.password = password
        self.token = token

    def __repr__(self):
        return f"User('{self.login}', '{self.token}')"


class News(db.Model):
    __tablename__ = 'news'

    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String())
    sourcelink = db.Column(db.String())
    title = db.Column(db.String())
    subtitle = db.Column(db.String())
    time = db.Column(db.String())
    paragraph = db.Column(db.String())
    summary = db.Column(db.String())

    def __init__(self, source, sourcelink, title, subtitle, time, paragraph, summary):
        self.source = source
        self.sourcelink = sourcelink
        self.title = title
        self.subtitle = subtitle
        self.time = time
        self.paragraph = paragraph
        self.summary = summary

    def add(self):
        db.session.add(self)
        db.session.commit()
        pass


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return render_template('main.html',
                                   main_title="Oops! Something went wrong.", message="Hello, no token was provided", message_color="#a60f0f",
                                   button="go home", button_link="/")
        try:
            jwt.decode(token, app.config.get(
                'SECRET_KEY'), algorithms=['HS256'])
        except:
            return render_template('main.html',
                                   main_title="Oops! Something went wrong.", message="Hello, Could not verify the token", message_color="#a60f0f",
                                   button="go home", button_link="/")

        return f(*args, **kwargs)

    return decorated


@app.route('/')
def main():
    return render_template('main.html',
                           main_title="Welcome", button="Login", button_link="/login")


@app.route('/search', methods=['GET', 'POST'])
@token_required
def search():
    query = request.form.get('text-field')
    if not query:
        return render_template('search.html', query=query)

    return render_template('search.html', query=query, data=scrap(query))


@app.route('/login')
def login():

    auth = request.authorization
    username = ""
    if auth:
        username = auth.username
        usernamedata = Users.query.filter_by(
            login=auth.username, password=auth.password).first()
        if usernamedata is not None:

            token = jwt.encode({'user': auth.username, 'exp': datetime.utcnow(
            ) + timedelta(minutes=30)}, app.config['SECRET_KEY'])
            update_token = Users.query.filter_by(id=usernamedata.id).first()
            update_token.token = token
            db.session.commit()
            return render_template('main.html',
                                   main_title="Hi, " + username, button="check token", button_link="/protected?token=" + token)
    return make_response(f'<h1>Could not found a user with login: {username}</h1>', 401, {'WWW-Authenticate': 'Basic realm="Login required'})


@app.route('/protected')
@token_required
def protected():
    token = request.args.get('token')
    user = Users.query.filter_by(token=token).first()
    return render_template('main.html',
                           main_title="Hi, " + user.login, message="Hello, token which is provided is correct", message_color="#16ab0b",
                           button="search", button_link="/search?token=" + token)


def scrap(query):
    scrapper = Scrapper()
    results = scrapper.get_data(query)

    for result in results:
        news = News(
            title=result['title'],
            subtitle=result['subtitle'],
            source=result['source'],
            sourcelink=result['sourcelink'],
            time=result['time'],
            paragraph=result['paragraph'],
            summary=result['summary']
        )
        news.add()

    return results


db.drop_all()
db.create_all()

user1 = Users(id=1, login='Damir', password='lolkek', token='some_token')
user2 = Users(id=2, login='Elmira', password='saku', token='some_token')
user3 = Users(id=3, login='Van', password='Darkholme', token='some_token')

db.session.add(user1)
db.session.add(user2)
db.session.add(user3)

db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)
