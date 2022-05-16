from settings import *
import json

# Initializing our database
db=SQLAlchemy(app)

# the class student will inherit the db.Model of SQLAlchemy
class student(db.Model):

    #table name
    __tablename__='students'

    #primary key -> Unique
    student_id=db.Column(db.Integer,primary_key=True)

    #nullable -> Shouldn't be empty
    first_name=db.Column(db.String(80),nullable=False)
    last_name=db.Column(db.String(80))
    standard=db.Column(db.String(80),nullable=False)
    age=db.Column(db.Integer,nullable=False)
    gender=db.Column(db.String(80))
    dob=db.Column(db.String(80))
    created_date=db.Column(db.String(80),default="None")
    updated_date=db.Column(db.String(80),default="None")
    deleted_date=db.Column(db.String(80),default="None")
    dob_edited_count=db.Column(db.Integer,default=0)

    def json(self):
        return {'student_id':self.student_id,'first_name':self.first_name,'last_name':self.last_name,'standard':self.standard,'age':self.age,'gender':self.gender,'dob':self.dob}
        # this method we are defining will convert our output to json

    def add_details(_student_id,_first_name,_last_name,_standard,_age,_gender,_dob):
        #function to add new student details to database using _student_id,_first_name,_last_name,_standard,_age,_gender as parameters

        #Creating an instance of our student constructor

        if (bool(student.query.filter_by(student_id=_student_id).first())):
            pass
        else:
            now = datetime.now()
            created_date_p1 = now.strftime("%d-%m-%Y %H:%M:%S")

            new_student=student(student_id=_student_id,first_name=_first_name,last_name=_last_name,standard=_standard,age=_age,gender=_gender,dob=_dob,created_date=created_date_p1)
            db.session.add(new_student)
            db.session.commit()

    def get_all_student_details():
        #function to get all student details from database
        return [student.json(stud_detail) for stud_detail in student.query.all() if stud_detail.deleted_date == "None"]

    def get_student_details(_student_id):
        #function to get specific student details from database using student_id
        try:
            return [student.json(student.query.filter_by(student_id=_student_id,deleted_date="None").first())]
        except:
            return "Student Record Has Not Found"

    def update_student_details(_student_id,_first_name,_last_name,_standard,_age,_gender,_dob):
        #function to update the details of a student using the student_id,first_name,last_name,standard,age,gender as parameters
        student_details_update=student.query.filter_by(student_id=_student_id).first()
        student_details_update.first_name = _first_name
        student_details_update.last_name = _last_name
        student_details_update.standard = _standard
        student_details_update.age = _age
        student_details_update.gender = _gender

        if student_details_update.dob_edited_count <= 1:
            student_details_update.dob = _dob
            student_details_update.dob_edited_count=student_details_update.dob_edited_count+1

        now=datetime.now()
        student_details_update.updated_date=now.strftime("%d-%m-%Y %H:%M:%S")
        student_details_update.deleted_date="None"

        db.session.commit()

    def delete_student_details(_student_id):
        #function used to delete student details record from database
        # student.query.filter_by(student_id=_student_id).delete()

        student_details_update=student.query.filter_by(student_id=_student_id).first()

        now=datetime.now()
        student_details_update.deleted_date=now.strftime("%d-%m-%Y %H:%M:%S")

        # filter movie by id and delete
        db.session.commit()  # commiting the new change to our database
