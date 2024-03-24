import nbtlib
from nbtlib import serialize_tag#可以使用nbtlib将Nbt标记序列化为它们的文字表示形式。
from nbtlib.tag import String, List, Compound, IntArray
from nbtlib import parse_nbt, Path #NBT分析库 https://github.com/vberlier/nbtlib

s = '{Damage:34,Unbreakable:1b,Enchantments:[{id:"minecraft:aqua_affinity",lvl:2s},{id:"minecraft:bane_of_arthropods",lvl:3s}]}'
data = parse_nbt(s)
#print(data)
#print(data.get('Damage'))#获取 <class 'nbtlib.tag.Int'>，要取值则调用value()
#print(data.pop('Damage'))#获取并移除
#print(data)
#print(data.get('Damage'))#不存在则返回None


def item_nbt_updata(id: String,nbtlib_compound: nbtlib.tag.Compound): #处理分析过的NBT(nbtlib_compound)，更新后每个指令存在
    components_list = []
    #Damage
    if 'Damage' in nbtlib_compound:
        components_list = Damage_updata(components_list,nbtlib_compound.get('Damage'))
        del nbtlib_compound['Damage']

    #RepairCost
    if 'RepairCost' in nbtlib_compound:
        components_list = RepairCost_updata(components_list,nbtlib_compound.get('RepairCost'))
        del nbtlib_compound['RepairCost']
    
    #Unbreakable
    if 'Unbreakable' in nbtlib_compound:
        components_list = Unbreakable_updata(components_list,nbtlib_compound.get('Unbreakable'),nbtlib_compound.get('HideFlags',0))
        del nbtlib_compound['Unbreakable']
    
    #Enchantments
    if 'Enchantments' in nbtlib_compound:
        components_list = Enchantments_updata(components_list,nbtlib_compound.get('Enchantments'),nbtlib_compound.get('HideFlags',0))
        del nbtlib_compound['Enchantments']

    #StoredEnchantments
    if 'StoredEnchantments' in nbtlib_compound:
        components_list = StoredEnchantments_updata(components_list,nbtlib_compound.get('StoredEnchantments'),nbtlib_compound.get('HideFlags',0))
        del nbtlib_compound['StoredEnchantments']

    #display_Name
    if 'Name' in nbtlib_compound.get('display',{}):
        components_list = display_Name_updata(components_list,nbtlib_compound['display']['Name'])
        del nbtlib_compound['display']['Name']

    #display_Lore
    if 'Lore' in nbtlib_compound.get('display',{}):
        components_list = display_Lore_updata(components_list,nbtlib_compound['display']['Lore'])
        del nbtlib_compound['display']['Lore']

    #CanDestroy
    if 'CanDestroy' in nbtlib_compound:
        components_list = CanDestroy_updata(components_list,nbtlib_compound['CanDestroy'],nbtlib_compound.get('HideFlags',0))
        del nbtlib_compound['CanDestroy']

    #CanPlaceOn
    if 'CanPlaceOn' in nbtlib_compound:
        components_list = CanPlaceOn_updata(components_list,nbtlib_compound['CanPlaceOn'],nbtlib_compound.get('HideFlags',0))
        del nbtlib_compound['CanPlaceOn']

    #display_color
    if 'color' in nbtlib_compound.get('display',{}):
        components_list = display_color_updata(components_list,nbtlib_compound['display']['color'],nbtlib_compound.get('HideFlags',0))
        del nbtlib_compound['display']['color']

    #AttributeModifiers
    if 'AttributeModifiers' in nbtlib_compound:
        components_list = AttributeModifiers_updata(components_list,nbtlib_compound['AttributeModifiers'],nbtlib_compound.get('HideFlags',0))
        del nbtlib_compound['AttributeModifiers']

    #ChargedProjectiles
    if 'Charged' in nbtlib_compound:
        components_list = ChargedProjectiles_updata(components_list,nbtlib_compound.get('ChargedProjectiles',[]))
        del nbtlib_compound['Charged']
        del nbtlib_compound['ChargedProjectiles']

    #Items
    if 'Items' in nbtlib_compound:
        components_list = Items_updata(components_list,nbtlib_compound['Items'])
        del nbtlib_compound['Items']

    #display_MapColor
    if 'MapColor' in nbtlib_compound.get('display',{}):
        components_list = display_MapColor_updata(components_list,nbtlib_compound['display']['MapColor'])
        del nbtlib_compound['display']['MapColor']

    #Decorations
    if 'Decorations' in nbtlib_compound:
        components_list = Decorations_updata(components_list,nbtlib_compound['Decorations'])
        del nbtlib_compound['Decorations']
    
    #map
    if 'map' in nbtlib_compound:
        components_list = map_updata(components_list,nbtlib_compound['map'])
        del nbtlib_compound['map']
    
    #CustomModelData
    if 'CustomModelData' in nbtlib_compound:
        components_list = CustomModelData_updata(components_list,nbtlib_compound['CustomModelData'])
        del nbtlib_compound['CustomModelData']
    
    #Potion
    if 'Potion' in nbtlib_compound:
        components_list = Potion_updata(components_list,nbtlib_compound['Potion'],nbtlib_compound.get("CustomPotionColor",None),nbtlib_compound.get("custom_potion_effects",None))
        del nbtlib_compound['Potion']
        if 'CustomPotionColor' in nbtlib_compound:
            del nbtlib_compound['CustomPotionColor']
        if 'custom_potion_effects' in nbtlib_compound:
            del nbtlib_compound['custom_potion_effects']

    #pages
    if 'pages' in nbtlib_compound:
        components_list = pages_updata(components_list,id,nbtlib_compound['pages'],nbtlib_compound.pop("filtered_pages",nbtlib.Compound({})),nbtlib_compound.pop("title",None),nbtlib_compound.pop("author",None),nbtlib_compound.pop("generation",None),nbtlib_compound.pop("resolved",None))
        del nbtlib_compound['pages']
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

