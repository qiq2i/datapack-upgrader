def parse_nbt(s):
    # 使用逗号和冒号进行分割，并考虑字符串类型的情况
    pairs = s[1:-1]
    nbt= ""
    nbt_value= ""
    i_is_comma = 0
    i_is_colon = 0
    i_is_list = 0
    i_is_nesting = 0
    i_is_str1 = 0
    i_is_str2 = 0
    locate = None
    nbt_dirt = {}
    for i in pairs:
        if i == '"': #是"
            if locate == None:
                locate = "str1"
        if i == "'": #是'
            if locate == None:
                locate = "str2"
        if i == "[": #是[
            if locate == None:
                locate = "list"
        if i == "{": #是{
            if locate == None:
                locate = "nesting"
        #print(locate,i,i_is_nesting)
        if locate == "str1": #在引号"内
            if i == '"':#是"
                i_is_str1 += 1
            if i_is_colon == i_is_comma: #NBT
                nbt += i
            if i_is_colon > i_is_comma: #NBT的值
                nbt_value += i
            if i_is_str1 >= 2:
                locate = None
                i_is_str1 = 0
        elif locate == "str2": #在引号'内
            if i == "'":#是'
                i_is_str2 += 1
            if i_is_colon == i_is_comma: #NBT
                nbt += i
            if i_is_colon > i_is_comma: #NBT的值
                nbt_value += i
            if i_is_str2 >= 2:
                locate = None
                i_is_str2 = 0
        elif locate == "list": #在[]内
            if i == "[":#进入[]
                i_is_list += 1
            if i == "]":#离开[]
                i_is_list -= 1
            if i_is_colon == i_is_comma: #NBT
                nbt += i
            if i_is_colon > i_is_comma: #NBT的值
                nbt_value += i
            if i_is_list == 0:
                locate = None
        elif locate == "nesting": #在{}内
            if i == "{":#进入{}
                i_is_nesting += 1
            if i == "}":#离开{}
                i_is_nesting -= 1
            if i_is_colon == i_is_comma: #NBT
                nbt += i
            if i_is_colon > i_is_comma: #NBT的值
                nbt_value += i
            if i_is_nesting == 0:
                locate = None
        else:
            if i == ",": #碰到了,
                i_is_comma += 1
                nbt_dirt[nbt]=nbt_value
                nbt= ""
                nbt_value= ""
            if i == ":": #碰到了:
                i_is_colon += 1
            if i != "," and i != ":" and i != "'" and i != '"' and i != '['and i != ']'and i != '{'and i != '}': #是否可以成为NBT或NBT的值
                if i_is_colon == i_is_comma: #NBT
                    nbt += i
                if i_is_colon > i_is_comma: #NBT的值
                    nbt_value += i
    nbt_dirt[nbt]=nbt_value
    return nbt_dirt
# 测试
s = '{ab:"ab,cd",\'cd\':\'ab\',D:2}'
print(parse_nbt(s))  # 输出：{'ab': '"ab,cd"', "'cd'": "'ab'", 'D': '2'}
