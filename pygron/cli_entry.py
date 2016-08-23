import argparse
from .pygron import json_url,json_file

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v","--version",action="version",version="%(prog)s 0.2.9",help="Displays the version of pygron in use")
    parser.add_argument("-f","--file",action="store_true",help="Tells pygron to read json from a file")
    parser.add_argument("url",type=str,help="The url from which the json is obtained.\
    When -f is provided the path to the json file is required")
    parser.add_argument("-w","--write",action="store_true",help="Pygron writes output to a file")

    cli_arg = parser.parse_args()
    if cli_arg.file:
        if cli_arg.write:
            json_file(cli_arg.url,True)
        else:
            json_file(cli_arg.url,False)
    else:
        if cli_arg.write:
            json_url(cli_arg.url,True)
        else:
            json_url(cli_arg.url,False)

# if __name__ == '__main__':
#     main()
