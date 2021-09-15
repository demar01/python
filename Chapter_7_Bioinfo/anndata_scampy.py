import numpy as np
import pandas as pd
import anndata as ad
print(ad.__version__)


# Let us generate some example data:

# number of observations
n_obs = 1000
# say we measure the time of observing the data points
# add them to a dataframe for storing some annotation
obs = pd.DataFrame()
obs['time'] = np.random.choice(['day 1', 'day 2', 'day 4', 'day 8'], n_obs)
# set the names of variables/features to the following
# ['A', 'B', 'C', ..., 'AA', 'BB', 'CC', ..., 'AAA', ...]
from string import ascii_uppercase
var_names = [i*letter for i in range(1, 10) for letter in ascii_uppercase]
# number of variables
n_vars = len(var_names)
# dataframe for annotating the variables
var = pd.DataFrame(index=var_names)
# the data matrix of shape n_obs x n_vars
X = np.arange(n_obs*n_vars).reshape(n_obs, n_vars)


#and init an AnnData object.

# we're using an integer data type just for prettier outputs
# the default 'float32' is flexible and precise enough for most purposes
adata = ad.AnnData(X, obs=obs, var=var, dtype='int32')
#convention is that observations/samples of variables/features are stored in the rows of a data matrix X

#The names of observations and of variables are as follows.
print(adata.obs_names[:10].tolist())
print(adata.obs_names[-10:].tolist())
print(adata.var_names[:10].tolist())
print(adata.var_names[-10:].tolist())
print(adata.X)


#Indexing and Views
print(adata[:, 'A'])
print(adata[adata.obs['time'].isin(['day 1', 'day 2'])].obs.head())


#Writing the results to disk 
#adata.write('./write/my_results.h5ad')



######
###https://colab.research.google.com/github/pachterlab/kallistobustools/blob/master/docs/tutorials/kb_aggregate/python/kb_aggregating_count_matrices.ipynb#scrollTo=v0LMbyEs1U-9

sample1 = ad.read_h5ad('/Users/mariadermit/Downloads/mouse_subset_anndata.h5ad')
# key difference is that AnnData matrices are transposed compared to those used by R packages, the rows represent cells and the columns represent features

sample1.X
#spare matrix 
type(sample1.X)
#scipy.sparse.csc.csc_matrix

sample1.obs.head()
#annotation of observation (similar to metadata)
type(sample1.obs)
#pandas.core.frame.DataFrame

sample1.var.head()
#annotation of variables (similar to metadata)

# Concatenate the anndatas
concat_samples = sample1.concatenate(
    sample2, join='outer', batch_categories=['sample1', 'sample2'], index_unique='-'
)

# genes that yield the highest fraction of counts in each single cell, across all cells.
sc.pl.highest_expr_genes(sample1, n_top=20, )


#PREPROCESSING
#basic filtering
sc.pp.filter_cells(sample1, min_genes=200)
sc.pp.filter_genes(sample1, min_cells=3)

#With pp.calculate_qc_metrics, we can compute many metrics very efficiently.
sample1.var['mt'] = sample1.var_names.str.startswith('MT-')  # annotate the group of mitochondrial genes as 'mt'
sc.pp.calculate_qc_metrics(sample1, qc_vars=['mt'], percent_top=None, log1p=False, inplace=True)

#Violin plot for some quality measurements
#awesomely does a plot with grif for the columns selected. In this case a plot with 3 grids.
sc.pl.violin(sample1, ['n_genes_by_counts', 'total_counts', 'pct_counts_mt'],
             jitter=0.4, multi_panel=True)

#awesomely does a scatter plot  
sc.pl.scatter(sample1, x='total_counts', y='pct_counts_mt')
sc.pl.scatter(sample1, x='total_counts', y='n_genes_by_counts')

#Filtering by slicing
sample1 = sample1[sample1.obs.n_genes_by_counts < 2500, :]
sample1 = sample1[sample1.obs.pct_counts_mt < 5, :]

#Normalize it and log it
sc.pp.normalize_total(sample1, target_sum=1e4)
#log1p because there is a lot of 0
sc.pp.log1p(sample1)

#we can freeze the state of anndata sample 1
#sample1.raw=sample1
#and then to recover the raw andata to a anndata 
#sample1.raw.toa_adata()



#Identify high variable genes
sc.pp.highly_variable_genes(sample1, min_mean=0.0125, max_mean=3, min_disp=0.5)

#Regress out
#see https://github.com/theislab/scanpy/issues/526
sc.pp.regress_out(sample1, ['total_counts', 'pct_counts_mt'])


