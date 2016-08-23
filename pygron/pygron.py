import urllib.request as ur
import json

abs_path_keys = []
abs_hierarchy = {}
is_list = type([])
is_dict = type({})
dict_stack = []
inorder_paths = []

def traverse_dict():
    d = dict_stack[-1]
    for key in d:
        if type(d[key]) == is_dict:
            dict_stack.append(d[key])
            abs_path_keys.append(key)
            traverse_dict()
        elif type(d[key]) == is_list:
            iter_var = 0
            for list_element in d[key]:
                if type(list_element) == is_dict:
                    dict_stack.append(list_element)
                    str_list_path = "{0}[{1}]".format(key,iter_var)
                    abs_path_keys.append(str_list_path)
                    iter_var+=1
                    traverse_dict()
        else:
            path_string = abs_path_keys[0]
            for elements in abs_path_keys[1:]:
                path_string+="."+elements
            path_string += "."+key
            abs_hierarchy[path_string] = d[key]
            inorder_paths.append(path_string)
    dict_stack.pop()
    abs_path_keys.pop()

def main(json_data,output_to_file):
    deser_json = json.loads(json_data)
    if is_dict == type(deser_json):
        abs_path_keys.append("json")
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
    sorted_output = []
    for key in inorder_paths:
        output_str = "{0} = {1}".format(key,abs_hierarchy[key])
        sorted_output.append(output_str)
    if output_to_file:
        with open("pygron_output.txt",'w') as output_file:
            for element in sorted_output:
                output_file.write(element+'\n')
        print("Output written into pygron_output.txt")
    else:
        for element in sorted_output:
            print(element)

def json_url(url_to_get,output_to_file):
    data = ''
    with ur.urlopen(url_to_get) as res:
        data = res.read()
    json_decoded = data.decode('utf-8')
    main(json_decoded,output_to_file)

def json_file(file_to_get,output_to_file):
    data = ''
    with open(file_to_get,'r') as files:
        data = files.read()
    main(data,output_to_file)

if __name__ == '__main__':
    json_url("https://api.github.com/repos/akshbn/pygron/commits",True)
