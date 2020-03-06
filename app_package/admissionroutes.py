from flask import render_template, flash, redirect, url_for
from app_package import app,mongo
from flask_login import current_user, login_user, logout_user, login_required
from app_package.admissionforms import AdmissionSearchForm,AdmissionAddForm




@app.route("/Admissionhome",methods=["GET","POST"])
def Admissionhome():
    form=AdmissionSearchForm()
    f2=AdmissionAddForm()
    if form.validate_on_submit():
        ad_col=mongo.db.enquiry
        edata=ad_col.find_one({"e_phone":form.e_phone.data})
        if edata["e_status"]=='Exam Passed':
            return render_template("Admissionform.html",form=form,f2=f2,edata=edata)
        else:
            flash("Not Applicable Candidate")
            return redirect(url_for("Admissionhome"))
    else:
        return render_template("Admissionhome.html",form=form)

@app.route("/Admission_add",methods=["GET","POST"])
def Admission_add():
    form=AdmissionAddForm()
    if form.validate_on_submit():
        ad_col=mongo.db.admission
        if ad_col.count()==0:
            a_id=0
        else:
            a=ad_col.find().sort("_id",-1).limit(1)
            tmp=a.next()
            a_id=tmp["_id"]
        a_id+=1
        fields=["_id","ad_name","ad_gender","ad_phone","ad_email","ad_qualification","ad_year_of_pass","ad_batch","ad_guardianname","ad_guardianphone","ad_address"]
        values=[a_id,form.e_name.data,form.e_gender.data,form.e_phone.data,form.e_email.data,form.e_qualification.data,form.e_year_of_pass.data,form.e_batch.data,form.e_guardianname.data,form.e_guardianphone.data,form.e_address.data]
        candidate=dict(zip(fields,values))
        tmp=ad_col.insert_one( candidate)
        if tmp.inserted_id==a_id:
            flash(" Candidate Added")
            return redirect(url_for("Admissionhome"))
        else:
            flash("Problem in adding Candidate")
            return redirect(url_for("Admissionform")) 
    else:
        flash(" Cannot submit")
        return redirect(url_for("Admissionhome"))

    

   