def Potion_updata(components_list: list,Potion: String,CustomPotionColor: int,custom_potion_effects: list):
    try:
        potion_contents_str = "potion_contents={potion:'"+Potion+"',"
        try:
            potion_contents_str +="custom_color:"+str(CustomPotionColor+0)+","
        except Exception:
            pass
        try:
            potion_contents_str +="custom_effects:"+serialize_tag(custom_potion_effects)+","
        except Exception:
            pass
        potion_contents_str=potion_contents_str.rstrip(",")+"}"
        components_list.append(potion_contents_str)
    except Exception:
        pass
    return components_list

def pages_updata(components_list: list,id:String,pages:list,filtered_pages,title:String,author:String,generation:int,resolved:bool):#过滤页面暂未处理
    try:
        print(pages)
        if id == 'writable_book' or id == 'written_book':
            if type(pages) is nbtlib.tag.List[String]:
                pages_str=id+"_content={pages:"+serialize_tag(pages)+","
            if type(pages) is nbtlib.tag.List[Compound]:
                pages_str=components_list.append(id+"_content={pages:"+serialize_tag(pages))+","
        if id == 'written_book':
            if title != None:
                pages_str+="title:'"+serialize_tag(title)+"',"
            if author != None:
                pages_str+="author:'"+serialize_tag(author)+"',"
            if generation != None:
                pages_str+="generation:'"+serialize_tag(generation)+"',"
            if resolved != None:
                pages_str+="resolved:'"+serialize_tag(resolved)+"',"
        pages_str=pages_str.rstrip(",")+"}"
        components_list.append(pages_str)
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
#s = '{Decorations:[{x:2.0d,z:3.0d,type:2b,rot:180.0d,id:"123"}]}'
s = '{pages:["123\n123","213"]}'
d = '{title:"233",author:"666",generation:0,resolved:1b,pages:[\'{"text":"123"}\',\'{"text":"456","hoverEvent":{"action":"show_text","value":[{"text":"","color":"blue"}]}}\']}'
#print(parse_nbt(s))
print(item_nbt_updata("writable_book",parse_nbt(s)))
#print(parse_nbt(d))
print(item_nbt_updata("written_book",parse_nbt(d)))