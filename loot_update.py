import os
import json
import nbt_to_components

"""# 指定目录路径
''directory_path = '测试文件'
file_name = 'bat.json'''
"""
'''# 构建完整文件路径
json_file_path = os.path.join(directory_path, file_name)

# 确保文件存在
if os.path.isfile(json_file_path):
    # 读取并解析 JSON 文件
    with open(json_file_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
else:
    print(f"File '{file_name}' not found in directory '{directory_path}'.")'''

def process_json_files(input_folder, output_folder):
    if not os.path.exists(output_folder):#检测输出路径是否不存在，不存在则创建
        os.makedirs(output_folder)

    for dirpath, _, filenames in os.walk(input_folder):#使用 os.walk 函数遍历输入文件夹及其所有子文件夹，找到所有以 .json 结尾的文件
        for filename in filenames:
            if filename.endswith('.json'):
                input_file_path = os.path.join(dirpath, filename)
                output_file_path = os.path.join(output_folder, filename)

                with open(input_file_path, 'r') as input_file:
                    data_dict = json.load(input_file)

                updated_dict = loot_updata(data_dict)

                with open(output_file_path, 'w') as output_file:#创建输出文件的路径，与输入文件在同一相对路径下但在输出文件夹内
                    json.dump(updated_dict, output_file, ensure_ascii=False, indent=4)#使用 json.dump 函数将更新后的字典写入输出文件，设置 ensure_ascii=False 以支持非ASCII字符，并使用 indent=4 进行格式化输出。

def loot_updata(loot_dict:dict): #输入json文件的dict格式，输出修改后的dict格式。
    for i in loot_dict.get("pools",[]):#打开随机池pools列表
        for j in i.get("entries",[]):#打开entries列表
            Item_id = j.get("name","written_book")
            for k in j.get("functions",[]):#打开functions列表
                if k.get('function','') == 'set_nbt' or k.get('function','') == 'minecraft:set_nbt':#是否是set_nbt函数，是的话，更新并替换成
                    k['function'] = 'set_components'
                    print(Item_id,k.get('tag'))
                    print(nbt_to_components.transfer(Item_id,k.get('tag'),3))
                    k['components'] =(nbt_to_components.transfer(Item_id,k.pop('tag'),3))
    return loot_dict

#print(loot_updata(json_data))

# 指定要写入的JSON文件路径
'''output_file_path = "output_file.json"

# 使用 'w' (write) 模式打开或创建文件
with open(output_file_path, "w", encoding="utf-8") as json_file:
    # 使用 json.dump() 将字典写入文件
    json.dump(loot_updata(json_data), json_file, ensure_ascii=False, indent=4)'''