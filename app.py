from flask import Flask , render_template, request
import os 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "who-is-who-in-myanmar.db"))


app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = "Who is Who in Myanmar"
db = SQLAlchemy(app)

@app.route('/',methods=['POST','GET'])
def home():
        
        person = Business leaders.query.filter_by(name='abc').first()
        name = person.name
        birthdate = person.birthdate
        occupation = person.occupation
        companyname = person.company
        photo = person.photo
        

	if request.method == 'POST' :

		app_name = request.form['app_name']
		app = App(app_name=app_name)
		db.session.add(app)
		db.session.commit()

	return render_template("business.html",name=name,birth=birth,occupation=occupation,facebook=facebook)


class Business Leaders(db.Model):

	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(20),nullable=False)
	birthdate = db.Column(db.String(20),nullable=False)
	occupation = db.Column(db.String(20),nullable=False)
        companyname = db.Column(db.String(20),nullable=False)
	photo = db.Column(db.Text,nullable=False)
	

	def __init__(self,*args,**kwargs):
		super(App,self).__init__(*args,**kwargs)

	def __repr__(self):
		return '<App %r>' % self.app_name


if __name__ == '__main__':
app.run(debug=True)
