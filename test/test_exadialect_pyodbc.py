import EXASOL

with EXASOL.connect('ws://127.0.0.1:8888', 'sys', 'exasol') as connection:
     with connection.cursor() as cursor:
          cursor.executemany("SELECT 'test' FROM DUAL",[[]])



from sqlalchemy.dialects import registry
registry.register("ws", "sqlalchemy_exasol.pyodbc", "EXADialect_pyodbc")

from sqlalchemy import create_engine

eng = create_engine('ws://sys:exasol@127.0.0.1:8888/')

eng.connect()
# from sqlalchemy_exasol.pyodbc import EXADialect_pyodbc


# dialect = EXADialect_pyodbc()

# c=dialect.connect('ws://127.0.0.1:8888', 'sys', 'exasol')
# print(c)
