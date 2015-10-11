import csv

# Reactions
with open('Transcription_RX.csv', 'rU') as f:
  with open('Transcription_RX_mod.csv', 'w') as wf:
    r = csv.reader(f, delimiter=',', dialect=csv.excel_tab)
    rows = list(r)

    w = csv.writer(wf, dialect=csv.excel)
    w.writerow(rows[0])
    
    for row in rows[1:]:
      id_ = row[0]
      name = row[1]
      stoich = row[2]
      ratelaw = row[4]
      rateparams = row[5]

      newrow = row

      new_ratelaw = ratelaw + '*min(RNA_POLYMERASE, MG_282_MONOMER)*ATP*CTP*GTP*UTP/( (1+ATP/Km1_tx) * (1 + CTP/Km2_tx) * (1 + GTP/Km3_tx) * (1 + UTP/Km4_tx) )'

      newrow[4] = new_ratelaw

      w.writerow(newrow)
