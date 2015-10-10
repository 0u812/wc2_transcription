import antimony
import csv

# Species
with open('Transcription_SP.csv', 'rU') as f:
  r = csv.reader(f, delimiter=',', dialect=csv.excel_tab)
  for row in r:
    print(row)