#Scale each gene to unit variance. 
# This is going to normalized the columns (genes). so that the PCA is not highly biased to genes that are highly expressed.
# Clip values exceeding standard deviation 10.
sc.pp.scale(sample1, max_value=10)

#Computing and embedding the neighborhood graph
sc.pp.neighbors(sample1, n_neighbors=10, n_pcs=40)

tl.paga(sample1)
pl.paga(sample1, plot=False)  # remove `plot=False` if you want to see the coarse-grained graph
tl.umap(sample1, init_pos='paga')

#Clustering the neighborhood graph
sc.pl.umap(adata, color=['leiden', 'CST3', 'NKG7'])



### Trayectory inference
adata = sc.datasets.paul15()
adata.X = adata.X.astype('float64')  # this is not required and results will be comparable without it


#Preprocessing and Visualization
sc.pp.recipe_zheng17(adata)
sc.tl.pca(adata, svd_solver='arpack')

#when you run PCA it actually stores the output in .obsm
adata.obsm["X_pca"].shape


#scanpy uses X_pca matrix to compute cellxcell neighbors graph 
#this is running UMAP behind the scenes
sc.pp.neighbors(adata, n_neighbors=4, n_pcs=20)
sc.tl.draw_graph(adata)
sc.pl.draw_graph(adata, color='paul15_clusters', legend_loc='on data')

#when you run neighbors it actually stores the output in .obsm
adata.obsm["X_umap"].shape


#this plot looks very messy. It needs denoising 
#To denoise the graph, we represent it in diffusion map space. This approach has been used in MAGIC
#This is not a necessary step, neither for PAGA, nor clustering, nor pseudotime estimation. You might just as well go ahead with a non-denoised graph. In many situations (also here), this will give you very decent results.
#the way to do this is by computing diffusion maps
sc.tl.diffmap(adata)
sc.pp.neighbors(adata, n_neighbors=10, use_rep='X_diffmap')


###Clustering and PAGA
sc.tl.louvain(adata, resolution=1.0)
#you can also use tl.leiden for clustering
#the clustering can be restricted to a group for greater resotuion of cells within a cluster
#sc.tl.leiden(restric_to= ,key_added="leiden_subclusters")
sc.tl.paga(adata, groups='louvain')
#Visualizing the distribution using known markers
sc.pl.paga(adata, color=['louvain', 'Hba-a2', 'Elane', 'Irf8'])
sc.pl.paga(adata, color=['louvain', 'Itga2b', 'Prss34', 'Cma1'])
adata.obs['louvain'].cat.categories
#annotate clusters using markers
adata.obs['louvain_anno'].cat.categories = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10/Ery', '11', '12',
       '13', '14', '15', '16/Stem', '17', '18', '19/Neu', '20/Mk', '21', '22/Baso', '23', '24/Mo']
#using the annotated clusters for PAGA
sc.tl.paga(adata, groups='louvain_anno')
sc.pl.paga(adata, threshold=0.03, show=False)

###Recomputing the embedding using PAGA-initialization
sc.tl.draw_graph(adata, init_pos='paga')
#we can see all marker genes also at single-cell resolution in a meaningful layout
sc.pl.draw_graph(adata, color=['louvain_anno', 'Itga2b', 'Prss34', 'Cma1'], legend_loc='on data')
#then we could change the colors


##Reconstructing gene changes along PAGA paths for a given set of genes
#Choose a root cell for diffusion pseudotime.
adata.uns['iroot'] = np.flatnonzero(adata.obs['louvain_anno']  == '16/Stem')[0]

#Infer progression of cells through geodesic distance along the graph
sc.tl.dpt(adata)

#Select some of the marker gene names
gene_names = ['Gata2', 'Gata1', 'Klf1', 'Epor', 'Hba-a2',  # erythroid
              'Elane', 'Cebpe', 'Gfi1',                    # neutrophil
              'Irf8', 'Csf1r', 'Ctsg']                     # monocyte


#Use the full raw data for visualization 
adata_raw = sc.datasets.paul15()
sc.pp.log1p(adata_raw)
sc.pp.scale(adata_raw)
adata.raw = adata_raw


## 3 Core plotting functions

#Scatter plots for embeddings (eg. UMAP, t-SNE)
#Identification of clusters using known marker genes
#Visualization of differentially expressed genes

#We can set up the settings for plotting at the beginning of the analysis
sc.set_figure_params(dpi=100, color_map = 'viridis_r')
sc.settings.verbosity = 1
sc.logging.print_header()

pbmc = sc.datasets.pbmc68k_reduced()
import anndata
mouse_brain = anndata.read_h5ad("mouse_brain_s_anndata.h5ad")
mouse_brain.var_names #notice that because they are mouse genes they are in sentence case

