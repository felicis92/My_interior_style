from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('style_vote_1.html')


@app.route('/vote2')
def go_vote2 ():
   return render_template('style_vote_2.html')


if __name__ == '__main__':
   app.run('127.0.0.1' ,port=5000,debug=True)