dic1={1:101, 2:201}
dic2={3:301, 4:410}
dic3={5:510,6:641}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)