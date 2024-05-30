from mindsdb.tables import Table

class StudentTables:
    def __init__(self, handler):
        self.handler = handler

    def get_tables(self):
        students_data = self.handler.get_data('students')
        grades_data = self.handler.get_data('grades')

        students_table = Table('students', data=students_data)
        grades_table = Table('grades', data=grades_data)

        return [students_table, grades_table]
