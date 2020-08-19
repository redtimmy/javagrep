#!/usr/bin/env python3
#
# Author: Red Timmy Security <info@redtimmy.com>
#

import argparse
import os
from ruamel.yaml import YAML

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

yaml = YAML()
input_file = 'dict.yml'
cmd = "grep --color=always -R {} {} | sed 's/:/ : /'"


parser = argparse.ArgumentParser()
parser.add_argument("source", help="Specify source directory of Java files")
parser.add_argument("level", help="Specify level: 1 - only high risk, 2 - also medium risk, 3 - show all")
args = parser.parse_args()


for category, items in yaml.load(open(input_file)).items():
    print(bcolors.BOLD + "Category: " + str(category) + bcolors.ENDC)
    print(bcolors.BOLD + "-------------" + bcolors.ENDC)
    for item in items:
        if int(item['level']) <= int(args.level):
            print(bcolors.OKGREEN + "Keyword: " + item['keyword'] + bcolors.ENDC) 
            exitcode = os.system(cmd.format(item['keyword'], args.source))
            hint = item['desc']
            if exitcode == 0 and hint is not None:
                print(bcolors.OKBLUE + "Hint: " + hint + bcolors.ENDC)
