import os
import psycopg2
from dbpkg.result import Result

class Postgres():
    def __init__(self):
        self.conn_str = os.environ['DATABASE_URL']
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(self.conn_str)
            #print('connected!')
            return self.conn
        except (Exception, psycopg2.DatabaseError) as error:
            print(error) 
            raise Exception(error)                     

    def disconnect(self, conn):
        if conn:
            conn.close()

    def commit(self):
        try:
            if self.conn:
                self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            raise Exception(error)              

    def rollback(self):
        try:
            if self.conn:
                self.conn.rollback()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            raise Exception(error)

    def query_one(self, query):
        try:
            result = Result()
            cur = self.conn.cursor()
            cur.execute(query)
            result.rows = cur.fetchone()
            result.rowcount = cur.rowcount
            cur.close()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            raise Exception(error)

    def query_all(self, query):
        try:
            result = Result()
            cur = self.conn.cursor()
            cur.execute(query)
            result.rows = cur.fetchall()
            result.rowcount = cur.rowcount
            cur.close()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            raise Exception(error)
    
    def query_many(self, query, quantity):
        try:
            result = Result()
            cur = self.conn.cursor()
            cur.execute(query)
            result.rows = cur.fetchmany(quantity)
            result.rowcount = cur.rowcount
            cur.close()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            raise Exception(error)
    
    def execute(self, query):
        try:
            cur = self.conn.cursor()
            cur.execute(query)
            cur.close()
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            self.conn.rollback()
            print(error)
            raise Exception(error)
            

    
