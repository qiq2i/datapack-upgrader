from nbtlib import parse_nbt, Path #NBT分析库 https://github.com/vberlier/nbtlib

s = '{Damage:34,Unbreakable:1b,Enchantments:[{id:"minecraft:aqua_affinity",lvl:2s},{id:"minecraft:bane_of_arthropods",lvl:3s}]}'
data = parse_nbt(s)
#print(data)
#print(data.get('Damage'))#获取 <class 'nbtlib.tag.Int'>，要取值则调用value()
#print(data.pop('Damage'))#获取并移除
#print(data)
#print(data.get('Damage'))#不存在则返回None


def item_nbt_updata(nbtlib): #处理分析过的NBT(nbtlib)，更新后每个指令存在
    components_list = []
    
    #Damage
    if 'Damage' in nbtlib:
        components_list = Damage_updata(components_list,nbtlib.get('Damage'))
        del nbtlib['Damage']

    #RepairCost
    if 'RepairCost' in nbtlib:
        components_list = RepairCost_updata(components_list,nbtlib.get('RepairCost'))
        del nbtlib['RepairCost']
    
    #Unbreakable
    if 'Unbreakable' in nbtlib:
        components_list = Unbreakable_updata(components_list,nbtlib.get('Unbreakable'),nbtlib.get('HideFlags',0))
        del nbtlib['Unbreakable']
    
    #Enchantments
    if 'Enchantments' in nbtlib:
        components_list = Enchantments_updata(components_list,nbtlib.get('Enchantments'),nbtlib.get('HideFlags',0))
        del nbtlib['Enchantments']

    #StoredEnchantments
    if 'StoredEnchantments' in nbtlib:
        components_list = StoredEnchantments_updata(components_list,nbtlib.get('StoredEnchantments'),nbtlib.get('HideFlags',0))
        del nbtlib['StoredEnchantments']

    #display_Name
    if 'Name' in nbtlib.get('display',{}):
        components_list = display_Name_updata(components_list,nbtlib['display']['Name'])
        del nbtlib['display']['Name']

    #display_Lore
    if 'Lore' in nbtlib.get('display',{}):
        components_list = display_Lore_updata(components_list,nbtlib['display']['Lore'])
        del nbtlib['display']['Lore']

    #CanDestroy
    if 'CanDestroy' in nbtlib:
        components_list = CanDestroy_updata(components_list,nbtlib['CanDestroy'],nbtlib.get('HideFlags',0))
        del nbtlib['CanDestroy']

    #CanPlaceOn
    if 'CanPlaceOn' in nbtlib:
        components_list = CanPlaceOn_updata(components_list,nbtlib['CanPlaceOn'],nbtlib.get('HideFlags',0))
        del nbtlib['CanPlaceOn']

    #display_color
    if 'color' in nbtlib.get('display',{}):
        components_list = display_color_updata(components_list,nbtlib['display']['color'],nbtlib.get('HideFlags',0))
        del nbtlib['display']['color']

    #AttributeModifiers
    if 'AttributeModifiers' in nbtlib:
        components_list = AttributeModifiers_updata(components_list,nbtlib['AttributeModifiers'],nbtlib.get('HideFlags',0))
        del nbtlib['AttributeModifiers']

    #ChargedProjectiles
    if 'Charged' in nbtlib:
        components_list = ChargedProjectiles_updata(components_list,nbtlib.get('ChargedProjectiles',[]))
        del nbtlib['Charged']
        del nbtlib['ChargedProjectiles']

    #Items
    if 'Items' in nbtlib:
        components_list = Items_updata(components_list,nbtlib['Items'])
        del nbtlib['Items']

    #display_MapColor
    if 'MapColor' in nbtlib.get('display',{}):
        components_list = display_MapColor_updata(components_list,nbtlib['display']['MapColor'])
        del nbtlib['display']['MapColor']

    #Decorations
    if 'Decorations' in nbtlib:
        components_list = Decorations_updata(components_list,nbtlib['Decorations'])
        del nbtlib['Decorations']
    
    #map
    if 'map' in nbtlib:
        components_list = map_updata(components_list,nbtlib['map'])
        del nbtlib['map']
    
    #CustomModelData
    if 'CustomModelData' in nbtlib:
        components_list = CustomModelData_updata(components_list,nbtlib['CustomModelData'])
        del nbtlib['CustomModelData']
    return components_list

