#coding=utf-8
import yaml
from ruamel import yaml

with open('test_data_list.yaml', 'rb') as f:
    res = yaml.load(f)
print(res)


