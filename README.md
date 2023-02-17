# spaGNN

This repository contains code for the manuscript "Spatially resolved gene neighborhood networks in single cells". Codes are run under specified Anaconda environments.

To set up environments, run the following command: `conda env create -f filename.yml`

## MERFISH analysis

All code in MERFISH analysis should be run under the scenv environment except for 04_networkVisualization.ipynb. 

04_networkVisualization.ipynb should be run under the network environment. The network environment can be 

01_merFishPatchAnalyss.ipynb generates analysis results and figures for patch correlation analysis and the following figures:

Rna visualization:

<img src="https://github.com/coskunlab/spaGNN/blob/main/MERFISH_analysis/code/figures/fibroblast%20shuffled%20merfish%20cell06%20scatter%20comp%20colors.png" width="600">

Single-cell patch detection:

<img src="https://github.com/coskunlab/spaGNN/blob/main/MERFISH_analysis/code/figures/show%20fibroblast%20patches.png" width="500">

Single-cell patch correlations:

<img src="https://github.com/coskunlab/spaGNN/blob/main/MERFISH_analysis/code/figures/fibroblast%20cell06%20patch%20correlation.png" width="500">

The locations of gene pairs with positive and negative correlations are also plotted:

<img src="https://github.com/coskunlab/spaGNN/blob/main/MERFISH_analysis/code/figures/cell06%20correlation%20scatter.png" width="500">

02_neighborhoodNetworkAnalysis.ipynb performs gene neighborhood networks analysis. The code detects gene neighbors as shown below:

<img src="https://github.com/coskunlab/spaGNN/blob/main/MERFISH_analysis/code/figures/merfish%20fibroblast%20patch3%20thbs1%20fbn2%20srrm2.png" width="500">

After counting number of times that two genes are neighbors, a permutation analysis was performed to determine the proximity score of two genes. Higher proximity scores mean the two genes are more likely to be neighbors given the copy number of each genes. Pairs of genes within different proximity scores are also visualized in a scatter plot:

<img src="https://github.com/coskunlab/spaGNN/blob/main/MERFISH_analysis/code/figures/cell06%20patch2%20scatter.png" width="600">

03_coclusteringAnalysis.ipynb clusters cells based on single-cell gene count, patch correlation, or network variability. The clustering result and true cell types are visualized using t-sne plot

<img src="https://github.com/coskunlab/spaGNN/blob/main/MERFISH_analysis/code/figures/tsne%20merfish%20gene%20count%20cell%20types.png" height="300"> <img src="https://github.com/coskunlab/spaGNN/blob/main/MERFISH_analysis/code/figures/tsne%20merfish%20gene%20count%20clustering.png" height="300">
<img src="https://github.com/coskunlab/spaGNN/blob/main/MERFISH_analysis/code/figures/tsne%20merfish%20gene%20patch%20correlation%20cell%20type.png" height="300">  <img src="https://github.com/coskunlab/spaGNN/blob/main/MERFISH_analysis/code/figures/tsne%20merfish%20gene%20patch%20correlation%20clustering.png" height="300">
<img src="https://github.com/coskunlab/spaGNN/blob/main/MERFISH_analysis/code/figures/tsne%20merfish%20network%20variability%20cell%20type.png" height="300"> <img src="https://github.com/coskunlab/spaGNN/blob/main/MERFISH_analysis/code/figures/tsne%20merfish%20network%20variability%20clustering.png" height="300">

04_networkVisualization.ipynb uses networkx package to visualize gene pairwise proximity scores in network format.
<img src="https://github.com/coskunlab/spaGNN/blob/main/MERFISH_analysis/code/figures/merfish_cell_06__patch_23.png">

05_clustering_eval.ipynb evaluated the mismatch between the clustering results and cell types. Confusion matrix shown below are count-based, patch correlation-based, and network variability-based clustering.

<img src="https://github.com/coskunlab/spaGNN/blob/main/MERFISH_analysis/code/figures/merfish%20confusion%20matrix%20count.png" width="200">  <img src="https://github.com/coskunlab/spaGNN/blob/main/MERFISH_analysis/code/figures/merfish%20confusion%20matrix%20patch.png" width="200">  <img src="https://github.com/coskunlab/spaGNN/blob/main/MERFISH_analysis/code/figures/merfish%20confusion%20matrix%20network.png" width="200">

## SeqFISH analysis

The analysis of MSC seqFISH dataset is similar to the analysis of MERFISH dataset with the addition of image analysis using codes in the "image_processing" folder. All image processing is conducted under skim environment, specified by skimEnv.yml.

00_Registration.ipynb cross-register images fro different cycles

01_dotDetectionThreCheck.ipynb allows user to manually identify threshold for dot detection in each channel. The following plot is generated to help examin the threshold:

<img src="https://github.com/coskunlab/spaGNN/blob/main/seqFISH_analysis/image_processing/figures/dot%20check.png" width="2000">

02_2dDotDetection.ipynb takes the input directories and detect dots. The detected dots are saved as .hdf5 files. A matrix of the size length x width x number of genes is stored. Each layer represent a gene. The value is 1 at the position of detected dots and 0 otherwise.

03_cytokineDetection.ipynb provides more detailed dot detection if dot detected by 02_2dDotDetection.ipynb needs additional tuning.

The spatially resolved gene neighborhood network analysis is perfomed by codes under "subcelluar_analysis" folder. All subcellular analysis is performed under the scenv environment specified by scanpyEnv.yml.

