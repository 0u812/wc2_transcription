import csv

# Reactions
with open('../spreadsheets/RNADecay_RX.csv', 'rU') as f:
  with open('../spreadsheets/RNADecay_RX_mod.csv', 'w') as wf:
    r = csv.reader(f, delimiter=',', dialect=csv.excel_tab)
    rows = list(r)

    w = csv.writer(wf, dialect=csv.excel)
    w.writerow(rows[0])

    for row in rows[1:]:
      id_ = row[0]
      molecule = id_[10:]
      #print(molecule)
      name = row[1]
      stoich = row[2]
      ratelaw = row[4]
      rateparams = row[5]

      newrow = row

      new_ratelaw = ratelaw + '*MG_0003/(1 + {}/Km_RNA_decay)'.format(molecule)

      newrow[4] = new_ratelaw

      w.writerow(newrow)
