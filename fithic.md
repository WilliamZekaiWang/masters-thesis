### Generating Files

- creating contact matrix file from pairs file (ENCODE, generated from pairix):
  - pair format (ligated together read, where frag is restriction enyzmes)
    - metadata including chr lens
    - readID chr1 pos1 chr2 pos2 strand1 strand2 frag1 frag2
  - use the validPairs2FitHiC-fixedSize.sh
    - There are alternative methods for non-fixed size, based on the restriction enzyme used, but this is more straightforwards right now
    - Their script doesn't work for pairix files, indexes wrong, fixed
    - removes all non chr1-22 and XY (removes mito too)
    - Also generates some weird rows (first chromosome is 0, last row's chromosome is called pairs), I just removed these in the output and rezip
  - use the pairs file from ENCODE
- creating the frag file
  - took the metadata from the pairs file on the chr1-22XY from pairs file
  - used createFitHiCFragments-fixedsize.py
- creating the bias file (helps adjust counts and normalizes with KR)
  - use HiCKy.py
  - KR makes the matrix all the same row sum to same number, so normalizes it based on read I guess
  - where it's a pairwise contact amtrix
- ran fithic.py to do the actual computation
  - worked!
  - ran with -x All, which makes it calculate all pairwise comps


### General Notes
- Total runtime for all +x was about 3 hours
  - Some of their code comments looks chatgpt'd?
- 