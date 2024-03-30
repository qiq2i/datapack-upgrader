import nbtlib
from nbtlib import serialize_tag#可以使用nbtlib将Nbt标记序列化为它们的文字表示形式。
from nbtlib.tag import String, List, Compound, IntArray
from nbtlib import parse_nbt, Path #NBT分析库 https://github.com/vberlier/nbtlib

def item_nbt_updata_to_dict(id: String,nbtlib_compound: nbtlib.tag.Compound): #处理分析过的NBT(nbtlib_compound)，更新后每个指令存在
    #输入 物品ID(String) 和 被nbtlib解析后的nbt(nbtlib_compound)，输出 被更新成组件后的形式，格式为字典(dict)
    components_dict = {}

    #Damage
    if 'Damage' in nbtlib_compound:
        components_dict = Damage_updata(components_dict,nbtlib_compound.pop('Damage',None))

    #RepairCost
    if 'RepairCost' in nbtlib_compound:
        components_dict = RepairCost_updata(components_dict,nbtlib_compound.pop('RepairCost'))
    
    #Unbreakable
    if 'Unbreakable' in nbtlib_compound:
        components_dict = Unbreakable_updata(components_dict,nbtlib_compound.pop('Unbreakable',0),nbtlib_compound.get('HideFlags',0))
    
    #Enchantments
    if 'Enchantments' in nbtlib_compound:
        components_dict = Enchantments_updata(components_dict,nbtlib_compound.pop('Enchantments',None),nbtlib_compound.get('HideFlags',0))

    #StoredEnchantments
    if 'StoredEnchantments' in nbtlib_compound:
        components_dict = StoredEnchantments_updata(components_dict,nbtlib_compound.pop('StoredEnchantments',None),nbtlib_compound.get('HideFlags',0))

    #display_Name
    if 'Name' in nbtlib_compound.get('display',{}):
        components_dict = display_Name_updata(components_dict,nbtlib_compound.get('display').pop('Name'))

    #display_Lore
    if 'Lore' in nbtlib_compound.get('display',{}):
        components_dict = display_Lore_updata(components_dict,nbtlib_compound.get('display').pop('Lore'))

    #CanDestroy
    if 'CanDestroy' in nbtlib_compound:
        components_dict = CanDestroy_updata(components_dict,nbtlib_compound.pop('CanDestroy',None),nbtlib_compound.get('HideFlags',0))

    #CanPlaceOn
    if 'CanPlaceOn' in nbtlib_compound:
        components_dict = CanPlaceOn_updata(components_dict,nbtlib_compound.pop('CanPlaceOn',None),nbtlib_compound.get('HideFlags',0))

    #display_color
    if 'color' in nbtlib_compound.get('display',{}):
        components_dict = display_color_updata(components_dict,nbtlib_compound.get('display').pop('color',None),nbtlib_compound.get('HideFlags',0))

    #AttributeModifiers
    if 'AttributeModifiers' in nbtlib_compound:
        components_dict = AttributeModifiers_updata(components_dict,nbtlib_compound.pop('AttributeModifiers',None),nbtlib_compound.get('HideFlags',0))

    #ChargedProjectiles
    if 'Charged' in nbtlib_compound:
        components_dict = ChargedProjectiles_updata(components_dict,nbtlib_compound.pop('ChargedProjectiles',None))
        del nbtlib_compound['Charged']

    #Items
    if 'Items' in nbtlib_compound:
        components_dict = Items_updata(components_dict,id,nbtlib_compound.pop('Items',None))

    #display_MapColor
    if 'MapColor' in nbtlib_compound.get('display',{}):
        components_dict = display_MapColor_updata(components_dict,nbtlib_compound.get('display').pop('MapColor',None))

    #Decorations
    if 'Decorations' in nbtlib_compound:
        components_dict = Decorations_updata(components_dict,nbtlib_compound.pop('Decorations',None))
    
    #map
    if 'map' in nbtlib_compound:
        components_dict = map_updata(components_dict,nbtlib_compound.pop('map'))
    
    #CustomModelData
    if 'CustomModelData' in nbtlib_compound:
        components_dict = CustomModelData_updata(components_dict,nbtlib_compound.pop('CustomModelData'))

    #Potion
    if 'Potion' in nbtlib_compound:
        components_dict = Potion_updata(components_dict,nbtlib_compound.pop('Potion',None),nbtlib_compound.pop("CustomPotionColor",None),nbtlib_compound.pop("custom_potion_effects",None))

    #pages
    if 'pages' in nbtlib_compound:
        components_dict = pages_updata(components_dict,id,nbtlib_compound.pop('pages',None),nbtlib_compound.pop("filtered_pages",nbtlib.Compound({})),nbtlib_compound.pop("title",None),nbtlib_compound.pop("author",None),nbtlib_compound.pop("generation",None),nbtlib_compound.pop("resolved",None))
    
    #Trim
    if 'Trim' in nbtlib_compound:
        components_dict = Trim_updata(components_dict,nbtlib_compound.pop('Trim',None),nbtlib_compound.get('HideFlags',0))

    #effects
    if 'effects' in nbtlib_compound:
        components_dict = effects_updata(components_dict,nbtlib_compound.pop('effects',None))

    #HideFlags
    if 'HideFlags' in nbtlib_compound:
        components_dict = HideFlags_updata(components_dict,nbtlib_compound.pop('HideFlags',0))

    #DebugProperty
    if 'DebugProperty' in nbtlib_compound:
        components_dict = DebugProperty_updata(components_dict,nbtlib_compound.pop('DebugProperty',None))

    #EntityTag
    if 'EntityTag' in nbtlib_compound:
        components_dict = EntityTag_updata(components_dict,nbtlib_compound.pop('EntityTag',None))

    #bucket_entity_data
    components_dict = bucket_entity_data_updata(components_dict,nbtlib_compound.pop("NoAI",None),nbtlib_compound.pop("Silent",None),nbtlib_compound.pop("NoGravity",None),nbtlib_compound.pop("Glowing",None),nbtlib_compound.pop("Invulnerable",None),nbtlib_compound.pop("Health",None),nbtlib_compound.pop("Age",None),nbtlib_compound.pop("Variant",None),nbtlib_compound.pop("HuntingCooldown",None),nbtlib_compound.pop("BucketVariantTag",None))

    #instrument
    if 'instrument' in nbtlib_compound:
        components_dict = instrument_updata(components_dict,nbtlib_compound.pop('instrument',None))

    #Recipes
    if 'Recipes' in nbtlib_compound:
        components_dict = Recipes_updata(components_dict,nbtlib_compound.pop('Recipes',None))
    
    #Lodestone
    if 'LodestonePos' in nbtlib_compound:
        components_dict = Lodestone_updata(components_dict,nbtlib_compound.pop("LodestoneDimension",None),nbtlib_compound.pop("LodestonePos",None),nbtlib_compound.pop("LodestoneTracked",None))
    
    #Explosion
    if 'Explosion' in nbtlib_compound:
        components_dict = Explosion_updata(components_dict,nbtlib_compound.pop("Explosion",None))

    #Fireworks
    if 'Fireworks' in nbtlib_compound:
        components_dict = Fireworks_updata(components_dict,nbtlib_compound["Fireworks"].pop("Explosions",None),nbtlib_compound["Fireworks"].pop("Flight",None))
        del nbtlib_compound["Fireworks"]

    #SkullOwner
    if 'SkullOwner' in nbtlib_compound:
        components_dict = SkullOwner_updata(components_dict,nbtlib_compound.pop("SkullOwner"))

    #BlockEntityTag
    if 'BlockEntityTag' in nbtlib_compound:
        components_dict = BlockEntityTag_updata(components_dict,id,nbtlib_compound.pop("BlockEntityTag"))

    #BlockStateTag
    if 'BlockStateTag' in nbtlib_compound:
        components_dict = BlockStateTag_updata(components_dict,nbtlib_compound.pop("BlockStateTag"))

    #清理门户
    if 'display' in nbtlib_compound:
        del nbtlib_compound["display"]
    #剩余NBT置入custom_data中
    if serialize_tag(nbtlib_compound) != "{}":
        components_dict["custom_data"]=serialize_tag(nbtlib_compound)

    return components_dict

