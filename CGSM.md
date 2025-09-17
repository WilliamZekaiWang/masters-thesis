## Outline

### Background within the context of current knowledge in the field
* Humans vary in their genetics, and singular changes in the nucleotide sequence are denoted as SNPs
* GWAS shows associations between genetic variation and disease
  * Typically screens for thousands of 
* We don't know mechansism of these SNPs 
   * They are typically in gene regulatory regions or regions of open chromatin, which means they likely regulate gene expression
* eQTL analysis can statisically find if a SNP change leads to a transcriptional change
  * There are two types of eQTLs, cis- (typically within 1mB from transcription start site) and trans- (longer)
  * These transcriptional changes can provide insight into disease etiology and subsequently, therapeutic opportunities
* Most previous research forcused on cis, which accounts for 1/3-1/2 of the GWAS results
  * Trans-eQTLs, underpowered, cell types, and context (environment), may help explain the rest
  * > Where is the paper for this ratio?
* Given the focus on cis-eQTLs, and the given importance of finding them, there is an unmet need of both finding methods and searching for trans-eQTLs
  * Trans-eQTLs present with two main issues, smaller effect size and difficult to account for multiple test correction (assuming you're testing every point of the genome to a gene of interest)
  * Finding new methods can increase the yield of GWASes, and thus, increase the effecitively of a widely used methodology
* Chromosome conforation assays can show how chromosomes interact
  * Gives guidance to streamline where to search, easing multiple test correction

### Objectives and Hypothesis

**Hypothesis**: We hypothesize we can find trans-eQTLs through bypassing the multiple testing issue of pairwise comparisions from every point of the genome by using targeted regions from chromosome conformation assays.

1. Use data from chromosome conformation assays, Hi-C and 4C, to determine which parts of the genomes are worth testing by finding appropriate thresholds
2. Incorporate data into GWAS and RNA-seqs to find trans-eQTLs in autoimmune diseases

### Methods and procedures used

1. Download data from ENCODE, GEO, or related databases relating to both Hi-C/4C data relating to autoimmune cells of interest
   1. Find a way to isolate Hi-C regions of interest that relate to genes of choice
2. Download the eQTL data for patients of varying autoimmune disease
3. Harmonize the datasets from the various studies and ensure that they can work together
4. Develop R scripts to incorporate data into GWAS/RNA-seq data
   1. What threshold is necessary to deem it a significant interaction worthy of interaction?
   2. How many SNPs within the region of interest do we test it for?
   3. What type of multiple test correction?

### Significance of proposed research in life sciences

This will literally change the world.