import sqlite3


class Database:
    def __init__(self,baza_manzili):
        self.path_to_dp = baza_manzili

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_dp)

    def execute(self,sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql,parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())


    def add_user(self, id: int, name: str, email: str = None, language:str = 'uz'):
        sql = """
        INSERT INTO users(id, Name, email, language) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, name, email, language), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        sql = "SELECT * FROM users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return sql.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM users;", fetchone=True)



    def delete_users(self):
        self.execute("DELETE FROM users WHERE TRUE", commit=True)



    def user_qoshish(self, ism: str, tg_id:int, fam: str = None, username:str=None):
        sql = """
           INSERT INTO users(ism,fam,tg_id,username) VALUES(?, ?, ?, ?)
         """
        self.execute(sql, parameters=(ism,fam,tg_id,username), commit=True)

    def select_barcha_foydalanuvchilar(self):
        sql = """
        SELECT * FROM users
        """
        return self.execute(sql, fetchall=True)

    def select_barcha_menular(self):
        sql = """
        SELECT * FROM menu
        """
        return self.execute(sql, fetchall=True)

    def select_maxsulotlar(self, **kwargs):
        sql = "SELECT * FROM maxsulotlar WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchall=True)

    def select_maxsulot(self, **kwargs):
        sql = "SELECT * FROM maxsulotlar WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)


    def select_barcha_maxsulotlar(self):
        sql = """
        SELECT * FROM maxsulotlar
        """
        return self.execute(sql, fetchall=True)

def logger(statement):
    print(f"""
    __________________________________________________________
    Executing:
    {statement}
 
    __________________________________________________________
""")
