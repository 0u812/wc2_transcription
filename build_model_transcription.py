#import antimony
import csv

out = ''

comps = set()

# Species
with open('Transcription_SP.csv', 'rU') as f:
  r = csv.reader(f, delimiter=',', dialect=csv.excel_tab)
  for row in list(r)[1:]:
    #print(row)
    # ID
    id_ = row[0]
    # Display name
    name = row[1]
    # Compartment
    comp = row[2]
    # Copy number
    copies = int(row[3])
    # Type
    tp = row[4]
    # Role
    role = row[5]

    out += '  var species {};\n'.format(id_)
    # initial conc.
    out += '  {} = {} items;\n'.format(id_, copies)
    # compartment
    out += '  {} in {};\n'.format(id_, comp)
    # display name
    out += '  {} is "{}";\n'.format(id_, name)

    comps.add(comp)

    out += '\n'

for c in comps:
  out = '  const compartment {};\n\n'.format(c) + out

out = '  Km1_tx = 1;\n  Km2_tx = 1;\n  Km3_tx = 1;\n  Km4_tx = 1;\n' + out
out = 'model transcription()\n' + out
out = 'function min(x,y)\n  piecewise(x,x<y,y)\nend\n\n' + out

# Reactions
with open('Transcription_RX.csv', 'rU') as f:
  r = csv.reader(f, delimiter=',', dialect=csv.excel_tab)
  for row in list(r)[1:]:
    #id_ = row[0][14:]
    id_ = row[0]
    print(id_)
    name = row[1]
    stoich = row[2]
    ratelaw = row[4]
    rateparams = row[5]

    out += '  {}: {}; {};\n'.format(id_, stoich, ratelaw)
    out += '  {};\n'.format(rateparams)
    # display name
    out += '  {} is "{}";\n'.format(id_, name)

    out += '\n'

out += 'end'

print(out)
#print(comps)

with open('transcription.sb', 'w') as f:
  f.write(out)
