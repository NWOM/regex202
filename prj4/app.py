from flask import Flask,render_template,request
from flask_wtf import FlaskForm 
from  wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import re
app=Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'
class RegexForm(FlaskForm):
	regex=StringField('Regex', validators=[DataRequired()])
	test_string=StringField('Test String',validators=[DataRequired()])
	submit=SubmitField('Submit')
@app.route('/')
def index():
	return 'HELLO WORLD!'

@app.route('/regex',methods=['GET','POST'])
def regex():
	form=RegexForm()
	result=None
	if form.validate_on_submit():
		regex=form.regex.data
		test_string=form.test_string.data
		match=re.search(regex,test_string)
		if match:
			result=match.group()
	return	render_template('regex.html',form=form,result=result)	
if __name__=='__main__'	:
	app.run(debug=True)
