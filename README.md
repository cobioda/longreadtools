# et voilà, nous avons terminé !


<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

![LongReadTools](https://raw.githubusercontent.com/cobioda/longreadtools/master/longreadtools/white_bg_log_hd.png)

## Install

``` sh
pip install git+https://github.com/cobioda/longreadtools.git
```

## How to use

Here we will use the `isomatrix_tools` module to convert our isomatrix
txt files in bulk into `anndata` objects using the
[`multiple_isomatrix_conversion`](https://cobioda.github.io/longreadtools/isomatrix_tools.html#multiple_isomatrix_conversion)
function. Then, we will utilize our specialized
[`concatenate_anndata`](https://cobioda.github.io/longreadtools/isomatrix_tools.html#concatenate_anndata)
function to generate a concatenated `anndata` for downstream analysis.

In this section, we will retrieve a list of isomatrix files for
conversion into Anndata objects. The `isomatrix_tools` module within the
LongReadTools library provides a function
[`multiple_isomatrix_conversion`](https://cobioda.github.io/longreadtools/isomatrix_tools.html#multiple_isomatrix_conversion),
which allows for batch conversion of isomatrix text files into Anndata
objects, a binary format for representing large datasets in the context
of single-cell genomics. This is particularly useful for downstream
analysis and integration with other single-cell analysis tools such as
Scanpy. The conversion process is essential for enabling efficient data
handling and manipulation, as Anndata objects are optimized for
high-performance computing tasks.

``` python
# Importing required libraries
import os
import re

# Defining the directory path
directory = '/data/analysis/data_mcandrew/000-sclr-discovair/'

# Defining the regular expression pattern to match the required files
pattern = re.compile('.*(_BIOP_INT|BIOP_NAS)$')

# Getting a list of all files in the directory
all_files = os.listdir(directory)

# Filtering the list to include only files that match the pattern
matching_files = [os.path.join(directory, f) for f in all_files if pattern.match(f)]

# Printing the list of matching files
print(matching_files)

# Assigning the list of matching files to the variable 'individual_runs'
individual_runs = matching_files

# Adding '_isomatrix.txt' to each file name in the 'individual_runs' list
individual_runs = [f'{run}_isomatrix.txt' for run in individual_runs]

# Creating a list of paths for each isomatrix file in the 'matching_files' list
isomatrix_paths = [os.path.join(run, f'{os.path.basename(run)}_isomatrix.txt') for run in matching_files]
```

    ['/data/analysis/data_mcandrew/000-sclr-discovair/D498_BIOP_INT', '/data/analysis/data_mcandrew/000-sclr-discovair/D492_BIOP_NAS', '/data/analysis/data_mcandrew/000-sclr-discovair/D494_BIOP_INT', '/data/analysis/data_mcandrew/000-sclr-discovair/D500_BIOP_INT', '/data/analysis/data_mcandrew/000-sclr-discovair/D494_BIOP_NAS', '/data/analysis/data_mcandrew/000-sclr-discovair/D496_BIOP_INT', '/data/analysis/data_mcandrew/000-sclr-discovair/D499_BIOP_INT', '/data/analysis/data_mcandrew/000-sclr-discovair/D493_BIOP_INT', '/data/analysis/data_mcandrew/000-sclr-discovair/D493_BIOP_NAS', '/data/analysis/data_mcandrew/000-sclr-discovair/D534_BIOP_INT', '/data/analysis/data_mcandrew/000-sclr-discovair/D490_BIOP_INT', '/data/analysis/data_mcandrew/000-sclr-discovair/D500_BIOP_NAS', '/data/analysis/data_mcandrew/000-sclr-discovair/D495_BIOP_INT', '/data/analysis/data_mcandrew/000-sclr-discovair/D492_BIOP_INT']

In this section, we will leverage the `isomatool` module from the
LongReadTools library to convert the isomatrix files, which we have
previously identified and listed in `isomatrix_paths`, into Anndata
objects. Anndata objects are a binary format designed for large-scale
single-cell genomics data, which facilitates efficient data handling and
manipulation, making them ideal for high-throughput computational
analysis. The
[`multiple_isomatrix_conversion`](https://cobioda.github.io/longreadtools/isomatrix_tools.html#multiple_isomatrix_conversion)
function from `isomatool` will be used to perform this batch conversion,
setting the stage for subsequent data integration and analysis steps,
such as normalization, dimensionality reduction, and cell clustering
using tools like Scanpy.

``` python
from longreadtools.isomatool import *
import scanpy as sc
```

``` python
converted_isomatrix_paths = multiple_isomatrix_conversion(isomatrix_paths, verbose=True, return_paths = True)
```

    File /data/analysis/data_mcandrew/000-sclr-discovair/D498_BIOP_INT/D498_BIOP_INT_isomatrix.h5ad was successfully written to disk.
    File /data/analysis/data_mcandrew/000-sclr-discovair/D500_BIOP_NAS/D500_BIOP_NAS_isomatrix.h5ad was successfully written to disk.
    File /data/analysis/data_mcandrew/000-sclr-discovair/D500_BIOP_INT/D500_BIOP_INT_isomatrix.h5ad was successfully written to disk.
    File /data/analysis/data_mcandrew/000-sclr-discovair/D494_BIOP_NAS/D494_BIOP_NAS_isomatrix.h5ad was successfully written to disk.
    File /data/analysis/data_mcandrew/000-sclr-discovair/D493_BIOP_NAS/D493_BIOP_NAS_isomatrix.h5ad was successfully written to disk.
    File /data/analysis/data_mcandrew/000-sclr-discovair/D493_BIOP_INT/D493_BIOP_INT_isomatrix.h5ad was successfully written to disk.
    File /data/analysis/data_mcandrew/000-sclr-discovair/D499_BIOP_INT/D499_BIOP_INT_isomatrix.h5ad was successfully written to disk.
    File /data/analysis/data_mcandrew/000-sclr-discovair/D494_BIOP_INT/D494_BIOP_INT_isomatrix.h5ad was successfully written to disk.
    File /data/analysis/data_mcandrew/000-sclr-discovair/D495_BIOP_INT/D495_BIOP_INT_isomatrix.h5ad was successfully written to disk.
    File /data/analysis/data_mcandrew/000-sclr-discovair/D490_BIOP_INT/D490_BIOP_INT_isomatrix.h5ad was successfully written to disk.
    File /data/analysis/data_mcandrew/000-sclr-discovair/D492_BIOP_INT/D492_BIOP_INT_isomatrix.h5ad was successfully written to disk.
    File /data/analysis/data_mcandrew/000-sclr-discovair/D496_BIOP_INT/D496_BIOP_INT_isomatrix.h5ad was successfully written to disk.
    File /data/analysis/data_mcandrew/000-sclr-discovair/D534_BIOP_INT/D534_BIOP_INT_isomatrix.h5ad was successfully written to disk.
    File /data/analysis/data_mcandrew/000-sclr-discovair/D492_BIOP_NAS/D492_BIOP_NAS_isomatrix.h5ad was successfully written to disk.

``` python
andata_concat = concatenate_anndata(converted_isomatrix_paths, verbose = True)
```

    Reading .h5ad files...
    Applying feature set standardization...
    Concatenating AnnData objects and adding batch keys with scanpy...
    Setting .var attribute...
    Final Check...
    Concatenation complete.

    Standardizing anndata features via union: 100%|██████████| 14/14 [01:03<00:00,  4.51s/it]
    /home/mcandrew/.conda/envs/scLRanalyis/lib/python3.11/site-packages/anndata/_core/anndata.py:1897: UserWarning: Observation names are not unique. To make them unique, call `.obs_names_make_unique`.
      utils.warn_names_duplicates("obs")
    /home/mcandrew/.conda/envs/scLRanalyis/lib/python3.11/site-packages/pandas/core/arrays/categorical.py:568: RuntimeWarning: invalid value encountered in cast
      np.array(self.categories._na_value).astype(dtype)
    /home/mcandrew/.conda/envs/scLRanalyis/lib/python3.11/site-packages/longreadtools/isomatool.py:342: FutureWarning: is_categorical_dtype is deprecated and will be removed in a future version. Use isinstance(dtype, CategoricalDtype) instead
      if pd.api.types.is_categorical_dtype(df[col]):
    /home/mcandrew/.conda/envs/scLRanalyis/lib/python3.11/site-packages/longreadtools/isomatool.py:342: FutureWarning: is_categorical_dtype is deprecated and will be removed in a future version. Use isinstance(dtype, CategoricalDtype) instead
      if pd.api.types.is_categorical_dtype(df[col]):
    /home/mcandrew/.conda/envs/scLRanalyis/lib/python3.11/site-packages/longreadtools/isomatool.py:342: FutureWarning: is_categorical_dtype is deprecated and will be removed in a future version. Use isinstance(dtype, CategoricalDtype) instead
      if pd.api.types.is_categorical_dtype(df[col]):
    /home/mcandrew/.conda/envs/scLRanalyis/lib/python3.11/site-packages/longreadtools/isomatool.py:342: FutureWarning: is_categorical_dtype is deprecated and will be removed in a future version. Use isinstance(dtype, CategoricalDtype) instead
      if pd.api.types.is_categorical_dtype(df[col]):

Now that we have concatenated the Anndata objects, let’s examine the
resulting object to ensure it’s structured correctly and ready for
downstream analysis. We will display the shape of the matrix, the
metadata associated with observations (cells), and the variables (genes)
to get an overview of the dataset. Additionally, we will check for any
potential issues such as non-unique observation names, which we’ve been
warned about in the output from cell 20.

``` python
# Display the shape of the concatenated Anndata object
print(f"The Anndata object has {andata_concat.n_obs} observations (cells) and {andata_concat.n_vars} variables (genes).")

# Display the first few entries of the observation metadata to inspect batch information and other annotations
print("Observation metadata (first 5 entries):")
print(andata_concat.obs.head())

# Display the first few entries of the variable metadata to inspect gene and transcript information
print("Variable metadata (first 5 entries):")
print(andata_concat.var.head())

# Check for unique observation names and make them unique if necessary
if not andata_concat.obs_names.is_unique:
    andata_concat.obs_names_make_unique()
    print("Observation names were not unique; they have been made unique.")
```

    The Anndata object has 122872 observations (cells) and 89177 variables (genes).
    Observation metadata (first 5 entries):
                              batch
    AGGAAATGTACAAGCG  D498_BIOP_INT
    GCCATTCGTCGGAACA  D498_BIOP_INT
    TCGACCTCAGTGTGCC  D498_BIOP_INT
    CGTAGTATCAGTGTGT  D498_BIOP_INT
    GCCAGGTGTCTAACTG  D498_BIOP_INT
    Variable metadata (first 5 entries):
                           geneId     transcriptId nbExons
    transcriptId                                          
    ENST00000548501       CYP4F12  ENST00000548501       4
    ENST00000324229         CALCB  ENST00000324229       5
    ENST00000371489          MYOF  ENST00000371489      15
    ENST00000368659       SLC27A3  ENST00000368659       2
    ENST00000669353  TMEM161B-AS1  ENST00000669353       4
    Observation names were not unique; they have been made unique.

``` python
andata_concat.X
```

    array([[0., 0., 0., ..., 0., 0., 0.],
           [1., 0., 0., ..., 0., 0., 0.],
           [1., 1., 2., ..., 0., 0., 0.],
           ...,
           [0., 0., 0., ..., 0., 0., 0.],
           [0., 0., 0., ..., 0., 0., 0.],
           [0., 0., 0., ..., 0., 0., 0.]], dtype=float32)

``` python
andata_concat.var
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
&#10;    .dataframe tbody tr th {
        vertical-align: top;
    }
&#10;    .dataframe thead th {
        text-align: right;
    }
</style>

|                 | geneId       | transcriptId    | nbExons |
|-----------------|--------------|-----------------|---------|
| transcriptId    |              |                 |         |
| ENST00000548501 | CYP4F12      | ENST00000548501 | 4       |
| ENST00000324229 | CALCB        | ENST00000324229 | 5       |
| ENST00000371489 | MYOF         | ENST00000371489 | 15      |
| ENST00000368659 | SLC27A3      | ENST00000368659 | 2       |
| ENST00000669353 | TMEM161B-AS1 | ENST00000669353 | 4       |
| ...             | ...          | ...             | ...     |
| ENST00000535337 | AC156455.1   | ENST00000535337 | 2       |
| ENST00000393825 | NDUFA4L2     | ENST00000393825 | 5       |
| ENST00000508491 | UTP15        | ENST00000508491 | 13      |
| ENST00000394566 | SLFN11       | ENST00000394566 | 7       |
| ENST00000642078 | MFSD8        | ENST00000642078 | 10      |

<p>89177 rows × 3 columns</p>
</div>

``` python
andata_concat.obs
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
&#10;    .dataframe tbody tr th {
        vertical-align: top;
    }
&#10;    .dataframe thead th {
        text-align: right;
    }
</style>

|                  | batch         |
|------------------|---------------|
| AGGAAATGTACAAGCG | D498_BIOP_INT |
| GCCATTCGTCGGAACA | D498_BIOP_INT |
| TCGACCTCAGTGTGCC | D498_BIOP_INT |
| CGTAGTATCAGTGTGT | D498_BIOP_INT |
| GCCAGGTGTCTAACTG | D498_BIOP_INT |
| ...              | ...           |
| AGTGACTTCTAAGCCA | D492_BIOP_INT |
| CATTGTTCATCACCAA | D492_BIOP_INT |
| GATGATCCACACAGAG | D492_BIOP_INT |
| TCGAACATCAGTGCGC | D492_BIOP_INT |
| GTTGCGGCACCTGCTT | D492_BIOP_INT |

<p>122872 rows × 1 columns</p>
</div>

Utilizing Scanpy, this function call will serialize the `andata_concat`
object to an HDF5 file, a format widely adopted for storing extensive
scientific data. The chosen filename
‘discovair_long_read_transcript_matrix.h5ad’ clearly reflects the file’s
contents, representing the transcript matrix obtained from long-read
sequencing data. The HDF5 format is particularly advantageous for
Anndata objects as it facilitates the efficient storage and retrieval of
large, intricate datasets, which is quintessential for managing the
high-dimensional data produced by single-cell sequencing technologies.

``` python
andata_concat.write_h5ad('discovair_long_read_transcript_matrix.h5ad')
```

In this step, we are utilizing the `sc.read_h5ad` function to load the
Anndata objects that contain the transcriptomic data from both long-read
and short-read sequencing technologies. The long-read data, which
typically provides full-length transcripts allowing for the
identification of isoform diversity, is stored in
“discovair_long_read_transcript_matrix.h5ad”. The short-read data, known
for its higher throughput and quantification accuracy at the gene level,
is stored in
“/data/analysis/data_mcandrew/000-sclr-discovair/integrated_V10.h5ad”.
These datasets will be used for subsequent comparative analysis and
integration, leveraging the capabilities of the longreadtools library to
handle and process long-read sequencing data efficiently.

``` python
isoform_anndata_from_long_reads = sc.read_h5ad("discovair_long_read_transcript_matrix.h5ad")
gene_anndata_from_short_reads = sc.read_h5ad("/data/analysis/data_mcandrew/000-sclr-discovair/integrated_V10.h5ad")
```

lets take a look at both

``` python
isoform_anndata_from_long_reads
```

    AnnData object with n_obs × n_vars = 122872 × 89177
        obs: 'batch'
        var: 'geneId', 'transcriptId', 'nbExons'

``` python
gene_anndata_from_short_reads
```

    AnnData object with n_obs × n_vars = 414609 × 36602
        obs: 'manip', 'donor', 'method', 'position', 'n_genes_by_counts', 'total_counts', 'total_counts_mt', 'pct_counts_mt', 'total_counts_ribo', 'pct_counts_ribo', 'louvain', 'n_genes', 'nCount_SCT', 'nFeature_SCT', 'batch', 'age', 'gender', 'phenotype', 'respifinder', 'TRACvsNAS', 'sixty_plus', 'smoker', 'smoking_years', 'leiden', 'leiden_Endothelial', 'leiden_Stromal', 'leiden_Immune', 'leiden_Epithelial', 'log1p_n_genes_by_counts', 'log1p_total_counts', 'pct_counts_in_top_50_genes', 'pct_counts_in_top_100_genes', 'pct_counts_in_top_200_genes', 'pct_counts_in_top_500_genes', 'celltype_lv2_V4', 'celltype_lv0_V4', 'celltype_lv1_V4', 'celltype_lv2_V5', 'celltype_lv0_V5', 'celltype_lv1_V5', 'leiden_scANVI', 'disease_score', 'smoker_phenotype', 'leiden_scANVI_hvg_10000', 'leiden_scANVI_nl_50', 'leiden_scANVI_hvg_10000_nl_50', 'celltype_lv3_V5'
        var: 'n_cells_by_counts', 'mean_counts', 'log1p_mean_counts', 'pct_dropout_by_counts', 'total_counts', 'log1p_total_counts', 'mt', 'ribo'
        uns: 'Adventitial Fibroblast_colors', 'DE_ct_lv2', 'DE_ct_lv3', 'celltype_lv0_V4_colors', 'celltype_lv0_V5_colors', 'celltype_lv1_V4_colors', 'celltype_lv1_V5_colors', 'celltype_lv2_V4_colors', 'celltype_lv2_V5_colors', 'celltype_lv3_V5_colors', 'donor_colors', 'leiden', 'neighbors', 'neighbors_scanvi', 'pca', 'phenotype_colors', 'position_colors', 'rank_genes_groups_leiden', 'umap'
        obsm: 'X_pca', 'X_scANVI', 'X_scANVI_hvg_10000', 'X_scANVI_hvg_10000_nl_50', 'X_scANVI_nl_50', 'X_umap', 'dorothea_mlm_estimate', 'dorothea_mlm_pvals', 'mlm_estimate', 'mlm_pvals'
        varm: 'PCs', 'gini_celltype', 'n_cells_celltype_lv2_V3'
        obsp: 'connectivities', 'distances', 'neighbors_scanvi_connectivities', 'neighbors_scanvi_distances'

``` python
gene_anndata_from_short_reads.obs
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
&#10;    .dataframe tbody tr th {
        vertical-align: top;
    }
&#10;    .dataframe thead th {
        text-align: right;
    }
</style>

|                                  | manip          | donor | method | position | n_genes_by_counts | total_counts | total_counts_mt | pct_counts_mt | total_counts_ribo | pct_counts_ribo | ... | celltype_lv2_V5 | celltype_lv0_V5 | celltype_lv1_V5 | leiden_scANVI | disease_score | smoker_phenotype | leiden_scANVI_hvg_10000 | leiden_scANVI_nl_50 | leiden_scANVI_hvg_10000_nl_50 | celltype_lv3_V5 |
|----------------------------------|----------------|-------|--------|----------|-------------------|--------------|-----------------|---------------|-------------------|-----------------|-----|-----------------|-----------------|-----------------|---------------|---------------|------------------|-------------------------|---------------------|-------------------------------|-----------------|
| D460_BIOP_PRO1GGCTTGGAGCGCCTCA-1 | D460_BIOP_PRO1 | D460  | BIOP   | PRO      | 2150              | 5919.0       | 283.0           | 4.782021      | 1510.0            | 25.515377       | ... | Veinous         | Endothelial     | Endothelial     | 11            | GAP Stage 1   | non-smoker_IPF   | 9                       | 9                   | 8                             | Veinous         |
| D463_BIOP_NAS1TCACTCGCATTGGGAG-1 | D463_BIOP_NAS1 | D463  | BIOP   | NAS      | 1927              | 4979.0       | 474.0           | 9.519984      | 1357.0            | 27.254469       | ... | Veinous         | Endothelial     | Endothelial     | 11            | GAP Stage 1   | non-smoker_IPF   | 9                       | 9                   | 8                             | Veinous         |
| D534_BIOP_PROAATCGACAGCAAGTCG-1  | D534_BIOP_PRO  | D534  | BIOP   | PRO      | 1264              | 3013.0       | 311.0           | 10.321939     | 779.0             | 25.854630       | ... | Capillary       | Endothelial     | Endothelial     | 11            | Healthy       | non-smoker_CTRL  | 9                       | 9                   | 8                             | Capillary       |
| D463_BIOP_NAS1TCGCTTGTCACTTGGA-1 | D463_BIOP_NAS1 | D463  | BIOP   | NAS      | 3691              | 11794.0      | 1314.0          | 11.141258     | 2867.0            | 24.308971       | ... | Veinous         | Endothelial     | Endothelial     | 11            | GAP Stage 1   | non-smoker_IPF   | 9                       | 9                   | 8                             | Veinous         |
| D489_BIOP_PROAGGGAGTTCGGTCTGG-1  | D489_BIOP_PRO  | D489  | BIOP   | PRO      | 738               | 1096.0       | 57.0            | 5.200730      | 127.0             | 11.587591       | ... | Capillary       | Endothelial     | Endothelial     | 11            | GOLD 1        | non-smoker_BPCO  | 9                       | 9                   | 8                             | Capillary       |
| ...                              | ...            | ...   | ...    | ...      | ...               | ...          | ...             | ...           | ...               | ...             | ... | ...             | ...             | ...             | ...           | ...           | ...              | ...                     | ...                 | ...                           | ...             |
| D460_BRUS_NAS1TCTATACCAATGGGTG-1 | D460_BRUS_NAS1 | D460  | BRUS   | NAS      | 1500              | 4263.0       | 447.0           | 10.485574     | 1342.0            | 31.480179       | ... | Suprabasal      | Epithelial      | Suprabasal      | 0             | GAP Stage 1   | non-smoker_IPF   | 2                       | 1                   | 1                             | Suprabasal      |
| D460_BRUS_NAS1GTTATGGCAATGGCAG-1 | D460_BRUS_NAS1 | D460  | BRUS   | NAS      | 2422              | 6089.0       | 774.0           | 12.711448     | 740.0             | 12.153063       | ... | Ionocyte        | Epithelial      | Ionocyte        | 24            | GAP Stage 1   | non-smoker_IPF   | 29                      | 27                  | 27                            | Ionocyte        |
| D460_BRUS_NAS1ATGAGTCAGCCGTTGC-1 | D460_BRUS_NAS1 | D460  | BRUS   | NAS      | 2784              | 11638.0      | 1460.0          | 12.545111     | 2642.0            | 22.701494       | ... | Goblet          | Epithelial      | Goblet          | 5             | GAP Stage 1   | non-smoker_IPF   | 13                      | 5                   | 4                             | Goblet          |
| D460_BRUS_NAS1TCATACTAGCAGTAAT-1 | D460_BRUS_NAS1 | D460  | BRUS   | NAS      | 2563              | 8025.0       | 919.0           | 11.451714     | 1619.0            | 20.174454       | ... | Goblet          | Epithelial      | Goblet          | 5             | GAP Stage 1   | non-smoker_IPF   | 13                      | 5                   | 4                             | Goblet          |
| D460_BRUS_NAS1TTGTTGTCAAGATGTA-1 | D460_BRUS_NAS1 | D460  | BRUS   | NAS      | 1380              | 3443.0       | 255.0           | 7.406332      | 724.0             | 21.028173       | ... | Goblet          | Epithelial      | Goblet          | 5             | GAP Stage 1   | non-smoker_IPF   | 13                      | 5                   | 4                             | Goblet          |

<p>414609 rows × 47 columns</p>
</div>

To ensure a coherent and integrated analysis of the transcriptomic data
derived from both long-read and short-read sequencing technologies, it
is imperative to harmonize the indexes of the corresponding Anndata
objects. This step is crucial as it aligns the observations (cells)
across the datasets, enabling a direct comparison and subsequent
operations such as data integration, differential expression analysis,
and visualization. The process of index matching is facilitated by the
[`subset_common_cells`](https://cobioda.github.io/longreadtools/harmonisation_tools.html#subset_common_cells)
function from the longreadtools library, which is designed to identify
and retain only those cells that are present in both datasets. This
function is exemplified in the codeblock below, where it is employed to
refine our datasets to a common set of cells, thereby setting the stage
for a robust comparative analysis that leverages the unique strengths of
each sequencing technology within the longreadtools framework.

``` python
isoform_anndata_from_long_reads.obs['batch'] = isoform_anndata_from_long_reads.obs['batch'].astype(str)
isoform_anndata_from_long_reads.obs_names = isoform_anndata_from_long_reads.obs['batch'] + isoform_anndata_from_long_reads.obs_names + "-1"
```

    /home/mcandrew/.conda/envs/scLRanalyis/lib/python3.11/site-packages/pandas/core/arrays/categorical.py:568: RuntimeWarning: invalid value encountered in cast
      np.array(self.categories._na_value).astype(dtype)

After the standardization of the Anndata objects’ indexes, we can
confirm that the indexes are now aligned and ready for comparative
analysis. This alignment is crucial for the integration of the long-read
and short-read transcriptomic data, as it ensures that the same cells
are represented in both datasets. The function
[`subset_common_cells`](https://cobioda.github.io/longreadtools/harmonisation_tools.html#subset_common_cells)
from the longreadtools library, which is highlighted in the codeblock
below, plays a pivotal role in this process. By subsetting the Anndata
objects to include only the common cells, we facilitate a more accurate
and meaningful comparison between the datasets.

``` python
isoform_anndata_from_long_reads.obs_names
```

    Index(['D498_BIOP_INTAGGAAATGTACAAGCG-1', 'D498_BIOP_INTGCCATTCGTCGGAACA-1',
           'D498_BIOP_INTTCGACCTCAGTGTGCC-1', 'D498_BIOP_INTCGTAGTATCAGTGTGT-1',
           'D498_BIOP_INTGCCAGGTGTCTAACTG-1', 'D498_BIOP_INTTGTGTGAGTGTTGACT-1',
           'D498_BIOP_INTCAGATACTCCAACTGA-1', 'D498_BIOP_INTGCCGATGTCTCATTAC-1',
           'D498_BIOP_INTGGAGAACTCTCGAGTA-1', 'D498_BIOP_INTAAGCATCTCGTGGTAT-1',
           ...
           'D492_BIOP_INTAAAGTGAAGGTTACAA-1', 'D492_BIOP_INTTACGGGCGTGAGACCA-1',
           'D492_BIOP_INTACAGGGAGTCAACATC-1', 'D492_BIOP_INTTTTCGATCAGGCCTGT-1',
           'D492_BIOP_INTAACAACCTCATCAGTG-1', 'D492_BIOP_INTAGTGACTTCTAAGCCA-1',
           'D492_BIOP_INTCATTGTTCATCACCAA-1', 'D492_BIOP_INTGATGATCCACACAGAG-1',
           'D492_BIOP_INTTCGAACATCAGTGCGC-1', 'D492_BIOP_INTGTTGCGGCACCTGCTT-1'],
          dtype='object', length=122872)

In this section, we are going to utilize the
[`subset_common_cells`](https://cobioda.github.io/longreadtools/harmonisation_tools.html#subset_common_cells)
function from the longreadtools library to harmonize our datasets. This
function is crucial for ensuring that we are comparing the same cells
across the two Anndata objects - one derived from long-read sequencing
and the other from short-read sequencing. By importing and applying this
function, we can identify the intersection of cells present in both
datasets, allowing for a consistent and integrated analysis. This step
is foundational for the subsequent comparative analysis and integration
tasks that leverage the unique advantages of each sequencing technology
within the longreadtools framework.

``` python
from longreadtools.Standardization import *
isoform_matrix = subset_common_cells(isoform_anndata_from_long_reads, gene_anndata_from_short_reads)
```

In the previous steps, we have successfully standardized the indexes of
our Anndata objects and utilized the
[`subset_common_cells`](https://cobioda.github.io/longreadtools/harmonisation_tools.html#subset_common_cells)
function to refine the isoform Anndata object derived from long-read
sequencing data. The next logical step is to apply the same subsetting
process to the gene Anndata object from short-read sequencing data. This
ensures that both datasets are synchronized and contain only the cells
common to both, which is a prerequisite for accurate annotation
transfer. The annotations, which include vital metadata such as cell
type, condition, and experimental batch information, are crucial for
downstream analysis and interpretation of the integrated dataset. The
codeblock below demonstrates the use of the
[`subset_common_cells`](https://cobioda.github.io/longreadtools/harmonisation_tools.html#subset_common_cells)
function for this purpose, setting the stage for a seamless transfer of
annotations from the short-read to the long-read dataset within the
longreadtools framework.

``` python
gene_matrtrix  = subset_common_cells(gene_anndata_from_short_reads, isoform_matrix)
```

The next step in our analysis pipeline is to transfer the observation
annotations from the `gene_matrix` Anndata object, which contains the
short-read sequencing data, to the `isoform_matrix` Anndata object,
which contains the long-read sequencing data. This is a critical step as
it ensures that the metadata, which includes information such as cell
type, condition, and experimental batch, is consistently annotated
across both datasets. The
[`transfer_obs`](https://cobioda.github.io/longreadtools/harmonisation_tools.html#transfer_obs)
function from the longreadtools library is instrumental in this process.
It meticulously maps the `.obs` attributes from one Anndata object to
another based on the shared cell identifiers, thus preserving the
integrity of the data and enabling a seamless integration. The codeblock
below demonstrates the application of this function, which is a
testament to the library’s capability to facilitate complex operations
in transcriptomic data analysis within a unified framework.

``` python
annotated_isoform_matrix = transfer_obs(gene_matrtrix, isoform_matrix)
```

In this step, we delve into the annotated isoform matrix, which is a
product of the meticulous standardization and subsetting processes we
have applied to our Anndata objects. The `annotated_isoform_matrix` is a
rich dataset that combines the detailed isoform data obtained from
long-read sequencing with the comprehensive annotations transferred from
the gene matrix derived from short-read sequencing. This matrix is a
testament to the capabilities of the `longreadtools` library,
particularly showcasing the
[`transfer_obs`](https://cobioda.github.io/longreadtools/harmonisation_tools.html#transfer_obs)
function, which we have utilized to enrich our isoform data with
valuable metadata from the gene matrix. By examining this matrix, we
gain insights into the transcriptomic landscape at an isoform
resolution, which is crucial for understanding the complexity of gene
expression patterns. The annotations included in this matrix, such as
cell type, donor information, and technical attributes, are pivotal for
subsequent analyses that aim to unravel the biological and clinical
significance of the data within the context of the longreadtools
framework.

``` python
annotated_isoform_matrix
```

    AnnData object with n_obs × n_vars = 62725 × 89177
        obs: 'manip', 'donor', 'method', 'position', 'n_genes_by_counts', 'total_counts', 'total_counts_mt', 'pct_counts_mt', 'total_counts_ribo', 'pct_counts_ribo', 'louvain', 'n_genes', 'nCount_SCT', 'nFeature_SCT', 'batch', 'age', 'gender', 'phenotype', 'respifinder', 'TRACvsNAS', 'sixty_plus', 'smoker', 'smoking_years', 'leiden', 'leiden_Endothelial', 'leiden_Stromal', 'leiden_Immune', 'leiden_Epithelial', 'log1p_n_genes_by_counts', 'log1p_total_counts', 'pct_counts_in_top_50_genes', 'pct_counts_in_top_100_genes', 'pct_counts_in_top_200_genes', 'pct_counts_in_top_500_genes', 'celltype_lv2_V4', 'celltype_lv0_V4', 'celltype_lv1_V4', 'celltype_lv2_V5', 'celltype_lv0_V5', 'celltype_lv1_V5', 'leiden_scANVI', 'disease_score', 'smoker_phenotype', 'leiden_scANVI_hvg_10000', 'leiden_scANVI_nl_50', 'leiden_scANVI_hvg_10000_nl_50', 'celltype_lv3_V5'
        var: 'geneId', 'transcriptId', 'nbExons'
