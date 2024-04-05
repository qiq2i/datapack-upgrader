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
    for dirpath, dirnames, filenames in os.walk(input_folder):
        relative_dirpath = os.path.relpath(dirpath, input_folder)

        # 如果需要在输出文件夹中创建对应的子目录
        output_subdir = os.path.join(output_folder, relative_dirpath)
        if not os.path.exists(output_subdir):
            os.makedirs(output_subdir)

        for filename in filenames:
            if filename.endswith('.json'):
                input_file_path = os.path.join(dirpath, filename)
                output_file_path = os.path.join(output_subdir, filename)

                with open(input_file_path, 'r', encoding='utf-8') as input_file:
                    data_dict = json.load(input_file)

                # 更新数据字典（此处假设您已定义了update_json函数）
                updated_dict = loot_updata(data_dict)

                with open(output_file_path, 'w', encoding='utf-8') as output_file:
                    json.dump(updated_dict, output_file, ensure_ascii=False, indent=4)

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