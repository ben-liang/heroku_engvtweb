import pandas
import os

FILE = os.path.expanduser('~/qbpcatalog.txt')
df = pandas.io.parsers.read_csv(FILE, sep='\t', header=0)

parts_objs = []
for i in range(0, len(df)):
    row = df.ix[i]
    floatFields = ['MSRP', 'MAP', 'Each Cost', 'Weight', 'Length', 'Width', 'Height']
    for field in floatFields:
        try:
            float(row[field])
            break
        except ValueError:
            print 'Row %s\tField %s' % (i, field)
