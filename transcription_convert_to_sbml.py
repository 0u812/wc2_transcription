import antimony

with open('transcription.sb') as f:
  sb = f.read()

print(sb)

res = antimony.loadString(sb)

if res < 0:
  print(antimony.getLastError())

print(res)
print(antimony.getModuleNames())
print(antimony.getModuleNames()[0])

sbml = antimony.getSBMLString(antimony.getModuleNames()[0])

with open('transcription_sbml.xml', 'w') as f:
  f.write(sbml)