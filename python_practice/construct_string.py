# encoding:utf-8

var1 = 'Router1'
var2 = 'CPU0'
var3 = 2

old_bird = "insert into TABLE1 VALUES ('%s','%s',%d)" % (var1, var2, var3)
new_bee = "insert into TABLE1 VALUES ('" + var1 + "','" + var2 + "'," + str(var3) + ")"

print '---The elegant way---\n', old_bird
print '---newbee would choose this---\n', new_bee
