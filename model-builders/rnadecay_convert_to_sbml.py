import antimony

with open('../model/rnadecay.sb') as f:
  sb = f.read()

print(sb)

res = antimony.loadString(sb)

if res < 0:
  print(antimony.getLastError())

print(res)
print(antimony.getModuleNames())
print(antimony.getModuleNames()[-1])

sbml = antimony.getSBMLString(antimony.getModuleNames()[-1])

with open('../model/rnadecay_sbml.xml', 'w') as f:
  f.write(sbml)
