from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class card_form(FlaskForm):
    card_data = StringField('Card Data', validators=[DataRequired()], render_kw={'autofocus': True})
    submit = SubmitField('Submit')