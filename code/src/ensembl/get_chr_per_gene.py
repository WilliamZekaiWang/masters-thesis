# given fithic data and gene TSS, find the significant contact regions

import sys
import csv # so much more readable
import json
import math

contact_list = sys.argv[1]
gene_list = sys.argv[2]
outfile = sys.argv[3]
resolution = int(sys.argv[4])

# Chrs from the pairs metadata
chrom_sizes = {
    "chr1": 248956422,
    "chr2": 242193529,
    "chr3": 198295559,
    "chr4": 190214555,
    "chr5": 181538259,
    "chr6": 170805979,
    "chr7": 159345973,
    "chr8": 145138636,
    "chr9": 138394717,
    "chr10": 133797422,
    "chr11": 135086622,
    "chr12": 133275309,
    "chr13": 114364328,
    "chr14": 107043718,
    "chr15": 101991189,
    "chr16": 90338345,
    "chr17": 83257441,
    "chr18": 80373285,
    "chr19": 58617616,
    "chr20": 64444167,
    "chr21": 46709983,
    "chr22": 50818468,
    "chrX": 156040895,
    "chrY": 57227415
}


# start making the contacts matrix {chr: {pos from 0 to chr size by res: {gene: [(TSS chr, TSS start, TSS end), (sig chr, sig start, sig end)]}}}
contacts = {}
for chrm, length in chrom_sizes.items():
    contacts[chrm] = {}
    for i in range(resolution, length, resolution):
        contacts[chrm][i] = {}

all_chrs = list(map(str, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,'X','Y']))
with open(contact_list, 'r') as fithic, open(gene_list, 'r') as genes:
    
    # populate our contact genes
    genes = csv.DictReader(genes, delimiter='\t')
    for row in genes:
        TSS1 = math.ceil(int(row['TSS1'])/resolution)*resolution # get the positions and see what bin
        TSS2 = math.ceil(int(row['TSS2'])/resolution)*resolution

        contacts[row['chr']][TSS1].update({row['gene_id']: [(row['chr'], row['TSS1'], row['TSS2'])]})
        if TSS1 != TSS2: # the TSS is not fully in one bin, put in the second one
            contacts[row['chr']][TSS2].update({row['gene_id']: [(row['chr'], row['TSS1'], row['TSS2'])]})


    # let's populate the significant contact regions in (chr, start, end) into the above mat
    fithic = csv.DictReader(fithic, delimiter='\t')
    for row in fithic:
        
        # THIS ONLY WORKS IF FITHIC2 DATA IS SAME RESOLUTION
        if float(row['q-value']) < 0.05:
            # left side end ranges
            frag1b = math.ceil(int(row['fragmentMid1'])/resolution)*resolution
            frag1t = math.floor(int(row['fragmentMid1'])/resolution)*resolution

            # right side
            frag2b = math.ceil(int(row['fragmentMid2'])/resolution)*resolution
            frag2t = math.floor(int(row['fragmentMid2'])/resolution)*resolution
            for gene in contacts[row['chr1']][frag1b]:
                contacts[row['chr1']][frag1b][gene].append(
                    # each gene now has the sig contact point
                    (row['chr2'], frag2b, frag2t) 
                    )
            
            # do the same for the other side
            if float(row['q-value']) < 0.05:
                for gene in contacts[row['chr2']][frag2t]:
                    contacts[row['chr2']][frag2t][gene].append(
                        # each gene now has the sig contact point
                        (row['chr1'], frag1b, frag1t) 
                        )

with open(outfile, 'w') as out:
    json.dump(contacts, out, indent=3)