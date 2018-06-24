class Student(object):
  def __init__(self, name, grade_point_average):
    self.name = name
    self.grade_point_average = grade_point_average
  
  def __lt__(self, other):
    print("In overrided lt operator")
    return self.name < other.name
    
  
students = [
  Student('A', 4.0),
  Student('C', 3.0),
  Student('B', 2.0),
  Student('D', 3.2)
]

# sort according to __lt__ defined in Student. students remain unchanged.
sorted_students = sorted(students)
print([student.name for student in sorted_students])
students.sort(key=lambda student: student.grade_point_average)
print([(student.name, student.grade_point_average) for student in students])
