from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
   form = LoginForm()
   if form.validate_on_submit():
      flash('Login requested for user {}'.format(form.username.data))
      return redirect(url_for('index'))
   return render_template('index.html',  title='Sign In', form=form)