def Damage_updata(components_dict: dict,value:nbtlib.tag.Int):#输入字典components_dict(dict)和Damage的值(int)。更新Damage后，添加进字典components_dict后输出该字典。
    if value != None:
        components_dict["damage"] = serialize_tag(value)
    return components_dict
def RepairCost_updata(components_dict: dict,value:nbtlib.tag.Int):#输入字典components_dict(dict)和RepairCost的值(int)。更新RepairCost后，添加进字典components_dict后输出该字典。
    if value != None:
        components_dict["repair_cost"] = serialize_tag(value)
    return components_dict
def Unbreakable_updata(components_dict: dict,value:nbtlib.tag.Byte,HideFlags:nbtlib.tag.Int):#输入字典components_dict(dict)和Unbreakable的值(byte)和HideFlags(int)。更新Unbreakable后，添加进字典components_dict后输出该字典。
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
                components_dict["unbreakable"]="{show_in_tooltip:false}"
            else:
                components_dict["unbreakable"]="{}"
    return components_dict
def Enchantments_updata(components_dict: dict,value:nbtlib.tag.List,HideFlags:nbtlib.tag.Int):#输入字典components_dict(dict)和Enchantments的值(list)和HideFlags(int)。更新Enchantments后，添加进字典components_dict后输出该字典。
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
            components_dict["enchantments"]="{levels:"+levels_str+",show_in_tooltip:false}"
        else:
            components_dict["enchantments"]="{levels:"+levels_str+"}"
    return components_dict
