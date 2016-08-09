import urllib.request as ur
import json

def main():
    data = ''
    with ur.urlopen("https://api.github.com/repos/akshbn/cream/commits") as res:
        data = res.read()
    json_decoded = data.decode('utf-8')
    deser_json = json.loads(json_decoded)
    pygron_data = []
    for dicts1 in deser_json:
        for s in dicts1:
            d = "{0}:{1}".format(s,dicts1[s])
            print(d)
            pygron_data.append(d)
    # print(pygron_data)

if __name__ == '__main__':
    main()
