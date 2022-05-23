from models import *

# route for logging user in
@app.route('/practice/login', methods=['POST'])
def login():

    # creates dictionary of form data
    auth = request.json

    if not auth['email'] or not auth['password']:
        # returns 401 if any email or / and password is missing
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm ="Login required !!"'})

    user = Info.query.filter_by(email=auth['email']).first()

    if not user:
        # returns 401 if user does not exist
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm ="User does not exist !!"'})

    if check_password_hash(user.password, auth['password']):
        # generates the JWT Token
        token = jwt.encode({'public_id': user.public_id, 'exp': (datetime.utcnow() + timedelta(minutes=30)).strftime('%Y%m%d%H%M%S')},app.config['SECRET_KEY'])

        return make_response(jsonify({'token': token}), 201)

    # returns 403 if password is wrong
    return make_response('Could not verify', 403, {'WWW-Authenticate': 'Basic realm ="Wrong Password !!"'})
