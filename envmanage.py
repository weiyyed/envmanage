from flask import Flask
from flask import render_template
from forms import Restart
app = Flask(__name__)
app.config['SECRET_KEY']='never'

@app.route('/')
def home():
    form=Restart()
    return render_template('home.html',form=form)


if __name__ == '__main__':
    app.run(debug=True)
