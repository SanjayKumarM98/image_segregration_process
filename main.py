from flask import Flask,request,make_response
from functools import wraps

app=Flask(__name__)

#Below Is The Decorator Function
def auth_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        auth=request.authorization

        if auth and auth.username == 'kumar' and auth.password == 'kumar':
            return f(*args,**kwargs)

        return make_response('Please Login Before Accessing this page',401,{'WWW-Authenticate':'Basic realm="Login Required'})

    return decorated

@app.route('/')
def index():
    if request.authorization and request.authorization.username == 'sanjay' and request.authorization.password == 'sanjay':
        return 'Congrats!! You Have Logged In'

    return make_response('Could Verify The Credentials',401,{'WWW-Authenticate':'Basic realm="Login Required"'})

@app.route('/access')
@auth_required
def access():
    return 'Hey Kumar !!! Welcome'

@app.route('/anotherpage')
@auth_required
def anotherpage():
    return 'Hey Kumar !!! This is your another page'

if __name__ == '__main__':
    app.run(debug=True)
