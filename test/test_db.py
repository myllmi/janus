from typing import Final

from db.mysql_dao import MySQLDao

db = MySQLDao()

SCHEMA: Final = 'order'

print('--- Tables ---')
list_tables = db.get_tables(SCHEMA)
for table in list_tables:
    print(table)
    print('--- Columns ---')
    list_columns = db.get_columns(SCHEMA, table['TABLE_NAME'])
    for column in list_columns:
        print(column)
    print('--- 1 to N ---')
    list_1m = db.get_fk_1m(SCHEMA, table['TABLE_NAME'])
    for fk in list_1m:
        print(fk)
    print('--- M to 1 ---')
    list_m1 = db.get_fk_m1(SCHEMA, table['TABLE_NAME'])
    for fk in list_m1:
        print(fk)
    print(f'')
