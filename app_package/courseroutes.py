from flask import render_template, flash, redirect, url_for
from app_package import app,mongo
from flask_login import current_user, login_user, logout_user, login_required
from app_package.courseforms import AddCourseForm,ModifyCourseForm
#from app_package.models import User

check=True
couid=3
@app.route("/course",methods=["GET","POST"])
#@login_required
def course():
     return redirect(url_for("display_course"))
    
@app.route("/add_course",methods=["GET","POST"])
#@login_required
def add_course():
    global check,couid
    form=AddCourseForm()
    if form.validate_on_submit():
        fields=["_id","coursename","courseduration","coursefee","coursestatus","coursedescription"]
        course_col=mongo.db.courses
        if check:
            check=False
            if course_col.count()==0:
                couid=0
            else:
                course=course_col.find().sort("_id",-1).limit(1)
                temp=course.next()
                couid=temp["_id"]
        couid+=1
        course=course_col.find_one({"coursename":form.coursename.data})
        if not bool(course):
            values=[couid,form.coursename.data,form.courseduration.data,form.coursefee.data,form.coursestatus.data,form.coursedescription.data]
            course=dict(zip(fields,values))
            course_col=mongo.db.courses
            tmp=course_col.insert_one(course)
            if tmp.inserted_id==couid:
                flash("Course added")
                return redirect(url_for("course"))
            else:
                flash("Problem adding course")
                return redirect(url_for("course"))
        else:
            flash("Course name already exists...")
            return redirect(url_for("add_course"))   
    else:
        return render_template("add_course.html",form=form)
        

@app.route("/modify_course/<int:a>",methods=["GET","POST"])
#@login_required
def modify_course(a):
    form=ModifyCourseForm()
    course_col=mongo.db.courses
    course=course_col.find_one({"_id":a})
    if form.validate_on_submit():
        values=dict()
        if form.coursename.data!="":values["coursename"]=form.coursename.data
        if form.courseduration.data!="":values["courseduration"]=form.courseduration.data
        if form.coursefee.data!="":values["coursefee"]=form.coursefee.data
        if form.coursestatus.data!="":values["coursestatus"]=form.coursestatus.data
        if form.coursedescription.data!="":values["coursedescription"]= form.coursedescription.data
        query={"_id":a}
        course_col=mongo.db.courses
        new_data={"$set":values}
        course_col.update_one(query,new_data)
        flash("Course modified")
        return redirect(url_for("course")) 
    else:
        return render_template("modify_course.html",form=form,course=course)

@app.route("/display_course")
#@login_required
def display_course():
    course_col=mongo.db.courses
    courses=course_col.find()
    return render_template("display_course.html",courses=courses)