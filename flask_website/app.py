from flask import Flask
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://team7:Eem3raRu@localhost:9002"
db = SQLAlchemy(app)
																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																											
@app.route('/')
def index():
    return"hello flask"

if __name__=="__main__":
    app.run()

class lexnexdata(db.Model):
	__tablename__ = 'lexnexdata'
	date = db.Column('date', db.Unicode, primary_key=True)
	content = db.Column('content', db.Unicode)																																																																																																																																																																																																							
	publication = db.Column('publication', db.Unicode)


