import sys
import gzip
import os

file = sys.argv[1]
basename = os.path.basename(file).replace('.gz', '')
out_path = os.path.join('links/scratch', basename + '.sizes')

with gzip.open(file, 'rt') as pairs, open(out_path, 'w') as output:
    for row in pairs:
        if row.startswith('#chrom'):
            output.write(row[12:])
        elif not row.startswith('#'):
            break