def StoredEnchantments_updata(components_dict: dict,value:nbtlib.tag.List,HideFlags:nbtlib.tag.Int):#输入字典components_dict(dict)和StoredEnchantments的值(list)和HideFlags(int)。更新StoredEnchantments后，添加进字典components_dict后输出该字典。
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
            components_dict["stored_enchantments"]="{levels:"+levels_str+",show_in_tooltip:false}"
        else:
            components_dict["stored_enchantments"]="{levels:"+levels_str+"}"
    return components_dict
def display_Name_updata(components_dict: dict,value: nbtlib.tag.String):#更新display.Name后，添加进字典components_dict后输出该字典。
    try:
        components_dict["custom_name"] = serialize_tag(value)
    except Exception:
        pass
    return components_dict
def display_Lore_updata(components_dict: dict,value: nbtlib.tag.List):#更新display.Lore后，添加进字典components_dict后输出该字典。
    try:
        components_dict["lore"]=serialize_tag(value)
    except Exception:
        pass
    return components_dict
def CanDestroy_updata(components_dict: dict,value: nbtlib.tag.List,HideFlags: nbtlib.tag.Int):#更新CanDestroy后，添加进字典components_dict后输出该字典。
    try:
        if HideFlags == None:
            HideFlags=0
        try:
            HideFlags += 0
        except Exception:
            HideFlags=0
        bit = (HideFlags >> 3) & 1 #获取第4个二进制位，为1则隐藏
        if bit == 1:
            components_dict['can_break']="{blocks:"+serialize_tag(value)+",show_in_tooltip:false}"
        else:
            components_dict['can_break']="{blocks:"+serialize_tag(value)+"}"
    except Exception:
        pass
    return components_dict
def CanPlaceOn_updata(components_dict: dict,value: nbtlib.tag.List,HideFlags: nbtlib.tag.Int):#更新CanPlaceOn后，添加进字典components_dict后输出该字典。
    try:
        if HideFlags == None:
            HideFlags=0
        try:
            HideFlags += 0
        except Exception:
            HideFlags=0
        bit = (HideFlags >> 4) & 1 #获取第4个二进制位，为1则隐藏
        if bit == 1:
            components_dict['can_place_on']='{blocks:'+serialize_tag(value)+",show_in_tooltip:false}"
        else:
            components_dict['can_place_on']='{blocks:'+serialize_tag(value)+"}"
    except Exception:
        pass
    return components_dict
def display_color_updata(components_dict: dict,value: nbtlib.tag.Int,HideFlags: nbtlib.tag.Int):#更新display.color后，添加进字典components_dict后输出该字典。
    try:
        if HideFlags == None:
            HideFlags=0
        try:
            HideFlags += 0
        except Exception:
            HideFlags=0
        bit = (HideFlags >> 6) & 1 #获取第7个二进制位，为1则隐藏
        if bit == 1:
            components_dict["dyed_color"]="{rgb:"+serialize_tag(value)+",show_in_tooltip:false}"
        else:
            components_dict["dyed_color"]="{rgb:"+serialize_tag(value)+"}"
    except Exception:
        pass
    return components_dict
def AttributeModifiers_updata(components_dict: dict,value: nbtlib.tag.List,HideFlags: nbtlib.tag.Int):#更新AttributeModifiers后，添加进字典components_dict后输出该字典。
    #value [{},{}]
    try:
        components_str = "{modifiers:["
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
                components_str +="amount:"+str(i.get("Amount",0)+0)+","
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
        components_str=components_str.rstrip(",")
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
        components_dict["attribute_modifiers"] = components_str
    except Exception:
        return components_dict
    return components_dict
