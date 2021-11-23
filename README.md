# flask_search_crypto

### Akbarov Damir, Orujova Elmira SE-2008


Application that allows to login, check the token, and search news about cryptocurrency to output it



## Installation



To do this project following libraries required: ```Flask```, ```Flask SQLAlchemy```, ```beautifulsoup```, ```Psycopg2```, ```jwt```, ```lxml```, ```tensorflow```, ```torch```. Below shown the installation



```
pip install beautifulsoup4
pip install Flask
pip install Flask-SQLAlchemy
pip install requests
pip install psycopg2
pip install jwt
pip install lxml
pip install tensorflow
pip install torch
```

#Install script 

```
git clone https://github.com/M0nero/flask_search_crypto.git
cd flask_search_crypto
#create venv
```

## Usage 



User needs to change password and enter his/her password from DBMS, in my case it is '123'


```python
app = Flask(__name__, template_folder='../templates', static_url_path='', static_folder='../static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432/jwt_flask'
app.config['SECRET_KEY'] = 'thisismyflasksecretkey
```

| id | login    | password | token      |
| -- | -------- | -------- | -----------|
| 1  | Damir    |  lolkek  | some_token |
| 2  | Elmira   |   saku   | some_token |
| 3  | Van      | Darkholme| some_token |
