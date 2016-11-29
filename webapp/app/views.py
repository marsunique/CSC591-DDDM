from app import app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask import request,redirect,url_for


app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://team7:Eem3raRu@localhost:9003"
app.debug = True
db = SQLAlchemy(app)


#SELECT topic,SUM(comment_score) AS score FROM final_combine GROUP BY topic ORDER BY score DESC;
#SELECT topic,SUM(comment_score) AS score FROM final_combine WHERE location='California' GROUP BY topic ORDER BY score DESC;


class lexnexdata(db.Model):
	__tablename__ = 'lexnexdata'
	date = db.Column('date', db.Unicode, primary_key=True)
	content = db.Column('content', db.Unicode)																																																																																																																																																																																																							
	publication = db.Column('publication', db.Unicode)

class test(db.Model):
	__tablename__ = 'test'
	features = db.Column('features', db.Unicode, primary_key=True)

class populateDropdowns(db.Model):
    __tablename__ = 'final_combine'
    category = db.Column('category', db.Unicode)
    location = db.Column('location', db.Unicode)
    source = db.Column('source', db.Unicode)
    comment_score = db.Column('comment_score', db.Unicode)
    topic = db.Column('topic', db.Unicode)
    vote = db.Column('vote', db.Unicode)
    sentiment = db.Column('sentiment', db.Unicode)
    sentence = db.Column('sentence', db.Unicode)
    orig_comment = db.Column('orig_comment', db.Unicode)
    comment_id = db.Column('comment_id', db.Unicode,primary_key=True)
    #primary_key = db.Column('primary_key', db.Unicode, )

	
class test2(db.Model):
	__tablename__ = 'test2'
	primary_features = db.Column('primary_features', db.Unicode, primary_key=True)
	secondary_feature = db.Column('secondary_feature', db.Unicode)


@app.route('/index')
def index():
	user  = {'nickname':'Nate Silver'}
	lexdata = lexnexdata.query.all()
	dropdownCategory = populateDropdowns.query.distinct('category')
	dropdownStates = populateDropdowns.query.distinct('location')
	dropdownSource = populateDropdowns.query.distinct('source')
    	return render_template('index.html', lexdata = lexdata, dropdownCategory = dropdownCategory, dropdownStates = dropdownStates, dropdownSource = dropdownSource)


@app.route('/formData', methods=['POST'])
def button_group_form():
	print("Here")
	categorySelection = request.form["category"]
	#btnForm = request.form.get("btnForm")
	#print(btnForm)
	#print(request.get_json())
	sourceSelection = request.form["source"]
	stateSelection = request.form["state"]

	queries = dict()

	if(sourceSelection!="-"):
		queries["source"]=sourceSelection
		#queries.append(sourceSelection)
	if(stateSelection!="-"):
		queries["location"]=stateSelection
		#queries.append(stateSelection)
	if(categorySelection!="-"):
		queries["category"]=categorySelection
		#queries.append(categorySelection)


	q = db.session.query(populateDropdowns)

	queryStringBase = "SELECT * FROM final_combine"
	print("Length of query is")
	print(len(queries))
	if(len(queries)!=0):
		queryStringBase += " WHERE"

	for attr, value in queries.items():
		queryStringBase += " "
		queryStringBase += attr 
		queryStringBase += "='"
		queryStringBase += value
		queryStringBase += "'"

		if(len(queries)>1 and attr != queries.keys()[-1]):
			queryStringBase += " AND "

	print(queryStringBase)

#		q = q.filter(getattr(populateDropdowns, attr).like("%%%s%%" % value))

	result = db.engine.execute(queryStringBase)
	data = {}
	a =[]
	i=0
	for row in result:
		i += 1
		#primary_key = row[10]
		data[i] = [str(row[0]),row[1].encode("utf-8"),row[2].encode("utf-8"), str(row[3]), str(row[4])]
		a.append(data[i])

	print a
	print data
	print(queries.get("category"))

	dropdownCategory = populateDropdowns.query.distinct('category')
	dropdownStates = populateDropdowns.query.distinct('location')
	dropdownSource = populateDropdowns.query.distinct('source')

	return render_template('index.html',data=a, dropdownCategory = dropdownCategory, dropdownStates = dropdownStates, dropdownSource = dropdownSource)

@app.route('/')	
@app.route('/topIssues', methods=['GET'])
def topIssues():
	dropdownCategory = populateDropdowns.query.distinct('category')
	dropdownStates = populateDropdowns.query.distinct('location')
	dropdownSource = populateDropdowns.query.distinct('source')
	return render_template('topIssues.html', dropdownCategory = dropdownCategory, dropdownStates = dropdownStates, dropdownSource = dropdownSource)



@app.route('/topIssuesFormData', methods=['POST'])
def topIssues_button_group_form():
	print("Here")
	categorySelection = request.form["category"]
	sourceSelection = request.form["source"]
	stateSelection = request.form["state"]

	queries = dict()

	if(sourceSelection!="-"):
		queries["source"]=sourceSelection
		#queries.append(sourceSelection)
	if(stateSelection!="-"):
		queries["location"]=stateSelection
		#queries.append(stateSelection)
	if(categorySelection!="-"):
		queries["category"]=categorySelection
		#queries.append(categorySelection)



	q = db.session.query(populateDropdowns)
#SELECT topic,SUM(comment_score) AS score FROM final_combine WHERE location='California' GROUP BY topic ORDER BY score DESC;
	queryStringBase = "SELECT SUM(ABS(comment_score)) AS score, topic, SUM(comment_score), SUM(vote) FROM final_combine"
	print("Length of query is")
	print(len(queries))
	if(len(queries)!=0):
		queryStringBase += " WHERE"

	for attr, value in queries.items():
		queryStringBase += " "
		queryStringBase += attr 
		queryStringBase += "='"
		queryStringBase += value
		queryStringBase += "'"

		if(len(queries)>1 and attr != queries.keys()[-1]):
			queryStringBase += " AND "

#	if(len(queries)!=0):
	queryStringBase += " GROUP BY topic ORDER BY score DESC;"

	print(queryStringBase)

#		q = q.filter(getattr(populateDropdowns, attr).like("%%%s%%" % value))

	result = db.engine.execute(queryStringBase)
	data = {}
	tableData =[]
	i=0
	for row in result:
		i += 1
		#primary_key = row[10]
		data[i] = [str(row[0]),row[1].encode("utf-8"), str(row[2]),str(row[3])]
		tableData.append(data[i])

	print tableData
	print data
	print(queries.get("category"))

	dropdownCategory = populateDropdowns.query.distinct('category')
	dropdownStates = populateDropdowns.query.distinct('location')
	dropdownSource = populateDropdowns.query.distinct('source')

	return render_template('topIssues.html',data=tableData, dropdownCategory = dropdownCategory, dropdownStates = dropdownStates, dropdownSource = dropdownSource)

if __name__=="__main__":
    app.run()