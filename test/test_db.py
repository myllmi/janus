import json
from typing import Final

from db.mysql_dao import MySQLDao

db = MySQLDao()

SCHEMA: Final = 'order'

arr_table = []
print('--- Tables ---')
list_tables = db.get_tables(SCHEMA)
for table in list_tables:
    print(table)
    print('--- Columns ---')
    arr_column = []
    list_columns = db.get_columns(SCHEMA, table['TABLE_NAME'])
    for column in list_columns:
        print(column)
        dict_column = {
            "name": column['COLUMN_NAME'].upper(),
            "description": column['COLUMN_COMMENT'].upper(),
            "type": column['DATA_TYPE'].upper(),
            "size": column['CHARACTER_MAXIMUM_LENGTH'],
            "mandatory": False if column['IS_NULLABLE'] == 'YES' else True,
            "minLength": None if column['IS_NULLABLE'] == 'YES' else 1,
            "maxLength": None if column['IS_NULLABLE'] == 'YES' else column['CHARACTER_MAXIMUM_LENGTH'],
            "key": 'PK' if column['COLUMN_KEY'].upper() == 'PRI' else 'FK' if column['COLUMN_KEY'].upper() == 'MUL' else None,
        }
        arr_column.append(dict_column)
    print(arr_column)

    dict_table = {
        "name": table['TABLE_NAME'],
        "description": table['TABLE_COMMENT'],
        "columns": arr_column,
    }
    arr_table.append(dict_table)

    print('--- 1 to N ---')
    list_1m = db.get_fk_1m(SCHEMA, table['TABLE_NAME'])
    for fk in list_1m:
        print(fk)
    print('--- M to 1 ---')
    list_m1 = db.get_fk_m1(SCHEMA, table['TABLE_NAME'])
    for fk in list_m1:
        print(fk)
    print(f'')

print(arr_table)
print(json.dumps(arr_table, indent=4))