def ChargedProjectiles_updata(components_dict: dict,value: nbtlib.tag.List):#更新ChargedProjectiles后，添加进字典components_dict后输出该字典。
    try:
        charged_projectiles_str="["
        for i in value:
            if i.get("id")!=None:
                charged_projectiles_str+=Item_Common_tags_updata(i)
                charged_projectiles_str+=","
        charged_projectiles_str=charged_projectiles_str.rstrip(",")+"]"
        components_dict["charged_projectiles"]=charged_projectiles_str
    except Exception:
        pass
    return components_dict
def Items_updata(components_dict: dict,id:String,value: nbtlib.tag.List):#更新Items后，添加进字典components_dict后输出该字典。
    try:
        #if id == "bundle" or id == "minecraft:bundle":#收纳袋
        bundle_contents_str="["
        for i in value:
            bundle_contents_str+=Item_Common_tags_updata(i)+","
        bundle_contents_str=bundle_contents_str.rstrip(",")+"]"
        components_dict["bundle_contents"]=bundle_contents_str
    except Exception:
        pass
    return components_dict
def display_MapColor_updata(components_dict: dict,value: nbtlib.tag.Int):#更新display.MapColor后，添加进字典components_dict后输出该字典。
    try:
        components_dict["map_color="]+serialize_tag(value)
    except Exception:
        pass
    return components_dict

def Decorations_updata(components_dict: dict,value: nbtlib.tag.List):#更新Decorations后，添加进字典components_dict后输出该字典。
    try:
        map_decorations_str = "{"
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
        components_dict["map_decorations"] = map_decorations_str
    except Exception:
        pass
    return components_dict

def map_updata(components_dict: dict,value: nbtlib.tag.Int):#更新map后，添加进字典components_dict后输出该字典。
    try:
        components_dict["map_id"]=serialize_tag(value)
    except Exception:
        pass
    return components_dict

def CustomModelData_updata(components_dict: dict,value: nbtlib.tag.Int):#更新CustomModelData后，添加进字典components_dict后输出该字典。
    try:
        components_dict["custom_model_data"]=serialize_tag(value)
    except Exception:
        pass
    return components_dict

def Potion_updata(components_dict: dict,Potion: String,CustomPotionColor: nbtlib.tag.Int,custom_potion_effects: nbtlib.tag.List):#更新Potion后，添加进字典components_dict后输出该字典。
    try:
        potion_contents_str = "{potion:'"+Potion+"',"
        try:
            potion_contents_str +="custom_color:"+str(CustomPotionColor+0)+","
        except Exception:
            pass
        try:
            potion_contents_str +="custom_effects:"+serialize_tag(custom_potion_effects)+","
        except Exception:
            pass
        potion_contents_str=potion_contents_str.rstrip(",")+"}"
        components_dict["potion_contents"]=potion_contents_str
    except Exception:
        pass
    return components_dict

def pages_updata(components_dict: dict,id:nbtlib.tag.String,pages:nbtlib.tag.List,filtered_pages,title:nbtlib.tag.String,author:nbtlib.tag.String,generation:nbtlib.tag.Int,resolved:nbtlib.tag.Byte):#更新pages后，添加进字典components_dict后输出该字典。#过滤页面暂未处理
    try:
        if id == 'writable_book' or id == 'minecraft:writable_book' or id == 'written_book' or id == 'minecraft:written_book':
            if type(pages) is nbtlib.tag.List[String]:
                pages_str="{pages:"+serialize_tag(pages)+","
            if type(pages) is nbtlib.tag.List[Compound]:
                pages_str="{pages:"+serialize_tag(pages)+","
        if id == 'written_book' or id == 'minecraft:written_book':
            if title != None:
                pages_str+="title:'"+serialize_tag(title)+"',"
            if author != None:
                pages_str+="author:'"+serialize_tag(author)+"',"
            if generation != None:
                pages_str+="generation:'"+serialize_tag(generation)+"',"
            if resolved != None:
                pages_str+="resolved:'"+serialize_tag(resolved)+"',"
        pages_str=pages_str.rstrip(",")+"}"
        components_dict[id+"_content"]=pages_str
    except Exception:
        pass
    return components_dict

