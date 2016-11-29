from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask import request,redirect,url_for

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://team7:Eem3raRu@localhost:9003"
app.debug = True
db = SQLAlchemy(app)
																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																											
class lexnexdata(db.Model):
	__tablename__ = 'lexnexdata'
	date = db.Column('date', db.Unicode, primary_key=True)
	content = db.Column('content', db.Unicode)																																																																																																																																																																																																							
	publication = db.Column('publication', db.Unicode)

@app.route('/')
def index():
	lexdata = lexnexdata.query.all()
	one_item = lexnexdata.query.filter_by(publication = "Newspaper").first()
    	return render_template('add_template1.html', lexdata = lexdata,one_item=one_item)

@app.route('/post_info', methods = ['POST'])
def post_info():
	return "hi post"

if __name__=="__main__":
    app.run()




