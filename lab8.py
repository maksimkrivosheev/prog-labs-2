from flask import abort, Blueprint, render_template, request, make_response, redirect, session, jsonify


lab8 = Blueprint('lab8', __name__)

@lab8.route('/lab8/')
def main():
    return render_template("lab8/index.html")

courses = [
    {"name": "c++", "videos": 30, "price": 3000},
    {"name": "basic", "videos": 30, "price": 11110},
    {"name": "c#", "videos": 8, "price": 3000},    
    {"name": "sql", "videos": 3, "price": 32400},
    {"name": "afna", "videos": 30, "price": 60000},
    {"name": "c", "videos": 8, "price": 5000},
    {"name": "assembler", "videos": 3, "price": 3000},
    {"name": "pascal", "videos": 30, "price": 4000},
    {"name": "pyton", "videos": 8, "price": 3000}
]

@lab8.route('/lab8/api/courses/', methods=['GET'])
def get_courses():
    return jsonify(courses)

@lab8.route('/lab8/api/courses/<int:course_num>', methods=['GET'])
def get_course(course_num):
    if course_num not in range(0, len(get_courses())):
        abort(404)
    else:
        return courses[course_num]

@lab8.route('/lab8/api/courses/<int:course_num>', methods=['DELETE'])
def del_course(course_num):
    if course_num not in range(0, len(get_courses())):
        abort(404)
    else:
        del courses[course_num]
        return '', 204

@lab8.route('/lab8/api/courses/<int:course_num>', methods=['PUT'])
def put_course(course_num):
    if course_num not in range(0, len(get_courses())):
        abort(404)
    else:
        course = request.get_json()
        course[course_num] = course

@lab8.route('/lab8/api/courses/', methods=['POST'])
def add_course():
    course = request.get_json()
    course[course_num] = course
    return {"num": len(courses) - 1}

    
