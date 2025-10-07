### HiChIP-seq paper

#### What to do next
- Expand on the regions they looked at: they limited to 10 MB
  - We could look at greater within chromosome distance, or focus on between chromosome regions
    - The followed the significance denoted by (https://pmc.ncbi.nlm.nih.gov/articles/PMC4347522/), which is just the power of decay between chromosome distance. This doesn't apply to between chromosome
    - https://github.com/ay-lab/fithic does interchromosomal significant calling, but has 32 issues and has not been updated in 3 years. [Pub](https://www.nature.com/articles/s43586-022-00188-6)
- They only looked at 5 cell types, (CD4/8 Tcell, naive Bcell, NK, classical monocytes): we can expand more

#### General Notes
- They used this pipeline: Hi-C pro
  - https://doi.org/10.1186/s13059-015-0831-x
  - Starts at raw paired end sequence reads
  - written in CPP and cython with pretty reasonable parallel computing
  - it has 184 issues on github and has not had a commit in 3 years 
- They don't really use their methods, but use the respective eQTLs found as functional enrichment


### Comments

- genes are mostly polygenic or complex (many genetic and environmental factors)
- when we look var, mostly non - coding
  - realized they are in diff positions, like regulatory regions
  - alter the quantity of protein transcription, doesn't directly alter the protein structure
- GWAS SNPs are in regions we denomte as regulatory
  - we know TF binds there, so maybe the SNP affects TF binding
  - it could also change the way the chormosomes are available
- open chromosome eQTLs found that a lot don't map to eQTLs, so maybe they open the chromosome but the TF just doesn't exist

hypothesis editing
- a proportion of unexplained genetic hereditability
  - can be explained by  
  - there are unexplained AA risk loci 
  - prepare CC methods to filter regions of distant choromsoems
 
