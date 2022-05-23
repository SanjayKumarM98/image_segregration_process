from models import *
from middleware import *
from login import *
from signup import *


# Info Database Route

# ------current_user--------------
# this route sends back list of users
@app.route('/practice/admin', methods=['GET'])
def get_all_users():
    # querying the database
    # for all the entries in it

    users = Info.query.all()
    # converting the query objects
    # to list of jsons
    output = []
    for user in users:
        # appending the user data json
        # to the response list
        if user.deleted_date is None:
            output.append(
                {'public_id': user.public_id, 'name': user.name, 'email': user.email, 'admin_access': user.admin,
                 'created_date': user.created_date, 'updated_date': user.updated_date,
                 'deleted_date': user.deleted_date})

    return jsonify({'users': output})


# --------------------
# This route sends the requested user details
@app.route('/practice/admin/<public_id>', methods=['GET', 'PUT', 'DELETE'])
def user_details(public_id):
    # To get only one user details
    if request.method == 'GET':

        user = Info.query.filter_by(public_id=public_id).first()

        if user.deleted_date is None:
            return jsonify(
                {'public_id': user.public_id, 'email': user.email, 'name': user.name, 'admin_access': user.admin,
                 'created_date': user.created_date, 'updated_date': user.updated_date,
                 'deleted_date': user.deleted_date})
        else:
            return jsonify({'message': 'User record has been deleted !!!!'})

    # --------------------
    # To delete a user details in DB

    if request.method == 'DELETE':
        user = Info.query.filter_by(public_id=public_id).first()

        now = datetime.now()
        deleted_date = now.strftime("%d-%m-%Y %H:%M:%S")

        user.deleted_date = deleted_date

        db.session.commit()

        return jsonify({'message': 'successfully deleted user details from db'})

    # --------------------
    # To update particular details of a user in DB

    if request.method == 'PUT':

        data = request.form

        column_name = data.get('field')
        value = data.get('value')

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
            return jsonify({'message': 'you cant edit this column!!!!'})

        else:
            return jsonify({'message': 'request-form is not sent!!!!'})

        now = datetime.now()
        updated_date = now.strftime("%d-%m-%Y %H:%M:%S")

        user.updated_date = updated_date

        db.session.commit()

        return jsonify({'message': 'user details has updated!!!'})