def Damage_updata(components_list: list,value:int):
    if value != None:
        components_list.append("damage=" + str(value + 0))
    return components_list
def RepairCost_updata(components_list: list,value:int):
    if value != None:
        components_list.append("repair_cost=" + str(value + 0))
    return components_list
def Unbreakable_updata(components_list: list,value,HideFlags:int):
    if value != None:
        if HideFlags == None:
            HideFlags=0
        try:
            HideFlags += 0
        except Exception:
            HideFlags=0
            value += 0
        if value == 1:
            bit = (HideFlags >> 2) & 1 #获取第3个二进制位，为1则隐藏
            if bit == 1:
                components_list.append("unbreakable={show_in_tooltip:false}")
            else:
                components_list.append("unbreakable={}")
    return components_list
def Enchantments_updata(components_list: list,value:list,HideFlags:int):
    if value != None:
        levels_str= "{"
        for i in value:
            levels_str =levels_str+"'"+i['id']+"':"+str(i['lvl']+0)+","
        levels_str = levels_str.rstrip(",") + "}"
        if HideFlags == None:
            HideFlags=0
        try:
            HideFlags += 0
        except Exception:
            HideFlags=0
        bit = HideFlags & 1 #获取第1个二进制位，为1则隐藏
        if bit == 1:
            components_list.append("enchantments={levels:"+levels_str+",show_in_tooltip:false}")
        else:
            components_list.append("enchantments={levels:"+levels_str+"}")
    return components_list
def StoredEnchantments_updata(components_list: list,value:list,HideFlags:int):
    if value != None:
        levels_str= "{"
        for i in value:
            levels_str =levels_str+"'"+i['id']+"':"+str(i['lvl']+0)+","
        levels_str = levels_str.rstrip(",") + "}"
        if HideFlags == None:
            HideFlags=0
        try:
            HideFlags += 0
        except Exception:
            HideFlags=0
        bit = HideFlags & (1 << 6) #获取第6个二进制位，为1则隐藏
        if bit == 1:
            components_list.append("stored_enchantments={levels:"+levels_str+",show_in_tooltip:false}")
        else:
            components_list.append("stored_enchantments={levels:"+levels_str+"}")
    return components_list
def display_Name_updata(components_list: list,value: str):
    try:
        components_list.append("custom_name='"+value+"'")
    except Exception:
        pass
    return components_list
def display_Lore_updata(components_list: list,value: list):
    #print("','".join(value)) #value为列表
    try:
        components_list.append("lore=['"+"','".join(value)+"']")
    except Exception:
        pass
    return components_list
def CanDestroy_updata(components_list: list,value: list,HideFlags: int):
    print(value)
    try:
        if HideFlags == None:
            HideFlags=0
        try:
            HideFlags += 0
        except Exception:
            HideFlags=0
        bit = (HideFlags >> 3) & 1 #获取第4个二进制位，为1则隐藏
        if bit == 1:
            components_list.append('can_break={predicates:{blocks:[\''+"','".join(value)+"\']},show_in_tooltip:false}")
        else:
            components_list.append('can_break={predicates:{blocks:[\''+"','".join(value)+"\']}")
    except Exception:
        pass
    return components_list
def CanPlaceOn_updata(components_list: list,value: list,HideFlags: int):
    try:
        if HideFlags == None:
            HideFlags=0
        try:
            HideFlags += 0
        except Exception:
            HideFlags=0
        bit = (HideFlags >> 4) & 1 #获取第4个二进制位，为1则隐藏
        if bit == 1:
            components_list.append('can_place_on={predicates:{blocks:[\''+"','".join(value)+"\']},show_in_tooltip:false}")
        else:
            components_list.append('can_place_on={predicates:{blocks:[\''+"','".join(value)+"\']}")
    except Exception:
        pass
    return components_list
