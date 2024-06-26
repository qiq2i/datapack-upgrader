import os
import json
import nbt_to_components

def process_json_files(input_folder, output_folder):
    for dirpath, dirnames, filenames in os.walk(input_folder):
        relative_dirpath = os.path.relpath(dirpath, input_folder)

        # 输出文件夹中创建对应的子目录
        output_subdir = os.path.join(output_folder, relative_dirpath)
        if not os.path.exists(output_subdir):
            os.makedirs(output_subdir)

        for filename in filenames:
            if filename.endswith('.json'):
                input_file_path = os.path.join(dirpath, filename)
                output_file_path = os.path.join(output_subdir, filename)

                with open(input_file_path, 'r', encoding='utf-8') as input_file:
                    data_dict = json.load(input_file)

                # 更新数据字典
                updated_dict = loot_updata(data_dict)

                with open(output_file_path, 'w', encoding='utf-8') as output_file:
                    json.dump(updated_dict, output_file, ensure_ascii=False, indent=4)

def loot_updata(loot_dict:dict): #输入json文件的dict格式，输出修改后的dict格式。
    for i in loot_dict.get("pools",[]):#打开随机池pools列表
        for j in i.get("entries",[]):#打开entries列表
            Item_id = j.get("name","written_book")
            if j.get("type","") == "loot_table" or j.get("type","") == "minecraft:loot_table":#战利品表引用更新
                j["value"]=j.pop("name","")
            for k in j.get("functions",[]):#打开functions列表
                if k.get('function','') == 'set_nbt' or k.get('function','') == 'minecraft:set_nbt':#是否是set_nbt函数，是的话，更新并替换成
                    k['function'] = 'set_components'
                    k['components'] =(nbt_to_components.transfer(Item_id,k.pop('tag'),3))

                if k.get('function','') == 'copy_nbt' or k.get('function','') == 'minecraft:copy_nbt':#是否是copy_nbt函数，是的话，更新并替换成
                    k['function'] = 'copy_custom_data'
                    #组件名称暂未处理

                if k.get('function','') == 'set_attributes' or k.get('function','') == 'minecraft:set_attributes':
                    operation_dict={"addition":"add_value","multiply_base":"add_multiplied_base,","multiply_total":"add_multiplied_total"}
                    for l in k.get('modifiers',[]):
                        l["operation"]=operation_dict[l.get('operation','')]
    return loot_dict