00_dotFiles2pkl.ipynb takes the .hdf5 files containing the information regarding detected dots and generate a dictionary for each cell. The keys of the dictionary are the gene names, and each item is a list of row and column positions of detected transcripts.

01_subcellularPatches.ipynb performs clustering-based subcellular patch detection and patch correlation calculation. Detected patches and patch correlation is shown below:

<img src="https://github.com/coskunlab/spaGNN/blob/main/seqFISH_analysis/subcellular_analysis/figures/showexp2_uc_017_1.png" height="300"> <img src="https://github.com/coskunlab/spaGNN/blob/main/seqFISH_analysis/subcellular_analysis/figures/uc%20mean%20correlation.png" height="300">

02_neighborhoodCorrelationAnalyses.ipynb performs analysis on combined patch correlations. All pair-wise correlations are combined and analyzed for HBM, HUC, and HCH dataset. A PCA analysis was conducted, and statistical comparison was conducted to identify significant differences.

<img src="https://github.com/coskunlab/spaGNN/blob/main/seqFISH_analysis/subcellular_analysis/figures/pca%20correlation%20cell%20type.png" height="350">

<img src="https://github.com/coskunlab/spaGNN/blob/main/seqFISH_analysis/subcellular_analysis/figures/bm%20uc%20hch%20pc1%20correlation.png" height="350">

03_subcellularNetworkInference.ipynb finds local gene neighborhoods as shown below:

<img src="https://github.com/coskunlab/spaGNN/blob/main/seqFISH_analysis/subcellular_analysis/figures/nearest%20neighbor%20visual.png" height="300">

Then the amount of gene per local neighborhood is counted, and correlation of gene is then calculated. The mean and standard deviation of pairwise gene neighborhood correlation was computed for each cell, and cells were clustered based on the mean and standard deviation of pairwise gene neighborhood correlations. The clustering result and cell types are visualized in t-SNE plots shown below:

<img src="https://github.com/coskunlab/spaGNN/blob/main/seqFISH_analysis/subcellular_analysis/figures/tsne%20msc%20network%20variability%20clustering.png" height="200">  <img src="https://github.com/coskunlab/spaGNN/blob/main/seqFISH_analysis/subcellular_analysis/figures/tsne%20msc%20network%20variability%20cell%20types.png" height="200">

04_coclusteringAnalysis.ipynb clusters cells based on single-cell RNA count and patch correlations. The clustering results and cell types are visualized on t-SNE plots as shown below:

<img src="https://github.com/coskunlab/spaGNN/blob/main/seqFISH_analysis/subcellular_analysis/figures/tsne%20msc%20gene%20count%20clustering.png" height="200">  <img src="https://github.com/coskunlab/spaGNN/blob/main/seqFISH_analysis/subcellular_analysis/figures/tsne%20msc%20gene%20count%20cell%20types.png" height="200">

<img src="https://github.com/coskunlab/spaGNN/blob/main/seqFISH_analysis/subcellular_analysis/figures/tsne%20msc%20patch%20correlation%20clustering.png" height="200">  <img src="https://github.com/coskunlab/spaGNN/blob/main/seqFISH_analysis/subcellular_analysis/figures/tsne%20msc%20patch%20correlation%20cell%20types.png" height="200">

05_connectivityToNetwork.ipynb visualizes the pairwise gene neighborhood correlations of each subcellular patch in network format. This code should be run under the network environment specified in networkEnv.yml.

<img src="https://github.com/coskunlab/spaGNN/blob/main/seqFISH_analysis/subcellular_analysis/figures/exp1_uc_017_6.png" height="250"> <img src="https://github.com/coskunlab/spaGNN/blob/main/seqFISH_analysis/subcellular_analysis/figures/exp1_uc_017_19.png" height="250">

06_rnaProteinNetwork.ipynb expands the subcellular gene neighborhood networks to protein markers. Both patch correlations and local gene neighborhood networks are expanded to inlcude protein markers.

<img src="https://github.com/coskunlab/spaGNN/blob/main/seqFISH_analysis/subcellular_analysis/figures/protein%20rna%20subcellular%20region%20correlation_v4.png" height="300">

<img src="https://github.com/coskunlab/spaGNN/blob/main/seqFISH_analysis/subcellular_analysis/figures/showhch%20patch5.png" height="250">  <img src="https://github.com/coskunlab/spaGNN/blob/main/seqFISH_analysis/subcellular_analysis/figures/hch_006_06_5.png" height="250">

07_circularNetworks.ipynb extract patch correlation and gene neighborhood networks based on distances from the edge of cells.


<img src="https://github.com/coskunlab/spaGNN/blob/main/seqFISH_analysis/subcellular_analysis/figures/exp1%20uc%20013%20cell1.png" width="300">

08_clustering_eval.ipynb evaluated the mismatch between the clustering results and cell types. Confusion matrix shown below are count-based, patch correlation-based, and network variability-based clustering.

<img src="https://github.com/coskunlab/spaGNN/blob/main/seqFISH_analysis/subcellular_analysis/figures/seqfish%20confusion%20matrix%20expression%20clustering%20v.%20cell%20type.pkl.png" height="300"> <img src="https://github.com/coskunlab/spaGNN/blob/main/seqFISH_analysis/subcellular_analysis/figures/seqfish%20confusion%20matrix%20correlation%20clustering%20v.%20cell%20type.pkl.png" height="300"> <img src="https://github.com/coskunlab/spaGNN/blob/main/seqFISH_analysis/subcellular_analysis/figures/seqfish%20confusion%20matrix%20network%20variance%20clustering%20v.%20cell%20type.pkl.png" height="300">
