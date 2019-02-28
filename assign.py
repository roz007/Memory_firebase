import json
'''         DOC STRING
 Program takes a JSON input and gives its equivalent memory representation in bytes'''

def dict_fun(obj):
    ''' 
    This function is used to calculate the total size taken up by the dictionary elements
    '''
    dict_memory_sum = 0 #calculates the total memory used by fields in a dictionary
    dict_key_sum = 0 #calulates the total memory used by keys in a dictionary

    dict_key_values_list = obj.keys()#extracts the keys from the dictionary and stores them in a list
    # print(dict_key_values_list)

    for items in dict_key_values_list:
        dict_obj_val = obj[items]

        if type(dict_obj_val) == list:
            dict_memory_sum = dict_memory_sum + list_fun(dict_obj_val)

        elif type(dict_obj_val) == dict:

            dict_temp = dict_fun(obj[items])
            dict_memory_sum = dict_memory_sum + dict_temp

        else:
            dict_memory_sum = dict_memory_sum + norm_fun(obj[items])

    dict_key_sum = dict_memory_sum + list_fun(dict_key_values_list)
    #Total sum of space is the sum of field values and keys from the dictionary
    return dict_key_sum


def list_fun(obj):
    ''' DOC STRING
    This function is used to calculate the total size taken up by the LIST elements
    '''
    list_memory_sum = 0#used to calculate total memory occupied by list elements
    for item in obj:
        # print(item)
        if type(item) != dict:
            list_memory_sum = list_memory_sum + norm_fun(item)

        else:
            list_memory_sum = list_memory_sum + dict_fun(item)

    return list_memory_sum


def norm_fun(obj):
    ''' DOC STRING
    This function is used to calculate the total size taken up by all the other elements
    '''
    if type(obj) == int or type(obj) == float:
        # print(obj)
        return 8

    elif type(obj) == str:
        # print(obj)
        return len(obj) + 1

    elif type(obj) == bool or type(obj) == null:
        # print(obj)
        return 1

    elif type(obj) == list:
        list_sum = list_fun(obj)
        return list_sum
    else:
        dict_sum = dict_fun(obj)
        # print(obj)
        return dict_sum


# data= '{"finance":{"error":{"code":"Unauthorized","description":"Invalid cookie"}},"category": "Household", "crawl_date": "20180726", "subcategory": false, "title": "Seventh Generation- 30 ct", "mrp": 7.5, "urlh": "1ef0f41e", "http_status": "200","ItemModList":[0,375,668,5,6], "pack_size":"med" , "available_price": 5}'
DATA = '{"molde": [1,2,"hi"],"drogo": 12,"sai": false, "finance":{"error":{"code":"Unauthorized","description":"Invalid cookie"}}}'

PER_DICT = json.loads(DATA)#stores the json into a dictionary

KEY_VAL = PER_DICT.keys()#is a list containing keys of the dictionary
BYTES = 0

for item in KEY_VAL:

    obj = PER_DICT[item]

    if obj != None:
        if type(obj) == dict:
            temp_count = dict_fun(obj)
            BYTES = BYTES + temp_count
        elif type(obj) == list:
            temp_count = list_fun(obj)
            BYTES = BYTES + temp_count
        else:
            temp_count = norm_fun(obj)
            BYTES = BYTES + temp_count

BYTES = BYTES + list_fun(KEY_VAL)
print(BYTES)
