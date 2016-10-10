from pollster import Pollster
import csv
import json

###Need pollster installed in order to run this script

#Instantiate pollster object. 
pollster = Pollster()

listOfCharts =  pollster.charts(topic='2016-president',page=1);


#Printing polls
polls =  pollster.polls(chart='2016-general-election-trump-vs-clinton');

# Printing properties and values of an object code. For debugging purposes
#	for property, value in vars(i).iteritems():
#		print property, ": ", value
#


count = 0 
print polls[0].questions
for i in polls:
	with open('dataPoll' + `count` + '.csv', "w") as f1:
		f = csv.writer(f1)
		poll = i.questions[0]
		subpop = poll['subpopulations'][0]
		responses = subpop['responses']
		f.writerow(["Poll", "ClintonSupport","TrumpSupport","Observations"])
		clinton = [x for x in responses if x['last_name']=='Clinton']
		trump = [x for x in responses if x['last_name']=='Trump']
		f.writerow([i.pollster,clinton[0]['value'],trump[0]['value'],subpop['observations']])
		count =count +1


