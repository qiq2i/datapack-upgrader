import nbt_to_components

#例子1-可染色物品，及通用NBT
print("测试1")
s = '''{CanPlaceOn:["minecraft:ice","minecraft:mud"],CanDestroy:["minecraft:fern","minecraft:lava"],display:{Name:'[{"text":"233","color":"gold","bold":true,"italic":true,"underlined":true,"strikethrough":true,"obfuscated":true},{"text":"666777","font":"6","bold":true}]',Lore:['{"text":"112233","bold":true,"italic":true}'],color:1011},HideFlags:129,CustomModelData:12345678,Enchantments:[{id:"minecraft:protection",lvl:3s},{id:"minecraft:thorns",lvl:11s}],AttributeModifiers:[{AttributeName:"generic.max_health",Name:"generic.max_health",Amount:10,Operation:0,UUID:[I;317531815,114708043,-1774063036,1637657640]},{AttributeName:"generic.knockback_resistance",Name:"generic.knockback_resistance",Amount:23,Operation:1,UUID:[I;-1554795033,723864717,-1969707662,611632905],Slot:"mainhand"}],a:"abc"}'''
#print(parse_nbt(s))
print(nbt_to_components.transfer("leather",s))

#测试2 - 书与笔 和 成书
print("测试2")
s = '{pages:["123\n123","213"]}'
d = '{Trim:{material:"minecraft:gold",pattern:"minecraft:eye"}}'
#print(parse_nbt(s))
print(nbt_to_components.transfer("writable_book",s))
#print(parse_nbt(d))
print(nbt_to_components.transfer("written_book",d))

#测试3 - 磁石指针
print("测试3")
s = '{LodestoneDimension:"minecraft:overworld",LodestoneTracked:1b,LodestonePos:{X:1,Y:2,Z:3}}'
print(nbt_to_components.transfer("compass",s))

#测试4 - 烟火之星
print("测试4")
s = '{Explosion:{Type:1,Flicker:1b,Trail:1b,Colors:[I;5057023],FadeColors:[I;9895769]}}'
print(nbt_to_components.transfer("firework_star",s))

#测试5 - 烟花火箭
print("测试5")
s = '{Fireworks:{Flight:10b,Explosions:[{Type:1,Flicker:1b,Trail:1b,Colors:[I;7553279],FadeColors:[I;16770503]},{Type:0,Trail:1b}]}}'
print(nbt_to_components.transfer("firework_rocket",s))

#测试6 - 头颅
print("测试6")
s = '{SkullOwner:"xiao_qi_zi",BlockEntityTag:{note_block_sound:"minecraft:ambient.cave"}}'
print(nbt_to_components.transfer("player_head",s))

#测试7 - 陶罐
print("测试7")
s = '{BlockEntityTag:{sherds:["minecraft:archer_pottery_sherd","minecraft:brick","minecraft:brick","minecraft:brick"]}}'
print(nbt_to_components.transfer("decorated_pot",s))

#测试8 - 弩
print("测试8")
s = '{RepairCost:233,Unbreakable:1b,Damage:3,ChargedProjectiles:[{id:"minecraft:firework_rocket",Count:1b,tag:{Fireworks:{Flight:233b,Explosions:[{Type:0}]}}},{id:"minecraft:arrow",Count:1b},{}],Charged:1b}'
print(nbt_to_components.transfer("crossbow",s))

#测试9 - 收纳袋
print("测试9")
s = '''{Items:[{id:"minecraft:bow",Count:1b,tag:{Damage:233}},{id:"minecraft:egg",Count:3b,tag:{display:{Name:'{"text":"nihao"}'}}}]}'''
print(nbt_to_components.transfer("bundle",s))

#测试10 - 箱子
print("测试10")
s = '''{BlockEntityTag:{Items:[{Slot:2b,id:"minecraft:bow",Count:1b,tag:{Damage:3}},{Slot:9b,id:"minecraft:egg",Count:12b}]}}'''
print(nbt_to_components.transfer("chest",s))