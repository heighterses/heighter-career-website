from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string, connect_args={
    "ssl": {
        "ssl_ca": "/etc/ssl/cert.pem",
    }
})

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        column_names = result.keys()
        jobs = [dict(zip(column_names, row)) for row in result]
    return jobs
  
  
def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text(f"SELECT * FROM jobs WHERE id = :val"),
      {"val": id}
    )
    rows = result.mappings().all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0])






def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text("INSERT INTO applications (job_id, full_name, email, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :resume_url, :education, :work_experience)")

        conn.execute(query, {                       
            "job_id": job_id,
            "full_name": data['full_name'],
            "email": data['email'],
            "resume_url": data['resume_url'],
            "work_experience": data['work_experience'],
            "education": data['education']
        })

  


    
    
    '''query = text("INSERT INTO applications (full_name, email, education, work_experience, resume_url) VALUES ( :full_name, :email, :resume_url, :education, :work_experience)")
    conn.execute(query,
                 full_name = data['full_name'],
                 email = data['email'],
                 education = data['education'],
                 work_experience = data['work_experience'],
                 resume_url = data['resume_url']
                )'''
  