# Select query
from dbconfig import dbconfig
from Student import Student
import json

class student_service:

    def get_students(self):
        conn = dbconfig.open_connection()
        cur = conn.cursor()
        cur.execute("select * from student")
        output = cur.fetchall()

        students_list = []
        for i in output:
            print("select query output ",i)
            student = Student(i[0], i[1], i[2],"Dummy", i[3]);
            students_list.append(json.loads(student.to_json()))

        dbconfig.close_connection(conn)
        return students_list

    def get_student(self, student_id):
        conn = dbconfig.open_connection()
        cur = conn.cursor()
        cur.execute("select * from student where id = " + str(student_id))
        output = cur.fetchall()
        student = ''
        for i in output:
            print("select query output ", i)
            student = Student(i[0], i[1], i[2], "Dummy", i[3]);

        dbconfig.close_connection(conn)
        return student.to_json()

    def insert_static_value(student_list):
        conn = dbconfig.open_connection()
        cur = conn.cursor()
        cur.execute("""
                    insert into student(id, email, password, name, course ) values ( %s, %s, %s, %s, %s)
                    """,
                    (11, 'test@test.com', 'password', 'test', 'AIML'))
        print(conn.insert_id())
        conn.commit()

    def create_student(self, student):
        conn = dbconfig.open_connection()
        cur = conn.cursor()
        cur.execute("""
                insert into student(id, email, password, name,course ) values ( %s, %s, %s, %s, %s)
                """,
                    (student.id, student.email, student.password, student.name, student.course))
        print(conn.insert_id())
        conn.commit()

    def insert_dynamic_value(student_list):
        conn = dbconfig.open_connection()
        cur = conn.cursor()
        for student in student_list:
            cur.execute("""
                 insert into student(id, email, password, name, course ) values ( %s, %s, %s, %s, %s)
                 """,
                        (student.id, student.email, student.password, student.name, student.course))
        print(conn.insert_id())
        conn.commit()

    def delete_student(self,student_id):
        conn = dbconfig.open_connection()
        cur = conn.cursor()
        cur.execute("DELETE from student where id = " + str(student_id))
        conn.commit()


    def update_student(self, student):
        conn = dbconfig.open_connection()
        cur = conn.cursor()
        cur.execute("""
            UPDATE student
            SET email = %s, password = %s, name = %s ,course = %s
            WHERE id = %s
            """,
            (student.email, student.password, student.name,student.course, student.id))
        conn.commit()
        conn.close()
    


# user_service = user_service()
# user_service.get_users()
# user_service.get_user('1919191919192')
# user1 = User(1,'vikas@test.com', 'password','USER', 'test')
# print("user ", user1)
# user_list = []
# user_service.insert_static_value(user_list)

# user_service.insert_dynamic_value(user_list)
# # user_service.get_user('3333')