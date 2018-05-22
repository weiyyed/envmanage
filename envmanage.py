from flask import Flask
from flask import render_template,flash,redirect
from forms import Restart
app = Flask(__name__)
app.config['SECRET_KEY']='never'
app.debug=True

@app.route('/',methods=['GET','POST'])
@app.route('/test_linux',methods=['GET','POST'])
def test_linux():
    form=Restart()
    if form.validate_on_submit():
        print('tijiao')
        flash("已提交")
        return redirect('/')
    return render_template('home.html',form=form)


if __name__ == '__main__':
    app.run(debug=True)
