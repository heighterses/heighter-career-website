from flask import Flask, render_template

app = Flask(__name__)

JOBS=[
  {'id': 1,
  'title': 'Data Scientist',
  'location': 'Islamabad, Pakistan',
  'salary': '85,000 Rs'},
    {'id': 2,
  'title': 'Data Engineer',
  'location': 'Rawalpindi, Pakistan'},
    {'id': 3,
  'title': 'ASO Optimiser',
  'location': 'Islamabad, Pakistan',
  'salary': '85,000 Rs'},
    {'id': 4,
  'title': 'Data Analyst',
  'location': 'Remote',
  'salary': '65,000 Rs'},
    {'id': 5,
  'title': 'Research Analyst',
  'location': 'Lahore, Pakistan',
  'salary': '89,000 Rs'}
]

@app.route("/")
def hello_world():
  return render_template("home.html",
                        jobs=JOBS, company_name='Heighter')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
