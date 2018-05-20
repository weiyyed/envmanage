from flask_wtf import FlaskForm
from wtforms import BooleanField,SubmitField

class Restart(FlaskForm):
    # server_names=['sy','mgr','portal']
    # for i in server_names:
    sy=BooleanField('sy')
    mgr=BooleanField('mgr')
    restart=SubmitField('重启')