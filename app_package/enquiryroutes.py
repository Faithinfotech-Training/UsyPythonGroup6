from flask import render_template, flash, redirect, url_for
from app_package import app, db,mongo
from flask_login import current_user, login_user, logout_user, login_required
from app_package.enquiryforms import EnquiryForm,EnquirySearchForm,EnquiryUpdateForm,EnquiryFilterForm
from app_package.models import User

@app.route("/",methods=["GET","POST"])
def index():
    return redirect(url_for("Enquiryhome"))

@app.route("/Enquiryhome",methods=["GET","POST"])
def Enquiryhome():
    form=EnquirySearchForm()
    f2=EnquiryFilterForm()
    if form.validate_on_submit():
        es_col=mongo.db.enquiry
        search=form.es_type.data
        if search=='Name':
            es_s={"e_name":form.es_name.data}
            edata=es_col.find(es_s)
            return render_template("Enquirydetails.html",edata=edata)
        else:
            return render_template("Enquiryhome.html",form=form)
    elif f2.validate_on_submit():
        es_col=mongo.db.enquiry
        filter=f2.ef_status.data
        es_s={"e_status":filter}
        edata=es_col.find(es_s)
        return render_template("Enquirydetails.html",edata=edata)
    else:
       return render_template("Enquiryhome.html",form=form,f2=f2)

@app.route("/Enquiryform", methods=["GET","POST"])
def Enquiryform():
    form=EnquiryForm()
    if form.validate_on_submit():
        e_col=mongo.db.enquiry
        if e_col.count()==0:
            e_id=0
        else:
            e=e_col.find().sort("_id",-1).limit(1)
            tmp=e.next()
            e_id=tmp["_id"]
        e_id+=1
        if form.e_year_of_pass.data>1900:
            fields=["_id","e_name","e_gender","e_phone","e_email","e_qualification","e_course_of_interest","e_year_of_pass","e_status"]
            values=[e_id,form.e_name.data,form.e_gender.data,form.e_phone.data,form.e_email.data,form.e_qualification.data,form.e_course_of_interest.data,form.e_year_of_pass.data,form.e_status.data]
            enquiredcust=dict(zip(fields,values))
            tmp=e_col.insert_one(enquiredcust)
            if tmp.inserted_id==e_id:
                flash(" Enquired Customer Added")
                return redirect(url_for("Enquiryhome"))
            else:
                flash("Problem in adding Enquired customer")
                return redirect(url_for("Enquiryform")) 
        else:
            flash("Inavalid year")
            return render_template("Enquiryform.html",form=form)
    else:
        return render_template("Enquiryform.html",form=form)

@app.route("/Enquirystatusupdate/<int:eid>", methods=["GET","POST"])
def Enquirystatusupdate(eid):
    form=EnquiryUpdateForm()
    e_col=mongo.db.enquiry
    e=e_col.find_one({"_id":eid})
    if form.validate_on_submit():
        values=dict()
        e_col=mongo.db.enquiry
        if form.eu_name.data!="":values["e_name"]=form.eu_name.data
        if form.eu_phone.data!="":values["e_phone"]=form.eu_phone.data
        if form.eu_email.data!="":values["e_email"]=form.eu_email.data
        if form.eu_qualification.data!="":values["e_qualification"]=form.eu_qualification.data
        if form.eu_course_of_interest.data!="":values["e_course_of_interest"]=form.eu_course_of_interest.data
        if form.eu_year_of_pass.data!="":values["e_year_of_pass"]=form.eu_year_of_pass.data
        if form.eu_status.data!="":values["e_status"]=form.eu_status.data
        if form.eu_year_of_pass.data>1900:
            new_data={"$set":values}
            query={"_id":eid}
            e_col.update_one(query,new_data)
            flash("Customer Modified")
            return redirect(url_for("Enquiryhome"))
        else:
            flash("Invalid Year")
            return render_template("Enquirystatusupdate.html",form=form,e=e)
    else:
        return render_template("Enquirystatusupdate.html",form=form,e=e)
