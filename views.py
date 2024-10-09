from __init__ import app, db # Your view functions here
from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

# Additional routes can be defined here
