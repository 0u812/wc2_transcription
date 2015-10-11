import tesedml

doc = tesedml.openDoc('sedml_webtools_gillespie_transcription.xml')
r = doc.run()[0]
print(r)
