from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:19990521a@localhost:5432/nameInfo'
db=SQLAlchemy(app)

class Student(db.Model):
  __tablename__='students'
  id=db.Column(db.Integer,primary_key=True)
  fname=db.Column(db.String(40))
  lname=db.Column(db.String(40))

  def __init__(self,fname,lname):
    db.create_all()
    self.fname=fname
    self.lname=lname


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
  fname= request.form['fname']
  lname=request.form['lname']

  student=Student(fname,lname)

  db.session.add(student)
  db.session.commit()
  return render_template('success.html', data=fname)

@app.route('/students', methods=['GET'])
def students():
    all_students = Student.query.all()
    return render_template('students.html', students=all_students)

if __name__ == '__main__':
    app.run(debug=True,port=5001)