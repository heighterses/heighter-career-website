from flask import Flask, render_template
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)

@app.route("/")
def hello_world():
    jobs = load_jobs_from_db()
    return render_template("home.html", jobs=jobs, company_name='heighterbyte')

@app.route("/job/<id>")  # Convert 'id' to an integer
def show_job(id):
    job = load_job_from_db(id)
    return render_template('jobpage.html', job=job)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)