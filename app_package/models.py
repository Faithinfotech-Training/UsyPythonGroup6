from app_package import db, login_manager
from flask_login import UserMixin
from passlib.hash import pbkdf2_sha256 as pbsha

@login_manager.user_loader
def load_user(self):
    return Registration.query.get(self.reg_id)

class Role(UserMixin,db.Model):

    __tablename__ = 'role'
    role_id=db.Column(db.Integer,primary_key=True)
    role_name=db.Column(db.String(64),unique=True)
 
class Login(UserMixin, db.Model):

    __tablename__ = 'login'
    l_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    role_id = db.Column(db.Integer())
    username=db.Column(db.String(64),unique=True)
    password_hash=db.Column(db.String(128))
    reg_id=db.Column(db.Integer())

    def set_password(self,password):

        self.password_hash=pbsha.hash(password)

    def check_password(self,password):

        return pbsha.verify(password,self.password_hash)

    def set_role_id(self,role_id):

        self.role_id =role_id

    def get_role_id(self):

        return self.role_id

    def set_reg_id(self, reg_id):

        self.reg_id =reg_id

    def get_reg_id(self):

        return self.reg_id

#def check_user(self,username):

#return Login.role_id

#def get_username(self,username):

#return Login.l_id
class Registration(UserMixin, db.Model): 

    __tablename__ = 'registration' 
    reg_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    fullname=db.Column(db.String(64))
    mobile=db.Column(db.Integer) 
    email=db.Column(db.String(64))




    def set_email(self, email):
        self.email = email
    def get_email(self):
        return self.email
    def set_mobile(self, mobile):
        self.mobile = mobile
    def get_mobile(self):
        return self.mobile




