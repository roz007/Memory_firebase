# Memory_firebase
Program takes a JSON input and gives its equivalent memory representation in bytes


Requirements:
Python 3.6.6+

This program uses recurssion extensively.We use three main functions to calculate the total memory of the JSON in bytes.

1) dict_fun(object) to calculate the memory used by dictionary elements
2) list_fun(object) to calculate the memory used by list elemects
3) norm_fun(object) to calculate the memory used by int,float,string and so on

Intially a json is processed and stored into  a dictionary, the keywords are then extracted from the dictionary and storedin a list.
Each object from the dictionary is then parsed and sorted according to their type.
On parsing the dictinary if a list is encountered then the object is passed to the list_fun(),
if a dictionary is encountered then the object is passed to the dict_fun()
and every other object is passed through norm_fun()

After all elements are parsed we get the total space occupied by field elements within the dictionary.
We can find the space occupied by the keys in the dictionary by passing the list containg the dictionary elements to the list_fun()

all the results are added up and on completion we recieve the total memory occupied by the json in bytes


Firebase standards are used to calculate the total memory.



