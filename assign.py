"""
 Program takes a JSON input and gives its equivalent memory representation in bytes
"""

import json


def dict_fun(obj):
    """
    This function is used to calculate the total size taken up by the dictionary elements
    """
    dict_memory_sum = 0  # calculates the total memory used by fields in a dictionary
    for each_key in obj.keys():
        dict_obj_val = obj[each_key]
        if type(dict_obj_val) == list:
            dict_memory_sum = dict_memory_sum + list_fun(dict_obj_val)
        elif type(dict_obj_val) == dict:
            dict_memory_sum = dict_memory_sum + dict_fun(obj[each_key])
        else:
            dict_memory_sum = dict_memory_sum + norm_fun(obj[each_key])
    return dict_memory_sum + list_fun(obj.keys())


def list_fun(obj):
    """
    This function is used to calculate the total size taken up by the LIST elements
    """
    list_memory_sum = 0  # used to calculate total memory occupied by list elements
    for item in obj:
        if type(item) != dict:
            list_memory_sum = list_memory_sum + norm_fun(item)
        else:
            list_memory_sum = list_memory_sum + dict_fun(item)
    return list_memory_sum


def norm_fun(obj):
    """
    This function is used to calculate the total size taken up by all the other elements
    """
    if type(obj) == int or type(obj) == float:
        return 8

    elif type(obj) == str:
        return len(obj) + 1

    elif type(obj) == bool or type(obj) == "null":
        return 1

    elif type(obj) == list:
        return list_fun(obj)
    else:
        return dict_fun(obj)


if __name__ == "__main__":
    # data= '{"finance":{"error":{"code":"Unauthorized","description":"Invalid cookie"}},"category": "Household", "crawl_date": "20180726", "subcategory": false, "title": "Seventh Generation- 30 ct", "mrp": 7.5, "urlh": "1ef0f41e", "http_status": "200","ItemModList":[0,375,668,5,6], "pack_size":"med" , "available_price": 5}'
    JSON_DATA = '{"molde": [1,2,"hi"],"drogo": 12,"sai": false, "finance":{"error":{"code":"Unauthorized","description":"Invalid cookie"}}}'
    DICT_DATA = json.loads(JSON_DATA)  # stores the json into a dictionary
    print(dict_fun(DICT_DATA))
