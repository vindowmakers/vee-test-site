from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
{
  'id':1,
  'title': "Software Engineer",
  'location' : 'Spain',
  'salary' : '50000'
  
},

{
  'id':2,
  'title': 'Data Scientist',
  'location' : 'NY',
   
},

 {
  'id':3,
  'title': 'Rocket Scientist',
  'location' : 'GA',
  'salary' : '150000'

 }, 
  
]

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)
if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True)