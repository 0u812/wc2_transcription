import phrasedml as p

with open('sedml_webtools_transcription.xml') as f:
  sedml = f.read()

pml = p.convertString(sedml)

with open('phrasedml_converted_transcription.phrasedml', 'w') as f:
  f.write(pml)
