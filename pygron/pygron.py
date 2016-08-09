import urllib.request as ur
import json

abs_path_keys = []
abs_hierarchy = {}
is_list = type([])
is_dict = type({})

def is_dict_recursive(dict_within,abs_hierarchy1,abs_path_keys):
    for key in dict_within:
        if is_dict == dict_within[key]:
            k = abs_path_keys[-1]
            k += ".{0}".format(key)
            abs_path_keys.append(k)
            is_dict_recursive(dict_within[key],abs_hierarchy1,abs_path_keys)
        else:
            print(key)
            print(abs_path_keys[-1])
            abs_hierarchy1[abs_path_keys[-1]]=dict_within[key]
            abs_path_keys.pop()
            return abs_hierarchy1

def main():
    data = ''
    with ur.urlopen("https://api.github.com/repos/akshbn/cream/commits") as res:
        data = res.read()
    json_decoded = data.decode('utf-8')
    deser_json = json.loads(json_decoded)
    pygron_data = []
    # abs_path_keys = ["json"]
    val = 0
    for dicts1 in deser_json:
        # abs_path = {}
        for s in dicts1:
            temp_path = "json[{0}].{1}".format(val,s)
            abs_path_keys.append(temp_path)
            if is_dict == type(dicts1[s]):
                # abs_path_keys.append(s)
                x = is_dict_recursive(dicts1[s],{},abs_path_keys)
                for f in  x:
                    abs_hierarchy[f]=x[f]
                # for f in y:
                #     abs_path_keys.append(f)
            else:
                abs_hierarchy[temp_path] = dicts1[s]
            # d = "json[{2}]{0}.{1}".format(s,dicts1[s],val)
            # print(d)
            # pygron_data.append(d)
        val += 1
    with open('ap.txt','w') as file:
        for key in abs_hierarchy:
            output_str = "{0} = {1}\n".format(key,abs_hierarchy[key])
            file.write(output_str)

if __name__ == '__main__':
    main()
