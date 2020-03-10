from flask import render_template, flash, redirect, url_for
from app_package import app, db,mongo
from flask_login import current_user, login_user, logout_user, login_required
from app_package.admissionforms import AdmissionSearchForm,AdmissionAddForm,AdmissionUpdateForm
#from app_package.models import User
from datetime import date


@app.route("/Admissionhome",methods=["GET","POST"])
def Admissionhome():
    form=AdmissionSearchForm()
    f2=AdmissionAddForm()
    batch_col=mongo.db.batches
    batch=batch_col.find()
    lst=[]
    for i in batch:
        lst.append((i["batch_name"],i["batch_name"]))
    f2.batch_name.choices=lst
   
    if form.validate_on_submit():
        ad_col=mongo.db.enquiry
        edata=ad_col.find_one({"e_phone":form.e_phone.data})
        if not bool(edata):
            flash("No results found")
            return redirect(url_for("Admissionhome"))
        else:
            if edata["e_status"]=='Exam Passed' or edata["e_status"]!='Joined':
                return render_template("Admissionform.html",form=form,f2=f2,edata=edata)
            else:
                flash("Not applicable candidate")
                return redirect(url_for("Admissionhome"))
    else:
        return render_template("Admissionhome.html",form=form)

@app.route("/Admission_add",methods=["GET","POST"])
def Admission_add():
    form=AdmissionAddForm()
    batch_col=mongo.db.batches
    batch=batch_col.find()
    lst=[]
    for i in batch:
        lst.append((i["batch_name"],i["batch_name"]))
    form.batch_name.choices=lst
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
        values=[a_id,form.e_name.data,form.e_gender.data,form.e_phone.data,form.e_email.data,form.e_qualification.data,form.e_year_of_pass.data,form.batch_name.data,form.e_guardianname.data,form.e_guardianphone.data,form.e_address.data]
        candidate=dict(zip(fields,values))
        tmp=ad_col.insert_one( candidate)
        if tmp.inserted_id==a_id:
            values=dict()
            e_col=mongo.db.enquiry
            values["e_status"]='Joined'
            new_data={"$set":values}
            query={"e_phone":form.e_phone.data}
            e_col.update_one(query,new_data)
            flash(" Candidate Added")
            return redirect(url_for("Admissionhome"))
        else:
            flash("Problem in adding Candidate")
            return redirect(url_for("Admissionform")) 
    else:
        flash(" Cannot Submit")
        return redirect(url_for("Admissionhome"))

@app.route("/Admissionlist",methods=["GET","POST"])
def Admissionlist():
    ad_col=mongo.db.admission
    edata=ad_col.find()
    return render_template("Admissionlist.html",edata=edata)

@app.route("/Admissionupdate/<int:eid>",methods=["GET","POST"])
def Admissionupdate(eid): 
    
    e_col=mongo.db.admission
    edata=e_col.find_one({"_id":eid})
    f2=AdmissionUpdateForm()
    batch_col=mongo.db.batches
    batch=batch_col.find()
    lst=[]
    for i in batch:
        lst.append((i["batch_name"],i["batch_name"]))
    f2.ad_batch.choices=lst
    if True:
        values=dict()
        e_col=mongo.db.admission
        if f2.ad_name.data!="":values["ad_name"]=f2.ad_name.data
        if f2.ad_phone.data!="":values["ad_phone"]=f2.ad_phone.data
        if f2.ad_email.data!="":values["ad_email"]=f2.ad_email.data
        if f2.ad_qualification.data!="":values["ad_qualification"]=f2.ad_qualification.data
        if f2.ad_year_of_pass.data!="":values["ad_year_of_pass"]=f2.ad_year_of_pass.data
        if f2.ad_batch.data!="":values["ad_batch"]=f2.ad_batch.data
        if f2.ad_guardianname.data!="":values["ad_guardianname"]=f2.ad_guardianname.data
        if f2.ad_guardianphone.data!="":values["ad_guardianphone"]=f2.ad_guardianphone.data
        if f2.ad_address.data!="":values["ad_address"]=f2.ad_address.data
        year= date.today().year
        if f2.ad_year_of_pass.data>1900 and f2.ad_year_of_pass.data<=year:
            new_data={"$set":values}
            query={"_id":eid}
            e_col.update_one(query,new_data)
            flash("Candidate Modified")
            return redirect(url_for("Admissionhome"))
        else:
            flash("Invalid Year")
            return render_template("Admissionupdate.html",f2=f2,edata=edata)
    else:
        flash("Some problems")
        return render_template("Admissionupdate.html",f2=f2,edata=edata)  
