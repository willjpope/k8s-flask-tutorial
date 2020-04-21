from flask import render_template, flash, redirect, url_for
from forms import LoginForm


@route('/')
@route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(
            form.username.data))
        return redirect(url_for('index'))
    return render_template('login.html',  title='Sign In', form=form)