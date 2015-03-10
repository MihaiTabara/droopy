from flask.ext.wtf import Form
from wtforms import (SubmitField, StringField, IntegerField)
from wtforms.validators import InputRequired, Length, ValidationError


class DroopyForm(Form):
    screen_name = StringField(u'Screen name', [InputRequired(),
                                               Length(max=99)])
    no_of_tweets = IntegerField(u'No. of tweets', default=10)
    submit = SubmitField('Scrap!')

    def __init__(self, *args, **kwargs):
        super(DroopyForm, self).__init__(*args, **kwargs)

    def validate_no_of_tweets(form, field):
        if field.data > 3200:
            raise ValidationError("No. of tweets is bound to 3200 per user")
