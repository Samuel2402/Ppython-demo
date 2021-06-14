from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:02November19961!@35.242.155.112:3306/flaskdb"    # 'sqlite:///data.db' 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)

if __name__ == "__main__":
    app.run(debug=True)






############################# INTRO ###########################################################

#from flask import Flask

#app = Flask(__name__)

#@app.route('/')
#@app.route('/home')
#def hpme(): 
#    return "Home page"

#@app.route('/about')
#def about_page():
#    return "About page" 

#@app.route('/squared/<num>')
#def squared(num):
#    number = int(num)
#    result = number*number
#    return str(result)

#if __name__=='__main__':
#    app.run(debug=True)

