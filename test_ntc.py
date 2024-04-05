from nbt_to_components import transfer

#例子1-可染色物品，及通用NBT
print("测试1")
s = '''{CanPlaceOn:["minecraft:ice","minecraft:mud"],CanDestroy:["minecraft:fern","minecraft:lava"],display:{Name:'[{"text":"233","color":"gold","bold":true,"italic":true,"underlined":true,"strikethrough":true,"obfuscated":true},{"text":"666777","font":"6","bold":true}]',Lore:['{"text":"112233","bold":true,"italic":true}'],color:1011},HideFlags:129,CustomModelData:12345678,Enchantments:[{id:"minecraft:protection",lvl:3s},{id:"minecraft:thorns",lvl:11s}],AttributeModifiers:[{AttributeName:"generic.max_health",Name:"generic.max_health",Amount:10,Operation:0,UUID:[I;317531815,114708043,-1774063036,1637657640]},{AttributeName:"generic.knockback_resistance",Name:"generic.knockback_resistance",Amount:23,Operation:1,UUID:[I;-1554795033,723864717,-1969707662,611632905],Slot:"mainhand"}],a:"abc"}'''
#print(parse_nbt(s))
print(transfer("leather",s))

#测试2 - 书与笔 和 成书
print("测试2")
s = '{pages:["123\n123","213"]}'
d = '{Trim:{material:"minecraft:gold",pattern:"minecraft:eye"}}'
#print(parse_nbt(s))
print(transfer("writable_book",s))
#print(parse_nbt(d))
print(transfer("written_book",d))

#测试3 - 磁石指针
print("测试3")
s = '{LodestoneDimension:"minecraft:overworld",LodestoneTracked:1b,LodestonePos:{X:1,Y:2,Z:3}}'
print(transfer("compass",s))

#测试4 - 烟火之星
print("测试4")
s = '{Explosion:{Type:1,Flicker:1b,Trail:1b,Colors:[I;5057023],FadeColors:[I;9895769]}}'
print(transfer("firework_star",s))

#测试5 - 烟花火箭
print("测试5")
s = '{Fireworks:{Flight:10b,Explosions:[{Type:1,Flicker:1b,Trail:1b,Colors:[I;7553279],FadeColors:[I;16770503]},{Type:0,Trail:1b}]}}'
print(transfer("firework_rocket",s))

#测试6 - 头颅
print("测试6")
s = '{SkullOwner:"xiao_qi_zi",BlockEntityTag:{note_block_sound:"minecraft:ambient.cave"}}'
print(transfer("player_head",s))

#测试7 - 陶罐
print("测试7")
s = '{BlockEntityTag:{sherds:["minecraft:archer_pottery_sherd","minecraft:brick","minecraft:brick","minecraft:brick"]}}'
print(transfer("decorated_pot",s))

#测试8 - 弩
print("测试8")
s = '{RepairCost:233,Unbreakable:1b,Damage:3,ChargedProjectiles:[{id:"minecraft:firework_rocket",Count:1b,tag:{Fireworks:{Flight:233b,Explosions:[{Type:0}]}}},{id:"minecraft:arrow",Count:1b},{}],Charged:1b}'
print(transfer("crossbow",s))

#测试9 - 收纳袋
print("测试9")
s = '''{Items:[{id:"minecraft:bow",Count:1b,tag:{Damage:233}},{id:"minecraft:egg",Count:3b,tag:{display:{Name:'{"text":"nihao"}'}}}]}'''
print(transfer("bundle",s))

#测试10 - 箱子
print("测试10")
s = '''{BlockEntityTag:{Items:[{Slot:2b,id:"minecraft:bow",Count:1b,tag:{Damage:3}},{Slot:9b,id:"minecraft:egg",Count:12b}]}}'''
print(transfer("chest",s))

#测试11
print("测试11")
s = '''{CanPlaceOn:["minecraft:ice","minecraft:mud"],CanDestroy:["minecraft:bell","minecraft:tnt","minecraft:dirt"],display:{Name:'{"text":"大礼包","color":"green","bold":true,"underlined":true}'},HideFlags:128,CustomModelData:123456,a:1,b:2,c:3,Enchantments:[{id:"minecraft:flame",lvl:15s},{id:"minecraft:power",lvl:20s}],AttributeModifiers:[{AttributeName:"generic.max_health",Name:"generic.max_health",Amount:10,Operation:0,UUID:[I;1252358603,-1539225956,-1477859009,836212788],Slot:"mainhand"},{AttributeName:"generic.attack_damage",Name:"generic.attack_damage",Amount:20,Operation:0,UUID:[I;-1185730063,1295926585,-1519262741,-400858813],Slot:"offhand"}],BlockEntityTag:{Items:[{Slot:0b,id:"minecraft:crossbow",Count:13b,tag:{RepairCost:20,Unbreakable:1b,Damage:100,Enchantments:[{id:"minecraft:multishot",lvl:111s},{id:"minecraft:piercing",lvl:222s},{id:"minecraft:quick_charge",lvl:255s}],ChargedProjectiles:[{id:"minecraft:arrow",Count:1b},{id:"minecraft:tipped_arrow",Count:1b,tag:{Potion:"minecraft:water"}},{id:"minecraft:arrow",Count:1b}],Charged:1b}},{Slot:1b,id:"minecraft:firework_rocket",Count:1b,tag:{Fireworks:{Flight:4b,Explosions:[{Type:0},{Type:1,Flicker:1b,Trail:1b,Colors:[I;2883371],FadeColors:[I;16772999]}]}}},{Slot:2b,id:"minecraft:bundle",Count:1b,tag:{Items:[{id:"minecraft:tnt",Count:1b},{id:"minecraft:player_head",Count:1b,tag:{SkullOwner:"xiao_qi_zi"}}]}}]}}'''
print(transfer("chest",s))