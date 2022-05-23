from models import *

# signup route
@app.route('/practice/signup', methods=['POST'])
def signup():

    data = request.json

    # gets name, email and password
    name,email,password = data['name'],data['email'],data['password']

    # update admin value as true or false if it is passed, otherwise update its default value i.e., false
    try:
        admin = data['admin']

    except:
        admin = False

    # checking for existing user
    user = Info.query.filter_by(email=email).first()

    if not user:
        now=datetime.now()
        created_date=now.strftime("%d-%m-%Y %H:%M:%S")

        # database ORM object
        user = Info(public_id=str(uuid.uuid4()),name=name,email=email,password=generate_password_hash(password),admin=admin,created_date=created_date)

        # insert user
        db.session.add(user)
        db.session.commit()

        return make_response('Successfully registered.', 201)

    else:
        # returns 202 if user already exists
        return make_response('User already exists. Please Log in.', 202)
