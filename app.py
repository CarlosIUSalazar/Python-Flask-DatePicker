from flask import Flask, redirect, url_for, render_template, session
from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
from wtforms import validators, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = '#$%^&*'

class InfoForm(FlaskForm):
    startdate = DateField('Start Date', format='%Y-%m-%d', validators=(validators.DataRequired(),))
    enddate = DateField('End Date', format='%Y-%m-%d', validators=(validators.DataRequired(),))
    submit = SubmitField('Submit')

@app.route('/', methods=['GET','POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        session['startdate'] = form.startdate.data
        session['enddate'] = form.enddate.data
        return redirect('date')
    return render_template('index.html', form=form)

@app.route('/date', methods=['GET','POST'])
def date():
    startdate = session['startdate']
    enddate = session['enddate']
    return render_template('date.html')

if __name__ == '__main__':
    app.run(debug=True)