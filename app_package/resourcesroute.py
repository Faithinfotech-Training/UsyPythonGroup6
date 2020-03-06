from flask import render_template, flash, redirect, url_for
from app_package import app, db,mongo
from flask_login import current_user, login_user, logout_user, login_required
from app_package.forms import AddResourceForm,UpdateResourceForm
#from app_package.models import User

check=True
res_id=0

@app.route("/",methods=["GET","POST"])
def index():
    return redirect(url_for("view_resource"))

@app.route("/add_resource",methods=["GET","POST"])
def add_resource():
    global check,res_id
    form=AddResourceForm()
    
    if form.validate_on_submit():
        fields=["_id","res_name","res_capacity","res_status","res_rent","type_of_use"]
        res_col=mongo.db.resources
        if check:
            check=False
            if res_col.count()==0:
                res_id=0
            else:
                res=res_col.find().sort("_id",-1).limit(1)
                tmp=res.next()
                res_id=tmp["_id"]
        res_id+=1
        values=[res_id,form.res_name.data,form.res_capacity.data,form.res_status.data,form.res_rent.data,form.type_of_use.data]
        resource=dict(zip(fields,values))
        query_name={"res_name":form.res_name.data}
        
        name_check=res_col.find_one(query_name)
        if not bool(name_check) :
          
            tmp=res_col.insert_one(resource)
            if tmp.inserted_id==res_id:
                flash("Resource Added")
                return redirect(url_for("add_resource"))
            else:
                flash("Problem adding resource")
                return redirect(url_for("add_resource"))
            
        else:
            flash("Resource already added")
            return redirect(url_for("add_resource"))
    
    else:
        return render_template("add_resource.html",form=form)


@app.route("/update_resource/<int:a>",methods=["GET","POST"])
def update_resource(a):
    form=UpdateResourceForm()
    res_col=mongo.db.resources
    resource=res_col.find_one({"_id":a})
    if form.validate_on_submit():
        
        values=dict()
        if form.res_capacity.data!="":values["res_capacity"]=form.res_capacity.data
        else:
            flash("Invalid capacity or rent fields....Cannot update")
            return redirect(url_for("view_resource"))
        if form.res_status.data!="":values["res_status"]=form.res_status.data
        if form.res_rent.data!="":values["res_rent"]=form.res_rent.data
       
        if form.type_of_use.data!="":values["type_of_use"]=form.type_of_use.data
        new_data={"$set":values}
        query={"_id":a}
        res_col=mongo.db.resources
        res_col.update_one(query,new_data)
        flash("Resource updated")
    
        return redirect(url_for("view_resource"))
    else:
        return render_template("update_resource.html",form=form,resource=resource)    
        

@app.route("/view_resource")
def view_resource():
    res_col=mongo.db.resources
    resources=res_col.find()
    return render_template("view_resource.html",resources=resources)  

