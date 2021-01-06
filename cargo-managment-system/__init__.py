from flask import Flask


app = Flask(__name__)
app.secret_key = 'hello_world'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Elif/Desktop/cargo-managment-system/cargo-system.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'True'
app.config.from_object(__name__)
