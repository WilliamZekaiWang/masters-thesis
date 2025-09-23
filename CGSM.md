## Outline

### Background within the context of current knowledge in the field
* There are diseases that propigate within a family line, insinuating that there is a genetic basis to the disease
  * More likely to find a disease with a related individual as compared to another random person
* If you genotype individuals with and without a disease, you can find the single nuleotide polymorphisms associated with each group
  * GWAS shows associations between genetic variation and disease
    * > [Uffelmann et al., 2021](https://www.nature.com/articles/s41588-020-0625-2): Nature primer GWAS
  * Already, we have done GWAS for a bunch of diseases, but their exact mechanisms of action are still not known
    * > [IMSCC, 2019](https://www.science.org/doi/10.1126/science.aav7188): GWAS for MS
    * > [Cooper et al., 2008](https://www.nature.com/articles/ng.249): GWAS for T1 diabeties
    * > [Grixti et al., 2024](https://doi.org/10.1007/s11154-023-09848-8): GWAS for graves disease
* We usually don't know mechansism of these SNPs
  * Some diseases with a genetic basis can be linked to a singluar inheritable source
    * > [Rommens et al., 1989](https://www.science.org/doi/10.1126/science.2772657): Cystic fibrosis, delta f508
  * Other diseases aren't expliclit with how a mutation causes diseases (i.e. not a single causal mutation)
    * > [Rheenen et al., 2019](https://www.nature.com/articles/s41576-019-0137-z): review article about genetic correlations and disease with an empahsis on GWAS
  * They are typically in gene regulatory regions or regions of open chromatin, which means they likely regulate gene expression 
    * > [Maurano et al., 2012](https://www.science.org/doi/10.1126/science.1222794): GWAS SNPs concentrated in regulatory DNA
* eQTL analysis can find if a SNP change leads to a transcriptional change from normal levels, potentially leading to disease
  * These transcriptional changes can provide insight into disease etiology and subsequently, therapeutic opportunities
  * There are two types of eQTLs, cis- and trans-
    * > [Gilad et al., 2008](https://www.sciencedirect.com/science/article/pii/S0168952508001777): eQTL review, details what potential use they have and the benefits of them, as well as what cis and trans eQTLs are
* Most previous research forcused on cis, as it is easier to detect them with a smaller sample size, however, they only explain 11 ± 2% of h2g
  * > [GTEx consortum, 2020](https://www.science.org/doi/full/10.1126/science.aaz1776): large study looking at many different tissue types and mapped a bunch of eQTLs. Most of focus was on cis, noted difficulties of finding trans-eQTLs
  * > [Yao et al., 2020](https://www.nature.com/articles/s41588-020-0625-2): heretibility statement. Also noted that trans, cell specific, chromosome conformation can help explain more
  * Trans-eQTLs, underpowered, cell types, and context (environment), may help explain the rest
    * > [GTEx consortum, 2020](https://www.science.org/doi/full/10.1126/science.aaz1776): noted that most of their significant cis-eQTLs had a >0.9 spearman correlation with number of cells (power)
    * > [Zhand & Zhao, 2023](https://www.sciencedirect.com/science/article/pii/S1673852723001133?via%3Dihub): review article that shows the change from bulkRNA to single cell RNA in eQTL 
    * > [Zhernakova et al., 2016](https://www.nature.com/articles/ng.3737): 12% of people from PBMC eQTL analysis showed context specific effects
* Given the focus on cis-eQTLs, and the importance of finding them, there is an unmet need of both finding methods and searching for trans-eQTLs
  * Trans-eQTLs present with two main issues, smaller effect size and difficult to account for multiple test correction (assuming you're testing every point of the genome to a gene of interest)
    * > [Zhang & Zhao, 2023](https://www.sciencedirect.com/science/article/pii/S1673852723001133?via%3Dihub): states most papers focus on cis-eQTLs due to smaller effect size of trans, and the respective power issue
  * Finding new methods can increase the yield of GWASes, and thus, increase the effecitively of a widely used methodology
* Chromosome conforation assays can show how chromosomes interact
  * > [Liberman-Aiden et al., 2010](https://linkinghub.elsevier.com/retrieve/pii/S1673852723001133): Hi-C
  * > [Simonis et al., 2006](https://www.nature.com/articles/ng1896): 4C
  * Generates a heatmap of interactivity (or histogram), from digesting digesting, and ligating cross linked chromosome from formaldehyde treatment
  * Gives guidance to streamline where to search, easing multiple test correction

### Objectives and Hypothesis

**Hypothesis**: We hypothesize that chromosome conformation assays can help reveal novel trans-eQTLs by limiting multiple testing to SNPs within regions that physically interact with genes of interest.

1. Use data from chromosome conformation assays, Hi-C and 4C, to determine which parts of the genomes are worth testing by finding appropriate thresholds
   1. Determine which regions are of interest through identifying automimmune releated genes 
2. Incorporate data from GWAS and scRNA-seqs to find trans-eQTLs in autoimmune diseases
   1. Compare to baseline of running traditional trans-eQTL analysis
3. Determine replicatability of data

### Methods and procedures used

1. Download data from ENCODE, GEO, or related databases relating to both Hi-C/4C data relating to autoimmune cells of interest
   1. Develop a list of regions/genes of interest for autoimmune diseases,
   2. Find a way to isolate Hi-C regions of interest that relate to genes of choice
2. Download the GWAS/scRNA-seq data for patients of varying autoimmune disease
3. Harmonize the datasets from the various studies
4. Develop R scripts to run eQTL analysis using informed information from Hi-C/4C data through matrix-eQTL
   * > [Shabalin, 2012](https://academic.oup.com/bioinformatics/article/28/10/1353/213326): matrix eQTL paper
   1. What threshold is necessary to deem it a significant interaction worthy of interaction?
   2. How many SNPs within the region of interest do we test it for?
   3. What type of multiple test correction?
5. Retest for replicability on subset of data (not tested previously)

### Significance of proposed research in life sciences

* Can better the analytic potential of GWASes without increasing sample size/retesting, effectively improving cost efficiency
* Discover new pathogenic pathways for genetic diseases, increasing the therapeutic potential of the disease