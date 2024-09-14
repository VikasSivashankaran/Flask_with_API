from flask import Flask, request, jsonify

from StudentService import student_service
from Student import Student

app = Flask(__name__)

service = student_service()

@app.route('/student', methods = ['POST'])
def create_student():
    data = request.get_json()
    student = Student(data['id'], data['email'], data['password'],  data['name'], data['course'])
    service.create_student(student)
    doc_json = Student.to_json(student)
    print("doc json ", doc_json)
    return doc_json
    

@app.route('/students', methods = ['GET'])
def get_all_student():
    students_list = service.get_students()
    return students_list

@app.route('/student/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = service.get_student(student_id)
    return student

@app.route('/delete_student/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    service.delete_student(student_id)
    return jsonify({'message': 'student deleted successfully', 'id': student_id})

@app.route('/update_student/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()
    student = Student(student_id, data['email'], data['password'], data['name'], data['course'])
    service.update_student(student)
    return jsonify({'message': 'student updated successfully', 'id': student_id})


@app.route('/')
def hello():
    return ' Flask is Running'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = '5001')

