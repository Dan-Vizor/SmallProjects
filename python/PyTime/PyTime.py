#!/usr/bin/python
import time
loop = 500

print("start")
def test():
  t1 = time.time()
  var = 1
  t2 = time.time()
  vartime = t2 - t1
  
  doc = open("doc.txt", "w")
  t1 = time.time()
  for x in range(0,4):
    doc.write("0")
  t2 = time.time()
  ptime = t2 - t1 - vartime
  return ptime / 4

testdata = []
for x in range(0,loop):
  testdata += [test()]

add = 0
for x in range(0,loop):
  add += testdata[x]

out = add /loop
print("end\n")
print(str(out * 1000000) + " for 1GB")# 1GB