with rc_context({'figure.figsize': (4, 4)}):
    sc.pl.umap(pbmc, color='CD79A')

with rc_context({'figure.figsize': (4, 4)}):
    sc.pl.umap(mouse_brain, color='Runx1')

#See what else we can plot 
mouse_brain.obs.columns
with rc_context({'figure.figsize': (3, 3)}):
    sc.pl.umap(mouse_brain, color=['Runx1', 'Klf7', 'Isl2', 'seurat_clusters','nCount_RNA'], s=50, frameon=False, ncols=4, vmax='p99')

sc.pl.umap(mouse_brain, color=['Klf7'],save = '_test2.png' )


marker_genes_dict = {
    'DRG': ['Runx1', 'Isl2'],
    'Other':['Klf7']
}

sc.pl.dotplot(mouse_brain, marker_genes_dict, 'seurat_clusters', dendrogram=True)

#Say that I want to keep only cluster 23
mouse_brain.obs['seurat_clusters'].cat.categories
mouse_brain_new = mouse_brain[mouse_brain.obs['seurat_clusters'].isin(['23']),:]
sc.pl.dotplot(mouse_brain_new, marker_genes_dict, 'celltype', dendrogram=False)

#This information can be used to manually annotate the cells as follows
cluster2annotation = {
     '0': 'Monocytes',
     '1': 'Dendritic',
     '2': 'T-cell',
     '3': 'NK',
     '4': 'B-cell',
     '5': 'Dendritic',
     '6': 'Plasma',
     '7': 'Other',
     '8': 'Dendritic',
}

# add a new `.obs` column called `cell type` by mapping clusters to annotation using pandas `map` function
pbmc.obs['cell type'] = pbmc.obs['clusters'].map(cluster2annotation).astype('category')

#Violin plots
with rc_context({'figure.figsize': (4.5, 3)}):
    sc.pl.violin(mouse_brain, ['Runx1', 'Isl2'], groupby='seurat_clusters' )

#stacked violin plot
ax = sc.pl.stacked_violin(mouse_brain, marker_genes_dict, groupby='seurat_clusters', swap_axes=False, dendrogram=True)

#Comparison of marker genes using split violin plots
with rc_context({'figure.figsize': (9, 1.5)}):
    sc.pl.rank_genes_groups_violin(mouse_brain, n_genes=20, jitter=False)


#check scanpy version 
sc.logging.print_versions()


#https://www.youtube.com/watch?v=EKTg9NV5hEA
#adata.var_names

#you can get information for a given gene
adata[:,'Zyx']
adata[:,'Zyx'].X.shape
adata[:,'Zyx'].obs

#layers
#https://anndata.readthedocs.io/en/latest/anndata.AnnData.layers.html
#it short of goes on top of 




##integrating-data-using-bbknn and ingest
##data integration. Basically integrate replicates with the aim of 
#finding biological variation that is not technical varioation 
#bbknn

#Interoperability with scvi tools 
import scvi

#See https://docs.scvi-tools.org/en/stable/user_guide/notebooks/api_overview.html

# tell scvi where to get the data
adata = scvi.data.heart_cell_atlas_subsampled()

sc.pp.filter_genes(adata, min_counts=3)

#In scivitools we do not need normalized data. We just stored it in a raw
adata.layers["counts"] = adata.X.copy() # preserve counts
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)
adata.raw = adata # freeze the state in `.raw`

#Feature selection to reduce the number of features (genes) we recommend anywhere from 1,000 to 10,000 HVGs
sc.pp.highly_variable_genes(
    adata,
    n_top_genes=1200,
    subset=True,
    layer="counts",
    flavor="seurat_v3",
    batch_key="cell_source"
)

#setup_anndata(), which alerts scvi-tools to the locations of various matrices inside the anndata that we need to do batch correction for
scvi.data.setup_anndata(
    adata,
    layer="counts",
    categorical_covariate_keys=["cell_source", "donor"],
    continuous_covariate_keys=["percent_mito", "percent_ribo"]
)


#Concat anndata
inner = ad.concat([a, b])  # Joining on intersection of variables

##Differential expresion in scanpy 
#rank_genes_groups
adata = sc.datasets.pbmc68k_reduced()
sc.tl.rank_genes_groups(adata, 'bulk_labels', method='wilcoxon')
# to visualize the results
sc.pl.rank_genes_groups(adata)

#scArches trVAE
url = 'https://drive.google.com/uc?id=1ehxgfHTsMZXy6YzlFKGJOsBKQ5rrvMnd'
output = 'pancreas.h5ad'
gdown.download(url, output, quiet=False)



