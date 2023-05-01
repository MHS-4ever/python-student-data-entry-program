import csv

def get_num_students():
  try:
    num_students = int(input("Enter the number of students: "))
    return num_students
  except ValueError:
    print("Invalid input. Please enter a valid integer.")
    return get_num_students()


def get_student_data(num_students):
  student_data = []
  for i in range(1,num_students + 1):
    try:
      student = {}
      student['Name'] = input("Enter student name: ")
      student['Age'] = int(input("Enter student age: "))
      student['Gender'] = input("Enter student gender: ")
      student['Class'] = input("Enter student class: ")
      student_data.append(student)
    except ValueError:
      print("Invalid input. Please enter a valid integer for age.")
      return get_student_data(num_students)
    
  return student_data


def save_data_to_csv(student_data):
  try:
    with open('student_data.csv', 'w', newline='') as csvfile:
      fieldnames = ['Name', 'Age', 'Gender', 'Class']
      writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
      writer.writeheader()
      for student in student_data:
        writer.writerow(student)
  except IOError:
    print("Error saving data to file.")


def retrieve_data_from_csv():
  try:
    with open('student_data.csv', 'r') as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
        print(row['Name'], row['Age'], row['Gender'], row['Class'])
  except IOError:
    print("Error reading data from file.")


def main():
  try:
    print('If you want to enter Data enter "0"\nIf you want to retrieve Data enter "1"\n')
    run = int(input('Enter a number: '))
    if run == 1:
      retrieve_data_from_csv()
    elif run == 0:
      num_students = get_num_students()
      student_data = get_student_data(num_students)
      save_data_to_csv(student_data)
    else:
      print('Enter a valid number')
      main()
    return run
  except ValueError:
    print('An error occurred:')
    return main()

main()    
