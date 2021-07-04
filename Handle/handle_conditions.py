import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)
from Handle.handle_excel import handleexcel
import json
import jsonpath_rw import parse
def split_data(condition):
    (case_id, rule_data) = condition.split('>')
    return case_id, rule_data
def get_depend_data(data):
     case_id = split_data(data)[0]
     row = handleexcel.get_row_number(case_id)
     depend_data = handleexcel.get_cell_value(row, 12)
     return depend_data


 def get_depend_field(res_data,key):
     json_exe = parse(key)
     madle = json_exe.find(res_data)
     return [match.value for match in madle][0]
 def get_data(data):
     rule_data = split_data(data)[1]
     res_data = get_depend_data(data)
     res_data = json.loads(res_data)
     dependdata = get_depend_field(res_data, rule_data)
     return dependdata

