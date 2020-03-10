from flask import render_template, flash, redirect, url_for
from app_package import app,db,mongo
from flask_login import current_user, login_user, logout_user, login_required
from app_package.forms import RegistrationForm, LoginForm
from app_package.models import Registration, Login, Role
from passlib.hash import pbkdf2_sha256 as pbsha
import pymysql

@app.route("/",methods=["GET","POST"])
def index():


    db=pymysql.connect("localhost","flasktamsuser","flasktamsuser","tamsdb")
    cursor = db.cursor()
    form=LoginForm()
    if form.validate_on_submit():
        user=Login.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid user")
            return redirect(url_for("index"))
        else:
    #try except finally
            cursor.execute("select role_id from login where username=%s", form.username.data)
            data = cursor.fetchone()
            cursor.execute("select role_name from role where role_id=%s", data)
            role=cursor.fetchone()
            db.close()
            if role==('admin',):
                return render_template("adminHome.html")
            if role==('coordinator',):
                return render_template("coordinatorHome.html")
            else:
                flash("Error")
                return redirect(url_for("index"))
    else:
        return render_template("login.html",form=form)

@app.route("/register",methods=["GET","POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("menu"))
    else:
        form=RegistrationForm()
        if form.validate_on_submit():
            regi=Registration(fullname=form.fullname.data)
            regi.set_email(form.email.data)
            regi.set_mobile(form.mobile.data)
            db.session.add(regi)
            db.session.commit()
            dba=pymysql.connect("localhost","flasktamsuser","flasktamsuser","tamsdb")
            cursor=dba.cursor()
            cursor.execute("select reg_id from registration where fullname=%s",form.fullname.data)
            regid=cursor.fetchone()
            dba.close()
            log=Login(username=form.username.data)
            log.set_password(form.password.data) 
            log.set_role_id(form.role_id.data)
            log.set_reg_id(regid)
            db.session.add(log)
            db.session.commit()
            flash("You may login now")
            return redirect(url_for("index"))
        else:
            return render_template("register.html",form=form)

""" @app.route("/adminmenu")
@login_required 
def adminmenu():
    return render_template("adminmenu.html")

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))
 """
