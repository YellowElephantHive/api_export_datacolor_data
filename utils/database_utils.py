# TODO Formulate frequently used class in this file
import cx_Oracle
import pymssql
import pymysql
import sqlite3
import builtins
import pandas as pd
from pandas import DataFrame

from utils.DataBaseCore import BaseDatabaseExporter
from dataclasses import dataclass


@dataclass(order=True)
class OracleExporter(BaseDatabaseExporter):
    db_ip: str
    db_user: str
    db_password: str

    def isConnect(self, db_ip: str, db_user: str, db_password: str):
        try:
            conn = cx_Oracle.connect(db_ip, db_user, db_password)
            print('True')
            cursor = conn.cursor()
            return conn
        except Exception as e:
            raise Exception('Connection Fails')

    def query(self, sql: str, conn) -> DataFrame:
        df = pd.read_sql(sql, conn)
        return df

    def commit(self, db_drive, table_name, df):
        from sqlalchemy import create_engine
        engine = create_engine(db_drive, echo=True)
        pd.io.sql.to_sql(df, table_name, engine, index=False, if_exists='append')


@dataclass(order=True)
class MSSQLExporter(BaseDatabaseExporter):
    db_ip: str
    db_name: str
    db_user: str
    db_password: str

    def isConnect(self, db_ip: str, db_name: str, db_user: str, db_password: str):
        try:
            import pymssql
            conn = pymssql.connect(host=db_ip, user=db_user, password=db_password, database=db_name)
            print('True')
            cursor = conn.cursor
            return conn
        except Exception as e:
            raise Exception('Connection Fails')

    def query(self, sql: str, conn) -> DataFrame:
        df = pd.read_sql(sql, conn)
        return df

    def commit(self, db_drive, table_name, df):
        from sqlalchemy import create_engine
        engine = create_engine(db_drive, echo=True)
        pd.io.sql.to_sql(df, table_name, engine, index=False, if_exists='append')


@dataclass(order=True)
class MySQLExporter(BaseDatabaseExporter):
    db_ip: str
    port: str
    db_name: str
    db_user: str
    db_password: str

    def isConnect(self, db_ip: str, port: str, db_name: str, db_user: str, db_password: str):
        try:
            import pymysql
            conn = pymysql.connect(host=db_ip, port=port, user=db_user, passwd=db_password, db=db_name)
            print('True')
            cursor = conn.cursor()
            return conn
        except Exception as e:
            raise Exception('Connection fails')

    def query(self, sql: str, conn) -> DataFrame:
        df = pd.read_sql(sql, conn)
        return df

    def commit(self, db_drive, table_name, df):
        from sqlalchemy import create_engine
        engine = create_engine(db_drive, echo=True)
        pd.io.sql.to_sql(df, table_name, engine, intdex=False, if_exists='append')
