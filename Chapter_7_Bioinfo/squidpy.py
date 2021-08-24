import scanpy as sc
import squidpy as sq

sc.logging.print_header()
print(f"squidpy=={sq.__version__}")

# load the pre-processed dataset
adata = sq.datasets.merfish()
adata

#Visualization
#Visualize the 3D stack of slides using 
sc.pl.embedding(adata, basis="spatial3d", projection="3d", color="Cell_class")
#Visualize a single slide
sc.pl.spatial(adata[adata.obs.Bregma == -9], color="Cell_class", spot_size=0.01)

#Neighbourh enrichment analysis in 3D
sq.gr.spatial_neighbors(adata, coord_type="generic", spatial_key="spatial3d")
sq.gr.nhood_enrichment(adata, cluster_key="Cell_class")
sq.pl.nhood_enrichment(adata, cluster_key="Cell_class", method="single", cmap="inferno", vmin=-50, vmax=100)


#Analysis in 2D
adata_slice = adata[adata.obs.Bregma == -9].copy()
sq.gr.spatial_neighbors(adata_slice, coord_type="generic")
sq.gr.nhood_enrichment(adata, cluster_key="Cell_class")
sc.pl.spatial(
    adata_slice,
    color="Cell_class",
    groups=["Ependymal", "Pericytes", "Endothelial 2"],
    spot_size=0.01,
)