def Trim_updata(components_dict: dict,value: nbtlib.tag.Compound,HideFlags: nbtlib.tag.Int):#更新Trim后，添加进字典components_dict后输出该字典。#过滤页面暂未处理
    try:
        if HideFlags == None:
            HideFlags=0
        try:
            HideFlags += 0
        except Exception:
            HideFlags=0
        bit = (HideFlags >> 7) & 1 #获取第8个二进制位，为1则隐藏
        if bit == 1:
            components_dict["trim"]=serialize_tag(value).rstrip("}")+",show_in_tooltip:false}"
        else:
            components_dict["trim"]=serialize_tag(value)
    except Exception:
        pass
    return components_dict

def effects_updata(components_dict: dict,value: nbtlib.tag.Compound):#更新effects后，添加进字典components_dict后输出该字典。#过滤页面暂未处理
    try:
        components_dict["suspicious_stew_effects"]=serialize_tag(value)
    except Exception:
        pass
    return components_dict

def HideFlags_updata(components_dict: dict,HideFlags: nbtlib.tag.Int):#更新HideFlags后，添加进字典components_dict后输出该字典。#过滤页面暂未处理
    try:
        if HideFlags == None:
            HideFlags=0
        try:
            HideFlags += 0
        except Exception:
            HideFlags=0
        bit = (HideFlags >> 5) & 1 #获取第6个二进制位，为1则隐藏
        if bit == 1:
            components_dict["hide_additional_tooltip"]="{}"
        else:
            pass
    except Exception:
        pass
    return components_dict

def DebugProperty_updata(components_dict: dict,value: nbtlib.tag.Compound):#更新DebugProperty后，添加进字典components_dict后输出该字典。#过滤页面暂未处理
    try:
        components_dict["debug_stick_state"]=serialize_tag(value)
    except Exception:
        pass
    return components_dict

def EntityTag_updata(components_dict: dict,value: nbtlib.tag.Compound):#更新EntityTag后，添加进字典components_dict后输出该字典。#过滤页面暂未处理
    try:
        components_dict["entity_data"]=serialize_tag(value)
    except Exception:
        pass
    return components_dict

def bucket_entity_data_updata(components_dict: dict,NoAI:nbtlib.tag.Byte,Silent:nbtlib.tag.Byte,NoGravity:nbtlib.tag.Byte,Glowing:nbtlib.tag.Byte,Invulnerable:nbtlib.tag.Byte,Health:nbtlib.tag.Float,Age:nbtlib.tag.Int,Variant:nbtlib.tag.Int,HuntingCooldown:nbtlib.tag.Long,BucketVariantTag:nbtlib.tag.Int):#更新bucket_entity_data后，添加进字典components_dict后输出该字典。
    try:
        bucket_entity_str="{"
        if NoAI != None:
            bucket_entity_str+="NoAI:"+serialize_tag(NoAI)+","
        if Silent != None:
            bucket_entity_str+="Silent:"+serialize_tag(Silent)+","
        if NoGravity != None:
            bucket_entity_str+="NoGravity:"+serialize_tag(NoGravity)+","
        if Glowing != None:
            bucket_entity_str+="Glowing:"+serialize_tag(Glowing)+","
        if Invulnerable != None:
            bucket_entity_str+="Invulnerable:"+serialize_tag(Invulnerable)+","
        if Health != None:
            bucket_entity_str+="Health:"+serialize_tag(Health)+","
        if Age != None:
            bucket_entity_str+="Age:"+serialize_tag(Age)+","
        if Variant != None:
            bucket_entity_str+="Variant:"+serialize_tag(Variant)+","
        if HuntingCooldown != None:
            bucket_entity_str+="HuntingCooldown:"+serialize_tag(HuntingCooldown)+","
        if BucketVariantTag != None:
            bucket_entity_str+="BucketVariantTag:"+serialize_tag(BucketVariantTag)+","
        bucket_entity_str=bucket_entity_str.rstrip(",")+"}"
        if bucket_entity_str != "{}":
            components_dict["bucket_entity_data"]=bucket_entity_str
    except Exception:
        pass
    return components_dict

def instrument_updata(components_dict: dict,value: nbtlib.tag.Compound):#更新instrument后，添加进字典components_dict后输出该字典。
    try:
        components_dict["instrument"]=serialize_tag(value)
    except Exception:
        pass
    return components_dict

def Recipes_updata(components_dict: dict,value: nbtlib.tag.List):#更新Recipes后，添加进字典components_dict后输出该字典。
    try:
        components_dict["recipes"]=serialize_tag(value)
    except Exception:
        pass
    return components_dict

