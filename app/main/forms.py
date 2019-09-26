from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class CommentForm(FlaskForm):
   
#    title = StringField('Comment title',validators=[Required()])
   comment = TextAreaField('pitch comment', validators=[Required()])
   submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class AddPitchForm(FlaskForm):
    category= SelectField('Category:',choices=[('pickup-lines','Pickup lines'),('Interview-pitches','interview pitches'),('promotion-pitches','Promotion pitches')])
    content=TextAreaField('Pitch',validators = [Required()])
    submit=SubmitField('SUBMIT')