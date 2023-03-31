## HMCDA

A novel method based on the heterogeneous graph neural network and metapath for circRNA-disease associations prediction.

### Dependencies

* python 3.6
* PyTorch 1.2.0
* NetworkX 2.3
* scikit-learn 0.21.3
* NumPy 1.17.2
* SciPy 1.3.1
* DGL 0.3.1



### Datasets

| Entity types | num  | Edge types      | num  |
| ------------ | ---- | --------------- | ---- |
| circRNA      | 1556 | circRNA-disease | 2160 |
| miRNA        | 840  | circRNA-miRNA   | 1964 |
| Disease      | 243  | miRNA-disease   | 1964 |
| Total        | 2639 | Total           | 6088 |

### Usage



1.data preprocess: run preprocess_HMCDA.ipynb



2.run run_HMCDA.py  

