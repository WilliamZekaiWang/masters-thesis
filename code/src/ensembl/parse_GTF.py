import sys
import re

infile = sys.argv[1]
outfile = sys.argv[2]

with open(infile, 'r') as file, open(outfile, 'w') as output:
    seen = set()

    # write header
    output.write('gene_id' +'\t'+ 'version' +'\t'+ 'chr' +'\t'+ 'TSS\n')

    for row in file:
        if row[0] != '#': # not meta
            row = row.split('\t')
            #chr,source,feature,start,end,score,strand,frame,attributes

            #regex for gene and id
            gene_id = re.match(r'gene_id "([^"]+)"',row[8]).group(1)
            version = re.match(r'.*gene_version "([^"]+)"',row[8]).group(1)


            # check if it's a gene
            if row[2] == 'gene' and not gene_id in seen:
                seen.add(gene_id)

                # check if it's positive for neg
                if row[6] == '+':
                    TSS = 3
                else:
                    TSS = 4
                
                output.write(gene_id +'\t'+ version +'\t'+ row[0] +'\t'+ row[TSS] +'\n')