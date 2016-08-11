import urllib.request as ur
import json

abs_path_keys = []
abs_hierarchy = {}
is_list = type([])
is_dict = type({})
dict_stack = []

def traverse_dict():
    d = dict_stack[-1]
    for key in d:
        if type(d[key]) == is_dict:
            dict_stack.append(d[key])
            abs_path_keys.append(key)
            traverse_dict()
        else:
            path_string = abs_path_keys[0]
            for elements in abs_path_keys[1:]:
                path_string+="."+elements
            path_string += "."+key
            abs_hierarchy[path_string] = d[key]
    dict_stack.pop()
    abs_path_keys.pop()

def main():
    data = ''
    with ur.urlopen("https://api.github.com/repos/akshbn/cream/commits") as res:
        data = res.read()
    json_decoded = data.decode('utf-8')
    deser_json = json.loads(json_decoded)
    if is_dict == type(deser_json):
        abs_path_keys.append["json"]
        dict_stack.append(deser_json)
        traverse_dict()
    elif is_list == type(deser_json):
        len_deser = len(deser_json)
        iter_var = 0
        while iter_var < len_deser:
            str_initial = "json[{0}]".format(iter_var)
            abs_path_keys.append(str_initial)
            if type(deser_json[iter_var]) == is_dict:
                dict_stack.append(deser_json[iter_var])
                traverse_dict()
            if len(dict_stack) > 0:
                dict_stack.clear()
            if len(abs_path_keys) > 0:
                abs_path_keys.clear()
            iter_var+=1
    with open('ap.txt','w') as file:
        for key in abs_hierarchy:
            output_str = "{0} = {1}\n".format(key,abs_hierarchy[key])
            file.write(output_str)

if __name__ == '__main__':
    main()
