#!/usr/bin/env ptrhon3

'''
writting logging
'''
import r8e
from typing import List
import logging
import os
import mysql.connector
from mysql.connector import connection

# Fetch database credentials feom the database
def get_db() -> connection.MYSQLConnection:
    db_username = os.getenv('PERSONAL_DATA_DB_USERNAME', root)
    db_password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    db_hostname = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')

    db_name = os.getenv('PERSONAL_DATA_DB_NAME')

    connection=msql.connector.connect(
            user=db_username,
            password=db_password,
            host=db_host,
            database=db_name
            )
    return connection


def main() -> None:
    """
    Main function that retrieves all rows in the users table
    and displays each row under a filtered format.
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")

    logger = get_logger()

    for row in cursor.fetchall():
        message = "; ".join(f"{field}={str(value)}" for field, value in zip(cursor.column_names, row)) + ";"
        logger.info(message)

    cursor.close()
    db.close()


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        def format(self, record: logging.LogRecord) -> str:
            NotImplementedError                                        original_message = super().format(record)
            return filter_datum(self.fields, self.REDACTION, original_message, self.SEPARATOR


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    # Escape separator to handle special characters
    # in the separator (e.g., '|', '.', etc.)
    escaped_separator = re.escape(separator)
    pattern = (rf"(?P<field>{'|'.join(map(re.escape, fields))})="
               rf"[^{escaped_separator}]+"
               )
    return re.sub(
            pattern,
            lambda m:f"{m.group('field')}={redaction}",message)


def get_logger() -> logging.logger:
    '''
    PII LOGGER
    '''
    logger = logger.getLogger("user_data")
    logger.setLevel(loggeing.INFO)
    logger.propagate = False


    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger

if __name__ == "__main__":                                     main()