def display_color_updata(components_list: list,value: int,HideFlags: int):
    try:
        if HideFlags == None:
            HideFlags=0
        try:
            HideFlags += 0
        except Exception:
            HideFlags=0
        bit = (HideFlags >> 6) & 1 #获取第7个二进制位，为1则隐藏
        if bit == 1:
            components_list.append("dyed_color={rgb:"+str(value+0)+",show_in_tooltip:false}")
        else:
            components_list.append("dyed_color={rgb:"+str(value+0)+"}")
    except Exception:
        pass
    return components_list
def AttributeModifiers_updata(components_list: list,value: list,HideFlags: int):
    #value [{},{}]
    try:
        components_str = "attribute_modifiers={modifiers:["
        for i in value:#{}
            #print(i.get("UUID"))
            components_str +="{"
            if "AttributeName" in i:
                components_str +="type:'"+i.get("AttributeName")+"',"
            if "Slot" in i:
                components_str +="slot:'"+i.get("Slot")+"',"
            if "UUID" in i:#列表[]
                #print(",".join([str(element+0) for element in i.get("UUID")]))
                components_str +="uuid:[I;"+",".join([str(element+0) for element in i.get("UUID")])+"],"
            if "Name" in i:
                components_str +="name:'"+i.get("Name")+"',"
                #print(i.get("Name"))
            if "Amount" in i:
                components_str +="amount:'"+str(i.get("Amount",0)+0)+"',"
                #print(i.get("Amount"))
            if "Operation" in i:
                if i.get("Operation",0) == 0:
                    components_str +="operation:'add_value',"
                elif i.get("Operation",0) == 1:
                    components_str +="operation:'add_multiplied_base',"
                elif i.get("Operation",0) == 2:
                    components_str +="operation:'add_multiplied_total',"
                else:
                    pass
                #print(i.get("Operation"))
                
            components_str=components_str.rstrip(",")+"},"
        components_str=components_str.rstrip(",")+"]"
        if HideFlags == None:
            HideFlags=0
        try:
            HideFlags += 0
        except Exception:
            HideFlags=0
        bit = (HideFlags >> 1) & 1 #获取第2个二进制位，为1则隐藏
        if bit == 1:
            components_str+="],show_in_tooltip:false}"
        else:
            components_str+="]}"
        components_list.append(components_str)
    except Exception:
        return components_list
    return components_list
def ChargedProjectiles_updata(components_list: list,value: list):#value为列表。
    try:
        #print(value)
        charged_projectiles_str="charged_projectiles=["
        for i in value:
            charged_projectiles_str+="{id:'"+i.get("id")+"'},"
        charged_projectiles_str=charged_projectiles_str.rstrip(",")+"]"
        components_list.append(charged_projectiles_str)
    except Exception:
        pass
    return components_list
def Items_updata(components_list: list,value: list):#收纳袋value:[] components待处理
    try:
        bundle_contents_str="bundle_contents=["
        for i in value:
            bundle_contents_str+="{id:'"+i.get("id")+"',count:"+str(i.get("Count")+0)+",components:[]"+"},"
        bundle_contents_str=bundle_contents_str.rstrip(",")+"]"
        components_list.append(bundle_contents_str)
    except Exception:
        pass
    return components_list
def display_MapColor_updata(components_list: list,value: int):
    try:
        components_list.append("map_color="+str(value+0))
    except Exception:
        pass
    return components_list