def Lodestone_updata(components_dict: dict,LodestoneDimension: nbtlib.tag.String,LodestonePos:nbtlib.tag.Compound,LodestoneTracked:nbtlib.tag.Byte):#更新Lodestone后，添加进字典components_dict后输出该字典。   #MC目前未能识别，暂不处理  
    try:
        lodestone_target_str="{target:{"
        if LodestoneDimension!=None:
            lodestone_target_str+="dimension:"+serialize_tag(LodestoneDimension)+","
        if LodestonePos!=None:
            lodestone_target_str+="pos:["+serialize_tag(LodestonePos.get("X"))+","+serialize_tag(LodestonePos.get("Y"))+","+serialize_tag(LodestonePos.get("Z"))+"],"
        if LodestoneTracked!=None:
            lodestone_target_str+="tracked:"+serialize_tag(LodestoneTracked)+","
        lodestone_target_str=lodestone_target_str.rstrip(",")+"}}"
        components_dict["lodestone_tracker"]=lodestone_target_str
    except Exception:
        pass
    return components_dict

def Explosion_updata(components_dict: dict,Explosion: nbtlib.tag.Compound):#更新Explosion后，添加进字典components_dict后输出该字典。
    try:
        firework_explosion_str="{"
        if Explosion.get("Type")!=None:
            if Explosion.get("Type") == 0:
                firework_explosion_str+="shape:'small_ball',"
            if Explosion.get("Type") == 1:
                firework_explosion_str+="shape:'large_ball',"
            if Explosion.get("Type") == 2:
                firework_explosion_str+="shape:'star',"
            if Explosion.get("Type") == 3:
                firework_explosion_str+="shape:'creeper',"
            if Explosion.get("Type") == 4:
                firework_explosion_str+="shape:'burst',"
        if Explosion.get("Colors")!=None:
            firework_explosion_str+="colors:"+serialize_tag(Explosion.get("Colors"))+","
        if Explosion.get("FadeColors")!=None:
            firework_explosion_str+="fade_colors:"+serialize_tag(Explosion.get("FadeColors"))+","
        if Explosion.get("Trail")!=None:
            firework_explosion_str+="has_trail:"+serialize_tag(Explosion.get("Trail"))+","
        if Explosion.get("Flicker")!=None:
            firework_explosion_str+="has_twinkle:"+serialize_tag(Explosion.get("Flicker"))+","
        firework_explosion_str=firework_explosion_str.rstrip(",")+"}"
        components_dict["firework_explosion"]=firework_explosion_str
    except Exception:
        pass
    return components_dict

def Fireworks_updata(components_dict: dict,Explosions: nbtlib.tag.Compound,Flight:nbtlib.tag.Byte):#更新Fireworks后，添加进字典components_dict后输出该字典。
    try:
        fireworks_str="{"
        if Explosions != None:
            fireworks_str+="explosions:["
            for i in Explosions:
                fireworks_str+="{"
                if i.get("Type")!=None:
                    if i.get("Type") == 0:
                        fireworks_str+="shape:'small_ball',"
                    if i.get("Type") == 1:
                        fireworks_str+="shape:'large_ball',"
                    if i.get("Type") == 2:
                        fireworks_str+="shape:'star',"
                    if i.get("Type") == 3:
                        fireworks_str+="shape:'creeper',"
                    if i.get("Type") == 4:
                        fireworks_str+="shape:'burst',"
                if i.get("Colors")!=None:
                    fireworks_str+="colors:"+serialize_tag(i.get("Colors"))+","
                if i.get("FadeColors")!=None:
                    fireworks_str+="fade_colors:"+serialize_tag(i.get("FadeColors"))+","
                if i.get("Trail")!=None:
                    fireworks_str+="has_trail:"+serialize_tag(i.get("Trail"))+","
                if i.get("Flicker")!=None:
                    fireworks_str+="has_twinkle:"+serialize_tag(i.get("Flicker"))+","
                fireworks_str=fireworks_str.rstrip(",")+"},"
            fireworks_str=fireworks_str.rstrip(",")+"],"

        if Flight != None:
            if type(Flight) == nbtlib.tag.String:#去除前后的"
                Flight_str = serialize_tag(Flight)[1:-1]
            else:
                Flight_str = serialize_tag(Flight)
            fireworks_str+="flight_duration:"+Flight_str
        fireworks_str=fireworks_str.rstrip(",")+"}"
        components_dict["fireworks"]=fireworks_str
    except Exception:
        pass
    return components_dict

