from init import *


class Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(70), unique=True)
    password = db.Column(db.String(300))
    admin = db.Column(db.Boolean, default=False)

    created_date = db.Column(db.DateTime, default=db.func.now())
    updated_date = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    deleted_date = db.Column(db.DateTime, default=None)
