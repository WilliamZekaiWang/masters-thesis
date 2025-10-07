library(ggplot2)
library(readr)

chrom_starts <- c(
  chr1  = 0,
  chr2  = 248956422,
  chr3  = 491149951,
  chr4  = 689445510,
  chr5  = 879660065,
  chr6  = 1061198324,
  chr7  = 1232004303,
  chr8  = 1391340276,
  chr9  = 1536478912,
  chr10 = 1674873629,
  chr11 = 1808671051,
  chr12 = 1943757673,
  chr13 = 2077032982,
  chr14 = 2191397310,
  chr15 = 2298441028,
  chr16 = 2400432217,
  chr17 = 2490760562,
  chr18 = 2574018003,
  chr19 = 2654391288,
  chr20 = 2713008904,
  chr21 = 2777453071,
  chr22 = 2824163054,
  chrX  = 2874981522,
  chrY  = 3031022417
)

df <- read_delim('test', col_names=TRUE, col_select=c('chr1', 'chr2','p-value', 'q-value'))

df_sig <- df[df$`q-value` < 0.05, ]

cat(sprintf("There are %d significant contacts with FDR < 0.05\n", nrow(df_sig)))

df_inter <- df_sig[df_sig$chr1 != df_sig$chr2, ]

cat(sprintf("There are %d significant contacts with FDR < 0.05 between chromosomes\n", nrow(df_inter)))
