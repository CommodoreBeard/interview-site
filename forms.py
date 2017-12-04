from flask_wtf import Form
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(Form):
    search_term = StringField(u'', validators=[DataRequired()])
    submit = SubmitField(u'Search')