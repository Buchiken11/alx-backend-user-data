#!/usr/bin/env ptrhon3

'''
writting logging
'''
import re
from typing import List


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
            lambda m:
            f"{m.group('field')}={redaction}",
            message
            )
