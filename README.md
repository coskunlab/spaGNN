# spaGNN
Spatial gene neighborhood network analysis of subcellular spatial transcriptomics.

Codes under "image_processing"  directory should be run under skim environment, set up by skimEnv.yml file.
Codes under "subcellular_analyses"  directory should be run under scanpy environment, set up by scanpyEnv.yml file.
  - "05_connectivityToNetwork.ipynb" should be run under networkx environment, set up by netwoorkEnv.yml file.
Codes under "transcriptomics_analysis" directory should be run under scanpy environment, set up by skim.iml file.



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
<img src="">

## SeqFISH analysis
