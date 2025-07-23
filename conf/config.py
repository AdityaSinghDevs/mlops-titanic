import os
import yaml 

with open("conf/config.yaml", "r") as f:
    config = yaml.saf_load(f)

raw_path = config['data']['raw_path']
