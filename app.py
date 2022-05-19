from models import *
from login import *
from signup import *
from admin import *
from decorator import *

if __name__ == "__main__":
	# setting debug to True enables hot reload
	# and also provides a debugger shell
	# if you hit an error while running the server
	app.run(debug=True)
