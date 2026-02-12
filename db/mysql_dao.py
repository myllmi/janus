from db.dao import Dao


class MySQLDao(Dao):
    def get_tables(self, _schema):
        with self.db.cursor(dictionary=True) as cursor_get_tables:
            sql = ("SELECT table_name, table_comment FROM information_schema.tables WHERE table_schema = %s AND table_type = "
                   "'BASE TABLE'")
            cursor_get_tables.execute(sql, (_schema,))
            return cursor_get_tables.fetchall()

    def get_columns(self, _schema, _table):
        with self.db.cursor(dictionary=True) as cursor_get_columns:
            sql = ("SELECT table_name, column_name, is_nullable, column_default, column_comment, "
                   "column_key, data_type, character_maximum_length FROM information_schema.columns "
                   "WHERE table_schema = %s AND table_name = %s ORDER BY ordinal_position")
            cursor_get_columns.execute(sql, (_schema, _table,))
            return cursor_get_columns.fetchall()

    def get_fk_1m(self, _schema, _table):
        with self.db.cursor(dictionary=True) as cursor_get_foreign_keys:
            sql = ("SELECT kcu.constraint_name, kcu.table_name AS child_table, kcu.column_name AS child_column, "
                   "kcu.referenced_table_name AS parent_table, kcu.referenced_column_name AS parent_column FROM "
                   "information_schema.key_column_usage kcu WHERE kcu.table_schema = %s AND "
                   "kcu.referenced_table_name = %s")
            cursor_get_foreign_keys.execute(sql, (_schema, _table,))
            return cursor_get_foreign_keys.fetchall()

    def get_fk_m1(self, _schema, _table):
        with self.db.cursor(dictionary=True) as cursor_get_foreign_keys:
            sql = ("SELECT kcu.constraint_name, kcu.table_name AS child_table, kcu.column_name AS child_column, "
                   "kcu.referenced_table_name AS parent_table, kcu.referenced_column_name AS parent_column FROM "
                   "information_schema.key_column_usage kcu WHERE kcu.table_schema = %s AND "
                   "kcu.table_name = %s  AND kcu.referenced_table_name IS NOT NULL")
            cursor_get_foreign_keys.execute(sql, (_schema, _table,))
            return cursor_get_foreign_keys.fetchall()