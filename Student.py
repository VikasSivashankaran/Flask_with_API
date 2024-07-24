from flask import json


class Student:
    id = 0
    email = ''
    password = ''
    name = ''
    course=''

    def __init__(self, id, email, password, name,course ):
        self.id = id
        self.email = email
        self.password = password
        self.name = name
        self.course=course

    def __str__(self) -> str:
        return f"{self.id} - {self.email}  - {self.password} - {self.name} - {self.course})"

    def to_json(obj):
        return json.dumps(obj, default=lambda obj: obj.__dict__)
