from flask import (Flask,
                   render_template,
                   request,
                   url_for,
                   redirect,
                   session,
                   g)
from functions import (get_api_igredients,
                       get_api_meal,
                       get_api_wine,
                       loading_files)
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user_base.db"
db.init_app(app)
app.secret_key = 'secret'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)


with app.app_context():
    db.create_all()


@app.before_request
def before_request():
    if 'user' in session:
        user = session['user']
        print(user)
        g.user = user


@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template("index.html")


@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        user = request.form.get('user')
        password = request.form.get('password')
        if not db.session.query(User).filter(User.username == user).all():
            return redirect(url_for('create_user'))
        elif db.session.query(User).filter(User.username == user).all():
            check_password = db.session.query(User).filter(User.username == user).first()
            print(check_password.password)
            if check_password.password != password:
                message = " The password is incorrect"
                context = {'message': message
                           }
                return render_template("login.html", context=context)
            else:
                session["user"] = user
                return redirect(url_for('index'))

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))


@app.route("/create_user", methods=['POST', 'GET'])
def create_user():
    if request.method == "POST":
        user = request.form.get('user')
        password = request.form.get('password')
        if not db.session.query(User).filter(User.username == user).all():
            new_user = User(username=user, password=password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("index"))
        else:
            message = 'Username is already in the database'
            context = {'message': message
                       }
            return render_template("create.html", context=context)
    return render_template("create.html")


@app.route("/wine", methods=['POST', 'GET'])
def choise_wine():
    return render_template("choise_wine.html")


@app.route("/ingredients", methods=['POST', 'GET'])
def ingredients():
    ask = request.form.get('ask')
    print(ask)
    wynik = get_api_igredients(ask)
    context = {"wynik": wynik,
               }
    return render_template("igredients.html", context=context)


@app.route("/meal", methods=['POST', 'GET'])
def meal():
    ask = request.form.get('ask')
    wynik = get_api_meal(ask)[0]
    image = get_api_meal(ask)[1]
    context = {"wynik": wynik,
               "image": image,
               }
    return render_template("meal.html", context=context)


@app.route("/getwine", methods=['POST', 'GET'])
def get_wine():
    if request.method == "POST":
        ask = request.form.get('ask')
        wynik = get_api_wine(ask)
        context = {"wynik": wynik,
                   }
    else:
        context = {"wynik": [],
                   }
    return render_template("get_wine.html", context=context)


@app.route("/wine/white_wine", methods=['POST', 'GET'])
def white_wine():
    wines = loading_files('tekst/white_wine.txt')
    context = {"wino": wines,
               }
    return render_template("white_wine.html", context=context)


@app.route("/wine/white_wine/dry", methods=['POST', 'GET'])
def white_dry_wine():
    wines = loading_files('tekst/dry_white_wine.txt')
    context = {"wino": wines,
               }
    return render_template("dry_white_wine.html", context=context)


@app.route("/wine/desert_wine", methods=['POST', 'GET'])
def desert_wine():
    wines = loading_files('tekst/dessert_wine.txt')
    context = {"wino": wines,
               }
    return render_template("desert_wine.html", context=context)
