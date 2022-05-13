from main import *
import pandas as pd

#route to get all students details

# @app.route('/students',methods=['POST'])
# def add_student_details():
#     #function to add new student details to our db
#     request_data=request.json
#     student.add_details(request_data["student_id"],request_data["first_name"],request_data["last_name"],request_data["standard"],request_data["age"],request_data["gender"])
#     response = Response("Student Details Added", 201, mimetype='application/json')
#     return response

@app.route('/students',methods=['POST'])
def add_student_details():
    #function to add new student details to our db

    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print("File Uploaded Sucessfully!!!!!")

    input_cols = ['student_id', 'first_name', 'last_name', 'standard', 'age', 'gender']
    input_df = pd.read_csv(UPLOAD_FOLDER + 'student_details_input.csv',names=input_cols, header=None)

    for index, row in input_df.iterrows():
        student.add_details(row['student_id'], row['first_name'], row['last_name'], row['standard'], row['age'], row['gender'])

    response = Response("Student Details Added",status=201,mimetype='application/json')
    return response

@app.route('/students',methods=['GET'])
def all_students_details():
    #function to get all student details from db
    return jsonify({'Students':student.get_all_student_details()})

@app.route('/students/<int:student_id>',methods=['GET'])
def student_details_route(student_id):
    try:
        return_value=student.get_student_details(student_id)
        return jsonify(return_value)
    except:
        return "Student Record Is Not Found In the Database"

# route to update student details with PUT method
@app.route('/students/<int:id>', methods=['PUT'])
def update_student_details(id):
    #Function to edit student details in our database using movie id
    request_data = request.json
    student.update_student_details(id,request_data["first_name"],request_data["last_name"],request_data["standard"],request_data["age"],request_data["gender"])
    response = Response("Student Details Updated", status=200, mimetype='application/json')
    return response

# route to delete student details with DELETE method
@app.route('/students/<int:student_id>',methods=['DELETE'])
def delete_student_details(student_id):
    student.delete_student_details(student_id)
    response=Response("Student Details Deleted",status=200,mimetype='application/json')
    return response

if __name__ == '__main__':
    app.debug=True
    app.run(debug=True)
