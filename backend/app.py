from flask import Flask, render_template,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('DATABASE_URL', 'postgresql://postgres:19990521a@localhost:5432/nameInfo')
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
  def to_dict(self):
    return {
        'fname': self.fname,
        'lname': self.lname
    }

@app.route('/', methods=['POST'])
def submit():
  data = request.get_json()
  fname = data['fname']
  lname = data['lname']
  student=Student(fname,lname)
  db.session.add(student)
  db.session.commit()
  return jsonify({"message": "success post"}),200

@app.route('/', methods=['GET'])
def students():
    all_students = Student.query.all()
    return jsonify([student.to_dict() for student in all_students]), 200

if __name__ == '__main__':
    app.run(debug=True,port=5001)