from flask import Flask, render_template
app = Flask(__name__)


from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.myinterior


@app.route('/')
def home():
   return render_template('style_vote/style_vote_1.html')


@app.route('/vote2')
def go_vote2 ():
   return render_template('style_vote/style_vote_2.html')

@app.route('/vote3')
def go_vote3 ():
   return render_template('style_vote/style_vote_3.html')

@app.route('/vote4')
def go_vote4 ():
   return render_template('style_vote/style_vote_4.html')

@app.route('/vote5')
def go_vote5 ():
   return render_template('style_vote/style_vote_5.html')

@app.route('/vote6')
def go_vote6 ():
   return render_template('style_vote/style_vote_6.html')

@app.route('/vote7')
def go_vote7 ():
   return render_template('style_vote/style_vote_7.html')

@app.route('/vote8')
def go_vote8 ():
   return render_template('style_vote/style_vote_8.html')

@app.route('/vote9')
def go_vote9 ():
   return render_template('style_vote/style_vote_9.html')

@app.route('/vote10')
def go_vote10 ():
   return render_template('style_vote/style_vote_10.html')

@app.route('/survey_result')
def go_survey_result ():
   return render_template('survey_result.html')





if __name__ == '__main__':
   app.run('127.0.0.1' ,port=5000,debug=True)