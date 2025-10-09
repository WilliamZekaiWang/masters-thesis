import sys

# GTF is my input, ensg is what im checking to make sure everything is in
gtf_in = sys.argv[1]
ensg_in = sys.argv[2]

known = set()
found = set()
with open(gtf_in, 'r') as gtf, open(ensg_in, 'r') as en:
    # get the ENSG, and strip the version
    knwon = set(map(lambda x:x[:x.index('.')], en.readline().split('\t')[2:]))

    # this should be all of them from gtf file
    for row in gtf:
        found.add(row.split('\t')[0])

    print(known.issubset(found))