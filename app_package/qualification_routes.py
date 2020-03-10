from flask import render_template,flash,redirect,url_for
from app_package import app,mongo
#from flask_login import current_user,login_user,logout_user,login_required
from app_package.qualification_forms import AddQualificationForm,CourseForm

check=True    
cmod_id=0

@app.route("/addqualifications",methods=["GET","POST"])
def addqualifications():
	form=CourseForm()
	course_col=mongo.db.courses
	cour=course_col.find()
	lst=[]
	for q in cour:
		lst.append((q['coursename'],q["coursename"]))
	form.courseName.choices=lst
	if form.validate_on_submit():
		
		qual_col=mongo.db.qualifications
		cqual_col=mongo.db.course_qualifications
		allqual=cqual_col.find({"coursename":form.courseName.data})
		qual=qual_col.find()
		lst=[]
		for q in qual:
			lst.append((q['name'],q["name"]))
		form=AddQualificationForm()
		form.name.choices=lst
		return render_template("addqualification.html",allqual=allqual,form=form,course=form.courseName.data)
	return render_template("selectcourse.html",form=form)

@app.route("/viewqualifications",methods=["GET","POST"])
def viewqualifications():
    global check
    global cmod_id
    form=AddQualificationForm()
    fields=["_id","coursename","qualifname"]
    cmod_col=mongo.db.course_qualifications
    if check:
        check=False
        if cmod_col.count()==0:
            cmod_id=0
        else:
            cmods=cmod_col.find().sort("_id",-1).limit(1)
            tmp=cmods.next()
            cmod_id=tmp["_id"]
    cmod_id+=1
    values=[cmod_id,form.courseName.data,form.name.data]
    cmod=dict(zip(fields,values))
    crs_mod=cmod_col.find({"coursename":form.courseName.data})
    flag=True
    for i in crs_mod:
        if i['qualifname']==form.name.data:
            flag=False
            break
        else:
            flag=True
    mod_col=mongo.db.qualifications
    allqual=cmod_col.find({"coursename":form.courseName.data})
    mod=mod_col.find()
    lst=[]
    for q in mod:
        lst.append((q['name'],q["name"]))
    form=AddQualificationForm()
    form.name.choices=lst
    if flag:
        temp=cmod_col.insert_one(cmod)
        if temp.inserted_id==cmod_id:
            flash("qualification added...")
            return render_template("addqualification.html",allqual=allqual,form=form,course=form.courseName.data)
        else:
            flash("problem on adding qualification ")
            return render_template("addqualification.html",allqual=allqual,form=form,course=form.courseName.data)
    else:
        flash("qualification already exists")
        return render_template("addqualification.html",allqual=allqual,form=form,course=form.courseName.data)

'''@app.route("/deletequalification/<int:a>/<string:b>", methods=["GET","POST"])
def deletequalification(a,b):
    form=AddQualificationForm()
    cmod_col=mongo.db.course_qualifications
    cmod_col.delete_one({"_id":a})
    mod_col=mongo.db.qualifications
    cmod_col=mongo.db.course_qualifications
    allqual=cmod_col.find({"coursename":b})
    mod=mod_col.find()
    lst=[]
    for q in mod:
        lst.append((q['name'],q["name"]))
    form.name.choices=lst
    flash("qualification deleted")
    return render_template("addqualification.html",allqual=allqual,form=form,course=b)
    #return redirect(url_for("addqualifications"))'''