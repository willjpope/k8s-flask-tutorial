from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
import teradata as td

#import teradatasql as td

def loginToTD(strHost, strUsr, strPwd):
    try:
        #tdSession = td.connect(host=strHost, user=strUsr, password=strPwd, logmech='LDAP')
        tdInfo = td.UdaExec(appName = 'UCBD', version = '0.1', logConsole = True)
        tdConn = tdInfo.connect(method = 'odbc', driver = 'Teradata', system = strHost, username = strUsr, password = strPwd, authentication = 'LDAP')
        return True
    except:
        return False


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Will'}
    posts = [
        {
            'author': {'username': 'Jay'},
            'body': 'Classic bantz!'
        },
        {
            'author': {'username': 'Anneliese'},
            'body': 'Wish I was at work!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if loginToTD(form.database.data, form.username.data, form.password.data):
            flash('Login succeeded for user {}'.format(form.username.data))
        else:
            flash('Login failed for user {}'.format(form.username.data))
        return redirect(url_for('index'))
    return render_template('login.html',  title='Sign In', form=form)
