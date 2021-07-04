from Handle.handle_json import get_value
import deepdiff
def get_result_json(apidata, status):
    data = get_value(apidata)
    if data:
        for i in data:
            message = i.get(status)
            if message:
                return message
    return None

def handle_result_json(dict1,dict2):
    if isinstance(dict1, dict) and isinstance(dict2, dict):
        cmp_dict = deepdiff.DeepDiff(dict1, dict2, ignore_order=True)
        if cmp_dict.get("dictionary_item_added"):
            return False
        else:
            return True



