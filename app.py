from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///animals.db'
db=SQLAlchemy(app)

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    owner_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    petsowner = db.relationship('Person',
        backref=db.backref('owner', lazy='dynamic'))

    def __init__(self, name, owner_id):
        self.name = name
        self.owner_id=owner_id


    def __repr__(self):
        return '<Pet %r>' % self.name


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Person %r>' % self.name

@app.route('/')
def index():
    person=db.session.query(Person).all()
    return render_template('index.html', person=person)

if __name__=='__main__':
    app.run(debug=True)