def SkullOwner_updata(components_dict: dict,SkullOwner: nbtlib.tag.Compound):#更新SkullOwner后，添加进字典components_dict后输出该字典。
    try:
        profile_str="{"
        if type(SkullOwner) is nbtlib.tag.String:
            profile_str+="name:"+serialize_tag(SkullOwner)+"}"
        else:
            if SkullOwner.get("Name")!=None:
                profile_str+="name:"+serialize_tag(SkullOwner.get("Name"))+","
            if SkullOwner.get("Id")!=None:
                profile_str+="id:"+serialize_tag(SkullOwner.get("Id"))+","
            if SkullOwner.get("Properties")!=None:
                print("玩家头颅处理中，暂未处理玩家档案配置属性Properties")
            profile_str=profile_str.rstrip(",")+"}"
        components_dict["profile"]=profile_str
    except Exception:
        pass
    return components_dict

def BlockEntityTag_updata(components_dict: dict,id:String,BlockEntityTag: nbtlib.tag.Compound):#更新BlockEntityTag后，添加进字典components_dict后输出该字典。
    try:
        if BlockEntityTag.get("note_block_sound")!=None:
            components_dict["note_block_sound"]=serialize_tag(BlockEntityTag.pop("note_block_sound"))
        #Base
        if BlockEntityTag.get("Base")!=None:
            if BlockEntityTag.get("Base")==0:
                components_dict["base_color"]='white'
            elif BlockEntityTag.get("Base")==1:
                components_dict["base_color"]='orange'
            elif BlockEntityTag.get("Base")==2:
                components_dict["base_color"]='magenta'
            elif BlockEntityTag.get("Base")==3:
                components_dict["base_color"]='light_blue'
            elif BlockEntityTag.get("Base")==4:
                components_dict["base_color"]='yellow'
            elif BlockEntityTag.get("Base")==5:
                components_dict["base_color"]='lime'
            elif BlockEntityTag.get("Base")==6:
                components_dict["base_color"]='pink'
            elif BlockEntityTag.get("Base")==7:
                components_dict["base_color"]='gray'
            elif BlockEntityTag.get("Base")==8:
                components_dict["base_color"]='light_gray'
            elif BlockEntityTag.get("Base")==9:
                components_dict["base_color"]='cyan'
            elif BlockEntityTag.get("Base")==10:
                components_dict["base_color"]='purple'
            elif BlockEntityTag.get("Base")==11:
                components_dict["base_color"]='blue'
            elif BlockEntityTag.get("Base")==12:
                components_dict["base_color"]='brown'
            elif BlockEntityTag.get("Base")==13:
                components_dict["base_color"]='green'
            elif BlockEntityTag.get("Base")==14:
                components_dict["base_color"]='red'
            elif BlockEntityTag.get("Base")==15:
                components_dict["base_color"]='black'
            BlockEntityTag_Base=BlockEntityTag.pop("Base")
        #Patterns
        if BlockEntityTag.get("Patterns")!=None:
            Patterns_str="["
            for i in BlockEntityTag.get("Patterns"):
                Patterns_str+="{pattern:"+serialize_tag(i.pop("Pattern"))+","
                if i.get("Color")!= None:
                    Patterns_str+="color:"+serialize_tag(i.pop("Color"))+"},"
            Patterns_str=Patterns_str.rstrip(",")+"]"
            components_dict["banner_patterns"]=Patterns_str
        #sherds
        if BlockEntityTag.get("sherds")!=None:
            components_dict["pot_decorations"]=serialize_tag(BlockEntityTag.pop("sherds"))
        #Items
        if BlockEntityTag.get("Items")!=None:
            Items_str="["
            for i in BlockEntityTag.pop("Items"):
                Items_str+="{"
                if i.get("Slot")!= None:
                    Items_str+="slot:"+serialize_tag(i.pop("Slot"))+","
                Items_str+="item:"+Item_Common_tags_updata(i)
                Items_str=Items_str.rstrip(",")+"},"
            Items_str=Items_str.rstrip(",")+"]"

            #shulker_boxes = ["shulker_box","white_shulker_box","orange_shulker_box","magenta_shulker_box","light_blue_shulker_box","yellow_shulker_box","lime_shulker_box","pink_shulker_box","gray_shulker_box","light_gray_shulker_box","cyan_shulker_box","purple_shulker_box","brown_shulker_box", "blue_shulker_box","green_shulker_box","red_shulker_box","black_shulker_box"]
            #if id in shulker_boxes:#潜影盒
            components_dict["container"]=Items_str
        #Bees
        if BlockEntityTag.get("Bees")!=None:
            Bees_str="["
            for i in BlockEntityTag.get("Bees"):
                Bees_str+="{"
                if i.get("EntityData")!=None:
                    Bees_str+="entity_data:"+serialize_tag(i.pop("EntityData"))+","
                if i.get("MinOccupationTicks")!=None:
                    Bees_str+="min_ticks_in_hive:"+serialize_tag(i.pop("MinOccupationTicks"))+","
                if i.get("TicksInHive")!=None:
                    Bees_str+="ticks_in_hive:"+serialize_tag(i.pop("TicksInHive"))+","
                Bees_str=Bees_str.rstrip(",")+"},"
            Bees_str=Bees_str.rstrip(",")+"]"
            components_dict["bees"]=Bees_str
        #Lock
        if BlockEntityTag.get("Lock")!=None:
            components_dict["lock"]=serialize_tag(BlockEntityTag.pop("Lock"))
        #LootTable
        if BlockEntityTag.get("LootTable")!=None:
            LootTable_str="{loot_table:"+serialize_tag(BlockEntityTag.pop("LootTable"))
            if BlockEntityTag.get("LootTableSeed")!=None:
                LootTable_str+=",seed:"+serialize_tag(BlockEntityTag.pop("LootTableSeed"))
            LootTable_str+="}"
            components_dict["container_loot"]=LootTable_str
        #其余内容变为block_entity_data
        if BlockEntityTag.items():
            components_dict["block_entity_data"]=serialize_tag(BlockEntityTag)
    except Exception:
        pass
    return components_dict

