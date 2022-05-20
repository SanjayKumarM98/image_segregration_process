from models import *
from decorator import *
from login import *
from signup import *

# Info Database Route

# --------------------
# this route sends back list of users
@app.route('/practice/admin', methods=['GET'])
@token_required
def get_all_users(current_user):
    # querying the database
    # for all the entries in it

    if current_user.admin:

        users = Info.query.all()
        # converting the query objects
        # to list of jsons
        output = []
        for user in users:
            # appending the user data json
            # to the response list
            if user.deleted_date == "None":
                output.append({'public_id': user.public_id, 'name': user.name, 'email': user.email, 'admin_access':user.admin, 'created_date':user.created_date, 'updated_date':user.updated_date, 'deleted_date':user.deleted_date})

        return jsonify({'users': output})

    else:
        return jsonify({'message':'you dont have access to this page'})

# --------------------
#This route sends the requested user details
@app.route('/practice/admin/<public_id>',methods=['GET','PUT','DELETE'])
@token_required
def user_details(current_user,public_id):

    # To get only one user details
    if request.method == 'GET':

        if current_user.admin:

            user=Info.query.filter_by(public_id=public_id).first()

            if user.deleted_date == "None":
                return jsonify({'public_id':user.public_id,'email':user.email,'name':user.name,'admin_access':user.admin, 'created_date':user.created_date, 'updated_date':user.updated_date, 'deleted_date':user.deleted_date})
            else:
                return jsonify({'message':'User record has been deleted !!!!'})

        else:
            return jsonify({'message':'you dont have access to this page'})

    # --------------------
    # To delete a user details in DB

    if request.method == 'DELETE':

        if current_user.admin:

            user = Info.query.filter_by(public_id=public_id).first()

            now=datetime.now()
            deleted_date=now.strftime("%d-%m-%Y %H:%M:%S")

            user.deleted_date=deleted_date

            db.session.commit()

            return jsonify({'message':'successfully deleted user details from db'})
        else:
            return jsonify({'message':'you dont have access to this page'})

    # --------------------
    # To update particular details of a user in DB

    if request.method == 'PUT':

        if current_user.admin:

            data = request.form

            column_name=data.get('field')
            value=data.get('value')

            user = Info.query.filter_by(public_id=public_id).first()

            if column_name == 'name':
                user.name = value

            elif column_name == 'email':
                user.email = value

            elif column_name == 'password':
                user.password = generate_password_hash(value)

            elif column_name == 'admin':
                if value == 'true':
                    user.admin = True
                else:
                    user.admin = False

            elif column_name == 'created_date' or column_name == 'updated_date' or column_name == 'deleted_date':
                return jsonify({'message':'you cant edit this column!!!!'})

            else:
                return jsonify({'message':'request-form is not sent!!!!'})

            now=datetime.now()
            updated_date=now.strftime("%d-%m-%Y %H:%M:%S")

            user.updated_date=updated_date

            db.session.commit()

            return jsonify({'message':'user has been promoted!!!'})

        else:
            return jsonify({'message':'you dont have access to this page'})
