# -*- coding: utf-8 -*-
import pandas.io.sql as psql
from sqlalchemy import create_engine
import config as conf

class DB_Drive():

    #connect to database
    def __init__(self):
        #parameter
        dbms = conf.postgresql["DBMS"]
        host = conf.postgresql["host"]
        username = conf.postgresql["username"]
        password = conf.postgresql["password"]
        port = conf.postgresql["port"]
        db_name = conf.postgresql["db_name"]

        # dialect+driver://username:password@host:port/database
        db = "{0}://{1}:{2}@{3}:{4}/{5}".format(dbms, username, password, host, port, db_name)
        engine = create_engine(db)
        c = engine.connect()
        self.conn = c.connection

    def query(self, sql):
        # read data from database
        df = psql.read_sql(sql, con=self.conn)
        return df