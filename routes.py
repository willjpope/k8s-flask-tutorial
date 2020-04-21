from flask import render_template, flash, redirect, url_for

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
