from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///task.db"
app.config['SQLALCHEMY_DATABASE_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class sheduling(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    Task = db.Column(db.String(500), nullable = False)
    Description = db.Column(db.String(1000), nullable = False)
    Task_Deadline = db.Column(db.String(10), nullable = False)
    date_created = db.Column(db.DateTime, default=lambda : datetime.now(timezone.utc))
    priority = db.Column(db.Integer, nullable = False)
    def _repr_(self) -> str:
        return f"{self.sno} - {self.Task} - {self.Task_Deadline}"
    
class wellnesstracker(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    Mood = db.Column(db.String(200), nullable = False)
    Describe = db.Column(db.String(200), nullable = False)
    Stress_Rate = db.Column(db.String(5), nullable = False)
    STRESS = db.Column(db.String(500), nullable = False)
    TYPE = db.Column(db.String(200), nullable = False)
    date_created = db.Column(db.DateTime, default = lambda : datetime.now(timezone.utc))
    def _repr_(self) -> str:
        return f"{self.sno} - {self.Mood} - {self.Stress_Rate} - {self.TYPE}"    

@app.route('/', methods = ['GET', 'POST'])
def front():
    if (request.method == 'POST'):
        TASK = request.form['task']
        DESC = request.form['desc']
        DEAD = request.form['deadline']
        Prio = request.form['importance']

        WLM = sheduling(Task = TASK, Task_Deadline = DEAD, Description = DESC,priority = Prio )
        db.session.add(WLM)
        db.session.commit()

    return render_template('index.html')

@app.route('/sheduling')
def shed():
    alldata = sheduling.query.order_by(sheduling.priority).all()
    return render_template('sheduling.html', alldata = alldata)

@app.route('/progress')
def prog():
    alldata = sheduling.query.order_by(sheduling.priority).all()
    return render_template('progress.html', alldata = alldata)

@app.route('/delete/<int:sno>')
def dele(sno):
    data = sheduling.query.filter_by(sno=sno).first()
    db.session.delete(data)
    db.session.commit()
    return redirect('/progress')

@app.route('/tracker', methods = ['GET', 'POST'])
def track():
    if(request.method == 'POST'):
        MOOD = request.form['Mood']
        DESC = request.form['desc']
        Rate = request.form['stressrate']
        Stress = request.form['stress']
        type = request.form['category']

        WOM2 = wellnesstracker(Mood = MOOD, Stress_Rate = Rate, STRESS = Stress,TYPE = type, Describe= DESC)
        db.session.add(WOM2)
        db.session.commit()
        

        return redirect('/tracker')
    
    allmoods = wellnesstracker.query.all()

    return render_template('Wellness.html', allmoods = allmoods)


if __name__ == "_main_":
    with app.app_context():
        db.create_all()
    app.run(debug = True)