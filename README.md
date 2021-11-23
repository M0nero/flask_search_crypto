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

##Examples

Welcome page
![alt text](https://user-images.githubusercontent.com/74233809/143092084-e8753b13-fdcf-4dd1-b626-b41f8cf5e222.png)

/login - at first user asked to enter the login and a password
![alt text](https://user-images.githubusercontent.com/74233809/143091973-b073e2d5-6392-444d-b4cc-5c09fe1ed621.png)

Welcome page after user has entered
![alt text](https://user-images.githubusercontent.com/74233809/143091986-a2ea7b71-43b2-4ff2-9113-949f6ca4d0dd.png)

/Provided token is correct
![alt text](https://user-images.githubusercontent.com/74233809/143091984-ee53aae7-1a79-46cd-93f7-e4ffa4ff8c94.png)

![alt text]

![alt text]

![alt text]
