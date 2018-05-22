from flask_wtf import FlaskForm
from wtforms import BooleanField,SubmitField

class Restart(FlaskForm):
    server_names=['sy','mgr','portal','passport','eam','trn','hse','csc','phd','pom',
                  'eam_m','trn_m','hse_m','csc_m','phd_m','pom_m']

    for i in server_names:
        locals()[i]=BooleanField(i)
        restart=SubmitField('restart')