def BlockStateTag_updata(components_dict: dict,BlockStateTag: nbtlib.tag.Compound):#更新BlockStateTag后，添加进字典components_dict后输出该字典。
    try:
        components_dict["block_state"]=serialize_tag(BlockStateTag)
    except Exception:
        pass
    return components_dict

def Item_Common_tags_updata(Item:nbtlib.tag.Compound):#处理嵌套物品NBT，输入被nbtlib解析过的嵌套物品NBT格式，其字符串形式为'{id:"diamond_sword",Count:1,tag:{Damage:233}}'，输出为转化成嵌套物品的组件形式，如'{id:'diamond_sword',count:1,components:{damage:233}}'
    Item_str="{"
    id=Item.get("id",None)
    Count=Item.get("count",None)
    tag=Item.get("tag",None)#Compound
    if id!=None:
        Item_str+="id:"+serialize_tag(id)+","
    if Count!=None:
        Item_str+="count:"+serialize_tag(Count)+","
    if tag!=None:
        Item_str+="components:"+updata_dict_to_str_2(item_nbt_updata_to_dict(id,tag))+","#暂未处理tag
    Item_str=Item_str.rstrip(",")+"}"
    return Item_str

#组件键值转化
def updata_dict_to_str_1(components_dict:dict):#将NBT格式更新完成后的字典components_dict组成MC命令可识别的写法，输出类型为String，也是最终结果。
    components_str="["
    for key,value in components_dict.items():
        components_str+=key+"="+value+","
    components_str=components_str.rstrip(",")+"]"
    return components_str
def updata_dict_to_str_2(components_dict:dict):#将NBT格式更新完成后的字典components_dict组成MC物品嵌套中可识别的写法，输出类型为String，也是最终结果。
    components_str="{"
    for key,value in components_dict.items():
        components_str+=key+":"+value+","
    components_str=components_str.rstrip(",")+"}"
    return components_str

#打包
def transfer(id:String,nbt:String,type=1):#输入 物品ID 和 物品NBT格式，根据type的数值来输出。
    try:
        if type ==1:#输出成MC命令可识别的components写法，输出类型为String。
            return updata_dict_to_str_1(item_nbt_updata_to_dict(id,parse_nbt(nbt)))
        else:#输出成MC物品嵌套中可识别的写法，输出类型为String。
            return "components:"+updata_dict_to_str_2(item_nbt_updata_to_dict(id,parse_nbt(nbt)))
    except Exception:
        return updata_dict_to_str_1(item_nbt_updata_to_dict(id,parse_nbt(nbt)))