from flask import render_template, flash, redirect, url_for
from app_package import app,mongo
from flask_login import current_user, login_user, logout_user, login_required
from app_package.forms import AddResourceForm,UpdateResourceForm
from app_package.models import User

@app.route("/",methods=["GET","POST"])
def index():
    return render_template("base.html")