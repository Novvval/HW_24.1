import os
import re
from typing import List, TextIO, Union, Any

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
file_path = os.path.join(DATA_DIR, "apache_logs.txt")


def query(cmd: Any, value: Any, file_list: Union[List[str], TextIO]) -> Any:
    if cmd == "filter":
        result = list(filter(lambda row: value in row, file_list))
        return result
    if cmd == "map":
        result = [row.split()[int(value)] for row in file_list]
        return result
    if cmd == "unique":
        result = list(set(file_list))
        return result
    if cmd == "sort":
        reverse = value == "desc"
        result = sorted(file_list, reverse=reverse)
        return result
    if cmd == "limit":
        result = list(file_list)[:int(value)]
        return result
    if cmd == "regex":
        r = re.compile(value)
        result = list(filter(r.findall, file_list))
        return result
