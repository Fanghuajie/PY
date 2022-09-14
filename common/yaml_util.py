import os

import yaml

class YamlUtil:

    # 读取extract.yaml文件
    def read_extract_yaml(self, key):
        with open(os.getcwd()+"/extract.yml", mode="r", encoding="utf-8") as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value[key]

    # 写入extract.yaml文件
    def write_extract_yaml(self, data):
        with open(os.getcwd()+"/extract.yml", mode="a", encoding="utf-8") as f:
            value = yaml.dump(data=data, stream=f, allow_unicode=True)
    # mode='w'写入，mode='a'追加

    # 清除数据
    def clear_extract_yaml(self):
        with open(os.getcwd()+"/extract.yml", mode="w", encoding="utf-8") as f:
            f.truncate()

    # 读取测试数据
    def read_data_yaml(self, yaml_name):
        with open(os.getcwd() +'/testcase/' + yaml_name, mode="r", encoding="utf-8") as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value
