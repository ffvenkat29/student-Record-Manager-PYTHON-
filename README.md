Student Record Manager (Python)
   This is a beginner-friendly Student Record Manager implemented in Python.It allows users to add, view, update, and delete student information using a clean, menu-based interface.

Features
  Add New Student
    Store student:
      - Name
      - Roll number
      - Marks
      - Other info (based on code)

 View Student Details
      - Displays saved information in a formatted way.

Update Student Information
      - Modify marks, name, or any stored field.

Delete Student
      -  Remove a record from the system.

View All Students
      - List all student records at once.

Concepts Used:
    - Python functions / classes
    - Dictionary / list storage
    - Menu-driven loop
    - If–else logic
    - Data validation

File Included:
  Student Record Manager.py

'''
Example Code Snippet
class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Roll No: {self.roll}")
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
'''
Future Enhancements:
    
    - Save records to file (CSV/JSON)
    - Search by name or roll
    - Sorting
Attendance system

GUI (Tkinter) version
