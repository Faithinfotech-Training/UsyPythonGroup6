from flask import render_template, flash, redirect, url_for
from app_package import app,mongo
#from flask_login import current_user, login_user, logout_user, login_required
from app_package.batchforms import AddBatchForm,ModifyBatchForm
#from app_package.models import User

check=True
batch_id=0
@app.route("/",methods=["GET","POST"])
def menu():
    return redirect(url_for("display_batches"))
@app.route("/add_batch",methods=["GET","POST"])
#@login_required
def add_batch():
    global batch_id
    global check
    form=AddBatchForm()
    if form.validate_on_submit():
        fields=["_id","batch_name","start_date","end_date","course_name","batch_status"]
        batch_col=mongo.db.batches
        if check:
            check=False
            if batch_col.count()==0:
                batch_id=0
            else:
                bat=batch_col.find().sort("_id",-1).limit(1)
                tmp=bat.next()
                batch_id=tmp["_id"]
        batch_id+=1
        values=[batch_id,form.batch_name.data,form.start_date.data,form.end_date.data,form.course_name.data,form.batch_status.data]
        batch=dict(zip(fields,values))
        if form.end_date.data < form.start_date.data:
            flash("End date must not be earlier than start date.")
            return render_template("add_batch.html",form=form)
        else:
            batch_col=mongo.db.batches
            tmp=batch_col.insert_one(batch)
            if tmp.inserted_id==batch_id:
                flash("New Batch Added")
                return redirect(url_for("menu"))
            else:
                flash("Problem adding batch")
                return redirect(url_for("logout"))
    else:
        return render_template("add_batch.html",form=form)


@app.route("/modify_batch/<int:a>",methods=["GET","POST"])
#@login_required
def modify_batch(a):
    form=ModifyBatchForm()
    batch_col=mongo.db.batches
    batch=batch_col.find_one({"_id":a})
    if form.validate_on_submit():
        if form.end_date.data < form.start_date.data:
            flash("End date must not be earlier than start date.")
            return render_template("modify_batch.html",form=form,batch=batch)
        values=dict()
        if form.start_date.data!="":values["start_date"]=form.start_date.data
        if form.end_date.data!="":values["end_date"]=form.end_date.data
        if form.batch_status.data!="":values["batch_status"]=form.batch_status.data
        new_data={"$set":values}
        query={"_id":a}
        batch_col=mongo.db.batches
        batch_col.update_one(query,new_data)
        flash("Batch modified")
        return redirect(url_for("menu"))
    else:
        return render_template("modify_batch.html",form=form,batch=batch)

@app.route("/display_batches")
#@login_required
def display_batches():
    batch_col=mongo.db.batches
    batches=batch_col.find()
    return render_template("display_batches.html",batches=batches)

@app.route("/logout")
def logout():
    return redirect(url_for("menu"))