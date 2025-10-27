from connection import conn


def index():
    cursor = conn.cursor(dictionary=True)

    cursor.execute('SELECT * FROM courses')

    courses = cursor.fetchall()

    cursor.close()

    return courses


def create(name, cls):
    cursor = conn.cursor(dictionary=True)

    cursor.execute(f"INSERT INTO courses (name, class) VALUES ({name}, {cls})")

    conn.commit()

    cursor.close()


def update(course_id, column, value):
    cursor = conn.cursor(dictionary=True)

    cursor.execute(f"UPDATE courses SET {column} = {value} WHERE id = {course_id}")

    conn.commit()

    cursor.close()


def delete(course_id):
    cursor = conn.cursor(dictionary=True)

    cursor.execute(f"DELETE FROM courses WHERE id = {course_id}")

    conn.commit()

    cursor.close()


def show(course_id):
    cursor = conn.cursor(dictionary=True)

    cursor.execute(f"SELECT * FROM courses WHERE id = {course_id}")

    course = cursor.fetchone()

    cursor.close()

    return course
