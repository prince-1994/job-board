from psycopg2._psycopg import connection

class UserRepository:
    def __init__(self, conn: connection):
        self.conn = conn

    def create(self, email: str):
        with self.conn:
            with self.conn.cursor() as cur:
                data = cur.execute(
                    f"""Insert Into 
                        data.user(email, created_on, created_by) 
                        values('{email}', current_timestamp, 'self')""")

    def get_all(self):
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute("SELECT id, email from data.user")
                data = cur.fetchall()
                print(data)

class JobRepository:
    def __init__(self, conn: connection):
        self.conn = conn

class CompanyRepository:
    def __init__(self, conn: connection):
        self.conn = conn