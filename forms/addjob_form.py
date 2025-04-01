from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Optional

class AddJobForm(FlaskForm):
    team_leader = IntegerField('Team leader', validators=[DataRequired()])
    job = StringField('Job', validators=[DataRequired()])
    work_size = IntegerField('Work size', validators=[Optional()])
    start_date = StringField('Start date', validators=[DataRequired()])
    end_date = StringField('End date', validators=[DataRequired()])
    submit = SubmitField('Add job')