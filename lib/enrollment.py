from datetime import datetime, timedelta

class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []

    def enroll(self, course):
        if isinstance(course, Course):
            enrollment = Enrollment(self, course)
            self._enrollments.append(enrollment)
            course.add_enrollment(enrollment)
        else:
            raise TypeError("course must be an instance of Course")

    def get_enrollments(self):
        return self._enrollments.copy()

    def __str__(self):
        return f"Student: {self.name}"

class Course:
    def __init__(self, title):
        self.title = title
        self._enrollments = []

    def add_enrollment(self, enrollment):
        if isinstance(enrollment, Enrollment):
            self._enrollments.append(enrollment)
        else:
            raise TypeError("enrollment must be an instance of Enrollment")

    def get_enrollments(self):
        return self._enrollments.copy()

    def __str__(self):
        return f"Course: {self.title}"

class Enrollment:
    all = []
    
    def __init__(self, student, course):
        if isinstance(student, Student) and isinstance(course, Course):
            self.student = student
            self.course = course
            self._enrollment_date = datetime.now()
            type(self).all.append(self)
        else:
            raise TypeError("Invalid types for student and/or course")

    def get_enrollment_date(self):
        return self._enrollment_date

    def get_duration_since_enrollment(self):
        current_date = datetime.now()
        date_range = [self._enrollment_date + timedelta(days=x) for x in range((current_date - self._enrollment_date).days + 1)]
        return date_range

    def __str__(self):
        return f"Enrollment: {self.student.name} in {self.course.title} on {self._enrollment_date}"