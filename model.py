"""
Database layer using pyodbc for the LMS Project.
Final Clean Version.
"""
from __future__ import annotations
import os
from typing import Any, List, Optional, Sequence, Tuple
import pyodbc

class Database:
    def __init__(self, connection_string: Optional[str] = None) -> None:
        default_conn_str = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=AGMAD_RAGAB;" 
            "DATABASE=EduMess_Project;"
            "Trusted_Connection=yes;"
        )

        self.connection_string = connection_string or os.getenv(
            "DB_CONNECTION_STRING",
            default_conn_str,
        )
        self.conn = pyodbc.connect(self.connection_string)
        self.session = self.conn.cursor()

    def execute_query(self, sql: str, params: Optional[Sequence[Any]] = None) -> None:
        self.session.execute(sql, params or [])
        self.conn.commit()

    def execute_scalar(self, sql: str, params: Optional[Sequence[Any]] = None) -> Any:
        self.session.execute(sql, params or [])
        row = self.session.fetchone()
        self.conn.commit()
        return row[0] if row else None

    def fetch_all(self, sql: str, params: Optional[Sequence[Any]] = None) -> List[Tuple[Any, ...]]:
        self.session.execute(sql, params or [])
        return self.session.fetchall()

    def close(self):
        self.session.close()
        self.conn.close()