from distutils.log import debug
from flask import Flask, render_template, request
from werkzeug.security import check_password_hash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# objet qui represente l'user
class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    password = db.Column("password", db.String(100))
                         
    def __init__(self, name, password):
        self.name = name
        self.password = password

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/post_login", methods=["get", "post"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    print("Username:", username, "password:", password)
    
    elca_password = 'pbkdf2:sha256:260000$ANLguAnydma42U68$0dd66afb1ba97e26ffa6984f2f28f5d8fe9188e772c06adb1b1deab2860efb31'
    
    if username == 'elca' and check_password_hash(elca_password, password):
        return 'Acces Autoriser pour ELCA'
    else:
        return 'Page traitement'
    
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)