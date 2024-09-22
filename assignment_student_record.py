def manage_student_database():
    students = []
    student_id = 1
    
    while True:
        name = input("Enter the student's name (or type 'stop' to finish): ").strip()
        
        if name.lower() == 'stop':
            break
        
        if any(student[1] == name for student in students):
            print(f"Duplicate found: {name} is already in the list.")
        else:
            students.append((student_id, name))
            student_id += 1
    
    print("\nComplete list of students:")
    for student in students:
        print(student)
    
    print("\nIndividual student details:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}")
    
    total_students = len(students)
    print(f"\nTotal number of students: {total_students}")
    
    total_name_length = sum(len(student[1]) for student in students)
    print(f"Total length of all student names combined: {total_name_length}")
    
    if students:
        longest_name_student = max(students, key=lambda student: len(student[1]))
        shortest_name_student = min(students, key=lambda student: len(student[1]))
        print(f"Student with the longest name: {longest_name_student[1]} (ID: {longest_name_student[0]})")
        print(f"Student with the shortest name: {shortest_name_student[1]} (ID: {shortest_name_student[0]})")
    else:
        print("No students in the database.")
        
manage_student_database()
