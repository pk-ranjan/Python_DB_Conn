import psycopg2
from config import config


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        return cur, conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        if conn is not None:
            conn.close()
            print('Database connection closed.')
        raise


def insert_dummy_students():
    cur, conn = connect()
    # Define the INSERT statement
    insert_statement = "INSERT INTO students (first_name, last_name, age, gender, email, address) VALUES (%s, %s, %s, " \
                       "%s, %s, %s)"

    # Define the student records
    students = [
        ("John", "Doe", 20, "Male", "john.doe@example.com", "123 Main St"),
        ("Jane", "Smith", 21, "Female", "jane.smith@example.com", "456 Elm St"),
        ("Michael", "Johnson", 19, "Male", "michael.johnson@example.com", "789 Oak St"),
        ("Emily", "Brown", 22, "Female", "emily.brown@example.com", "321 Maple Ave"),
        ("David", "Taylor", 20, "Male", "david.taylor@example.com", "654 Pine Rd"),
        ("Sophia", "Anderson", 21, "Female", "sophia.anderson@example.com", "987 Birch Ln"),
        ("Daniel", "Wilson", 19, "Male", "daniel.wilson@example.com", "135 Cedar St"),
        ("Olivia", "Thomas", 22, "Female", "olivia.thomas@example.com", "468 Walnut Dr"),
        ("Alex", "Lee", 20, "Male", "alex.lee@example.com", "753 Cherry Ave"),
        ("Ava", "Harris", 21, "Female", "ava.harris@example.com", "246 Spruce Blvd")
    ]

    # Execute the INSERT statements for each student record
    for student in students:
        cur.execute(insert_statement, student)

    # Commit the changes to the database
    conn.commit()

    # Close the cursor and the database connection
    cur.close()
    print("closing the connection to the database")
    print("--------------------------------")
    conn.close()


def insertStudent():
    cur, conn = connect()
    student = get_student_details_from_user()

    # Define the INSERT statement
    insert_statement = "INSERT INTO students (first_name, last_name, age, gender, email, address) VALUES (%s, %s, %s, " \
                       "%s, %s, %s)"

    # Execute the INSERT statement with the student details
    cur.execute(insert_statement, (
        student['first_name'],
        student['last_name'],
        student['age'],
        student['gender'],
        student['email'],
        student['address']
    ))

    # Commit the changes to the database
    conn.commit()

    print("Student inserted successfully!")
    cur.close()
    conn.close()



def get_student_details_from_user():
    student = {}

    # Prompt the user to enter student details
    student['first_name'] = input("Enter the first name of the student: ")
    student['last_name'] = input("Enter the last name of the student: ")
    student['age'] = int(input("Enter the age of the student: "))
    student['gender'] = input("Enter the gender of the student: ")
    student['email'] = input("Enter the email address of the student: ")
    student['address'] = input("Enter the address of the student: ")

    return student


def getAllStudents():
    cur, conn = connect()
    query = "select * from students"
    cur.execute(query)
    students = cur.fetchall()
    for student in students:
        print("ID:", student[0])
        print("First Name:", student[1])
        print("Last Name:", student[2])
        print("Age:", student[3])
        print("Gender:", student[4])
        print("Email:", student[5])
        print("Address:", student[6])
        print()

    cur.close()
    print("closing the connection to the database")
    print("--------------------------------")
    conn.close()


if __name__ == '__main__':
    insertStudent()
