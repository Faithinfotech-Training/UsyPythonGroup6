from flask import render_template,flash,redirect,url_for
from app_package import app,mongo
#from flask_login import current_user,login_user,logout_user,login_required
from app_package.module_forms import AddModuleForm,CourseForm

check=True    
cmod_id=0

@app.route("/addmodules",methods=["GET","POST"])
def addmodules():
	form=CourseForm()
	course_col=mongo.db.courses
	cour=course_col.find()
	lst=[]
	for q in cour:
		lst.append((q['coursename'],q["coursename"]))
	form.courseName.choices=lst
	if form.validate_on_submit():
		
		mod_col=mongo.db.modules
		cmod_col=mongo.db.course_modules
		allmod=cmod_col.find({"coursename":form.courseName.data})
		
		mod=mod_col.find()
		lst=[]
		for q in mod:
			lst.append((q['name'],q["name"]))
		form=AddModuleForm()
		form.name.choices=lst
		return render_template("addmodule.html",allmod=allmod,form=form,course=form.courseName.data)
	return render_template("selectcourse.html",form=form)

@app.route("/viewmodules",methods=["GET","POST"])
def viewmodules():
    global check
    global cmod_id
    form=AddModuleForm()
    fields=["_id","coursename","modulename"]
    cmod_col=mongo.db.course_modules
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
        if i['modulename']==form.name.data:
            flag=False
            break
        else:
            flag=True
    mod_col=mongo.db.modules
    allmod=cmod_col.find({"coursename":form.courseName.data})
    mod=mod_col.find()
    lst=[]
    for q in mod:
        lst.append((q['name'],q["name"]))
    form=AddModuleForm()
    form.name.choices=lst
    if flag:
        temp=cmod_col.insert_one(cmod)
        if temp.inserted_id==cmod_id:
            flash("module added")
            return render_template("addmodule.html",allmod=allmod,form=form,course=form.courseName.data)
        else:
            flash("problem on adding module ")
            return render_template("addmodule.html",allmod=allmod,form=form,course=form.courseName.data)
    else:
        flash("module already exists")
        return render_template("addmodule.html",allmod=allmod,form=form,course=form.courseName.data)
'''
@app.route("/deletemodule/<int:a>/<string:b>", methods=["GET","POST"])
def deletemodule(a,b):
    form=AddModuleForm()
    cmod_col=mongo.db.course_modules
    cmod_col.delete_one({"_id":a})
    mod_col=mongo.db.modules
    cmod_col=mongo.db.course_modules
    allmod=cmod_col.find({"coursename":b})
    mod=mod_col.find()
    lst=[]
    for q in mod:
        lst.append((q['name'],q["name"]))
    form.name.choices=lst
    flash("module deleted")
    #return render_template("addmodule.html",allmod=allmod,form=form,course=b)
    return redirect(url_for("viewmodules"))
'''
'''@app.route("/deletemodule/<int:a>/<string:b>", methods=["GET","POST"])
def deletemodule(a,b):
    form=AddModuleForm()
    cmod_col=mongo.db.course_modules
    cmod_col.delete_one({"_id":a})
    mod_col=mongo.db.modules
    cmod_col=mongo.db.course_modules
    allmod=cmod_col.find({"coursename":b})
    mod=mod_col.find()
    lst=[]
    for q in mod:
        lst.append((q['name'],q["name"]))
    form.name.choices=lst
    flash("module deleted")
    #return render_template("addmodule.html",allmod=allmod,form=form,course=b)
    return redirect(url_for("addmodules"))'''