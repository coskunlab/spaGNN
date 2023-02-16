# spaGNN
Spatial gene neighborhood network analysis of subcellular spatial transcriptomics.

Codes under "image_processing"  directory should be run under skim environment, set up by skimEnv.yml file.
Codes under "subcellular_analyses"  directory should be run under scanpy environment, set up by scanpyEnv.yml file.
  - "05_connectivityToNetwork.ipynb" should be run under networkx environment, set up by netwoorkEnv.yml file.
Codes under "transcriptomics_analysis" directory should be run under scanpy environment, set up by skim.iml file.



## MERFISH analysis
01_merFishPatchAnalyss.ipynb generates analysis results and figures for patch correlation analysis and the following figures:

Rna visualization:
![Alt text](https://github.com/coskunlab/spaGNN/blob/main/MERFISH_analysis/code/figures/fibroblast%20shuffled%20merfish%20cell06%20scatter%20comp%20colors.png)

Single-cell patch detection:
![Alt text](https://github.com/coskunlab/spaGNN/blob/main/MERFISH_analysis/code/figures/show%20fibroblast%20patches.png)

Single-cell patch correlations:
![Alt text](https://github.com/coskunlab/spaGNN/blob/main/MERFISH_analysis/code/figures/fibroblast%20cell06%20patch%20correlation.png)

The locations of gene pairs with positive and negative correlations are also plotted:
![Alt text](https://github.com/coskunlab/spaGNN/blob/main/MERFISH_analysis/code/figures/cell06%20correlation%20scatter.png)

02_neighborhoodNetworkAnalysis.ipynb performs gene neighborhood networks analysis. The code detects gene neighbors as shown below:
![Alt text](https://github.com/coskunlab/spaGNN/blob/main/MERFISH_analysis/code/figures/merfish%20fibroblast%20patch3%20thbs1%20fbn2%20srrm2.png)

After counting number of times that two genes are neighbors, a permutation analysis was performed to determine the proximity score of two genes. Higher proximity scores mean the two genes are more likely to be neighbors given the copy number of each genes. Pairs of genes within different proximity scores are also visualized in a scatter plot:
<img src="https://github.com/coskunlab/spaGNN/blob/main/MERFISH_analysis/code/figures/cell06%20patch2%20scatter.png" width="50">
## SeqFISH analysis
