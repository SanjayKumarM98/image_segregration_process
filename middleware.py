from models import *


@app.before_request
def before_request_func():

    if request.path == "/practice/login" or request.path == "/practice/signup":
        return None
    else:

        token = None

        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        # return 401 if token is not passed
        if not token:
            return jsonify({'message': 'Token is missing !!!'}), 401

        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            if data:
                exp = data['exp']
                ct = datetime.utcnow().strftime('%Y%m%d%H%M%S')
                FMT = '%Y%m%d%H%M%S'
                tdelta = (datetime.strptime(exp, FMT) - datetime.strptime(ct, FMT)).seconds
                min = tdelta / 60

                if min <= 0:
                    return jsonify({'message': 'Token has expired!!'}), 401

            else:
                return jsonify({'message': 'Please Pass Token For Validation!!!!'})
        except Exception as e:
            print(e)
            return jsonify({'message':'Token Is Incorrect!!!'}), 401
