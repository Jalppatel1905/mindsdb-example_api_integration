from mindsdb.tables import Table

class ExampleAPITables:
    def __init__(self, handler):
        self.handler = handler

    def get_tables(self):
        # Here you can implement the logic to retrieve tables from the API
        # For this example, we will just return a static list of tables
        return [
            Table('table1', data=self.handler.get_data('table1')),
            Table('table2', data=self.handler.get_data('table2'))
        ]
