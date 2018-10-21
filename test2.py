# creating file and writing data
with open('Students.txt', 'w') as fout:
    for i in range(3):
        name = input("Enter the name of Student: ")
        class_name = input("Enter the class of the student: ")
        roll_no = input("Enter the roll number of the student: ")
        gpa = input("Enter the gpa of the student: ")
        fout.write('Name: ' + name + '\n' + 'Class: ' + class_name + '\n' + 'Roll no.: ' + roll_no + '\n'*2)
        print()

# inputting and displaying data
with open('Students.txt') as fin:
    for line in fin:
        if "Name" in line:
            print(line)
