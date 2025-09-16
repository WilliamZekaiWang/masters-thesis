## eQTL Papers

- [x] [Revealing the architecture of gene regulation: the promise of eQTL studies, 2008](https://www.sciencedirect.com/science/article/abs/pii/S0168952508001777?via%3Dihub)
  - Review paper on eQTLs in general. What they are, how they work, limitations and strengths. General information about the difficulties of finding distal eQTLs, and the typical trends seen between cis/trans. 

- [ ] [eQTL studies: from bulk tissues to single cells](https://www.sciencedirect.com/science/article/pii/S1673852723001133)
  - A more up to date reveiw on eQTLs with additions of single cell RNA-seq

- [ ] [The GTEx Consortium atlas of genetic regulatory effects across human tissues](https://www.science.org/doi/full/10.1126/science.aaz1776)
  - Big study trying to annotate the whole genome

### Trans

- [ ] [Systematic identification of trans eQTLs as putative drivers of known disease associations](https://www.nature.com/articles/ng.2756)
  - Large scale study finding trans eQTLs

- [ ] [Large-scale cis- and trans-eQTL analyses identify thousands of genetic loci and polygenic scores that regulate blood gene expression](https://www.nature.com/articles/s41588-021-00913-z)
  - Exmaples of how they found a lot of Trans-eQTLs

### Methods

- [x] [Matrix eQTL: Ultra fast eQTL analysis via large matrix operations](https://www.bios.unc.edu/research/genomic_software/Matrix_eQTL/)
  - R package to work with eQTLs, fast, and doesn't get slowed down with co-variets. Tests each SNP with linear model (Sum least squares) or ANOVA. Presents a genotype across all samples as a row in a matrix. Presents all gene expressions per gene as a row and samples as columns so it can do matrix multiplication.

## 4C

- [ ] [Circular chromosome conformation capture (4C) uncovers extensive networks of epigenetically regulated intra- and interchromosomal interactions](https://www.nature.com/articles/ng1891)
  - Validation and methods of 4C using 3C. Formaldehyde linkage, lyse, restriction enzyme of choice, ligation, PCR regions of interest. Hybridyze to arrays.

- [ ] [Nuclear organization of active and inactive chromatin domains uncovered by chromosome conformation capture–on-chip (4C)](https://www.nature.com/articles/ng1896)
  - 4C methods paper. Namely, details the use of 4C specific microarray. Details the use of restriction enyzmes. Uses first restriction enzyme, ligate ends so you have closely identified points. Then use a secondary RE that cuts more frequently. Ligate ends of secondary cuts into circle. Use third restriction enyzmes that cuts inbetween first two restriction enzyme sites. Use primer based on viewpoint to inverse PCR amplify. Attach probes, and hybridize them for signal in a microarray. Compare with non-crosslinked, and relative signals can be compared

## Hi-C

- [ ] [Hi-C: A comprehensive technique to capture the conformation of genomes](https://www.sciencedirect.com/science/article/abs/pii/S1046202312001168?via%3Dihub)
  - Contains Hi-C methods, describes the methods of the assay as well as the output. Get cells, put them in solution to allow for crosslink. Lyse cells. Use type 2 restriction endonuclease to cut, fill in gaps and mark with biotin. Ligate, further restriction enzyme, isolate with biotin. Sequence using paired end reads. Align reads.

- [ ] [Comprehensive Mapping of Long-Range Interactions Reveals Folding Principles of the Human Genome](https://www.science.org/doi/10.1126/science.1181369)
  - The first Hi-C paper? 
