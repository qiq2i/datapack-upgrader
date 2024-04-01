import os
import json
import nbt_to_components

# 指定目录路径
directory_path = '测试文件'
file_name = 'bat.json'

# 构建完整文件路径
json_file_path = os.path.join(directory_path, file_name)

# 确保文件存在
if os.path.isfile(json_file_path):
    # 读取并解析 JSON 文件
    with open(json_file_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
else:
    print(f"File '{file_name}' not found in directory '{directory_path}'.")

def loot_updata(loot_dict:dict):
    for i in loot_dict.get("pools",[]):#打开随机池pools列表
        for j in i.get("entries",[]):#打开entries列表
            Item_id = j.get("name","written_book")
            for k in j.get("functions",[]):#打开functions列表
                if k.get('function','') == 'set_nbt':#是否是set_nbt函数，是的话，更新并替换成
                    print(k.get('tag'))
    return None

print(loot_updata(json_data))