def Decorations_updata(components_list: list,value: list):
    try:
        map_decorations_str = "map_decorations:{"
        for i in value:
            id = i.get("id")#String
            type_B = i.get("type")#Byte
            x = i.get("x")#Double
            z = i.get("z")#Double
            rot = i.get("rot")#Double
            if type_B == 0:
                type = "player"
            elif type_B == 1:
                type = "frame"
            elif type_B == 2:
                type = "red_marker"
            elif type_B == 3:
                type = "blue_marker"
            elif type_B == 4:
                type = "target_x"
            elif type_B == 5:
                type = "target_point"
            elif type_B == 6:
                type = "player_off_map"
            elif type_B == 7:
                type = "player_off_limits"
            elif type_B == 8:
                type = "mansion"
            elif type_B == 9:
                type = "monument"
            elif type_B == 10:
                type = "banner_white"
            elif type_B == 11:
                type = "banner_orange"
            elif type_B == 12:
                type = "banner_magenta"
            elif type_B == 13:
                type = "banner_light_blue"
            elif type_B == 14:
                type = "banner_yellow"
            elif type_B == 15:
                type = "banner_lime"
            elif type_B == 16:
                type = "banner_pink"
            elif type_B == 17:
                type = "banner_gray"
            elif type_B == 18:
                type = "banner_light_gray"
            elif type_B == 19:
                type = "banner_cyan"
            elif type_B == 20:
                type = "banner_purple"
            elif type_B == 21:
                type = "banner_blue"
            elif type_B == 22:
                type = "banner_brown"
            elif type_B == 23:
                type = "banner_green"
            elif type_B == 24:
                type = "banner_red"
            elif type_B == 25:
                type = "banner_black"
            elif type_B == 26:
                type = "red_x"
            elif type_B == 27:
                type = "village_desert"
            elif type_B == 28:
                type = "village_plains"
            elif type_B == 29:
                type = "village_savanna"
            elif type_B == 30:
                type = "village_snowy"
            elif type_B == 31:
                type = "village_taiga"
            elif type_B == 32:
                type = "jungle_temple"
            elif type_B == 33:
                type = "swamp_hut"
            else:
                type = "player"
            map_decorations_str += "'"+id+"':{type:'"+type+"',x:"+str(x+0)+",z:"+str(z+0)+",rotation:"+str(rot+0)+"f},"
        map_decorations_str=map_decorations_str.rstrip(",")+"}"
        components_list.append(map_decorations_str)
    except Exception:
        pass
    return components_list

def map_updata(components_list: list,value: int):
    try:
        components_list.append("map_id="+str(value+0))
    except Exception:
        pass
    return components_list

def CustomModelData_updata(components_list: list,value: int):
    try:
        components_list.append("custom_model_data="+str(value+0))
    except Exception:
        pass
    return components_list
'''
s = '{Damage:34,Unbreakable:False,Enchantments:[{id:"minecraft:aqua_affinity",lvl:2s},{id:"minecraft:bane_of_arthropods",lvl:3s}],display:{Name:\'{\"text\":\"§e治疗不死图腾\"}\',Lore:[\'{\"text\":\"§7死亡不掉落一次，带在身上即可。\"}\',\'{\"text\":\"§7（注意，如果游戏设置未开启 死亡掉落物品保护，则该物品无效）\"}\']}}'
print(parse_nbt(s))  # 输出：{'Enchantments': '[{id:"minecraft:aqua_affinity",lvl:2s},{id:"minecraft:bane_of_arthropods",lvl:3s}]'}
print(item_nbt_updata(parse_nbt(s))) # 输出：['damage=34']
print("===")
s = '{Unbreakable:1b,AttributeModifiers:[{AttributeName:"generic.max_health",Name:"generic.max_health",Amount:1,Operation:0,UUID:[I;487516678,559893762,-1722137402,-1908663762]}]}'
print(item_nbt_updata(parse_nbt(s)))
print("===")
s = '{ChargedProjectiles:[{id:"minecraft:arrow",Count:1b},{id:"minecraft:arrow",Count:1b},{id:"minecraft:arrow",Count:1b}],Charged:1b}'
print(item_nbt_updata(parse_nbt(s)))
'''
s = '{Decorations:[{x:2.0d,z:3.0d,type:2b,rot:180.0d,id:"123"}]}'
print(parse_nbt(s))
print(item_nbt_updata(parse_nbt(s)))