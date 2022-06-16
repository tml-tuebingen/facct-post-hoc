# Post-Hoc Explanations Fail to Achieve their Purpose in Adversarial Contexts

This repository contains the code to reproduce the results in the FAccT 2022 paper *Post-Hoc Explanations Fail to Achieve their Purpose in Adversarial Contexts* by Sebastian Bordt, Michèle Finck, Eric Raidl, and Ulrike von Luxburg.

[FAccT'22 Paper](https://arxiv.org/abs/2201.10295) | [Video about the paper](https://www.youtube.com/watch?v=X_itngSLf5A) 

<img src="https://github.com/tml-tuebingen/facct-post-hoc/blob/main/facct_logo.png" width="100"/>

## Overview

The code is organized with one jupyter notebook per dataset. 

*Adult-Income*: [Jupyter Notebook](https://github.com/tml-tuebingen/facct-post-hoc/blob/main/adult-income.ipynb)

*Folktables ACSIncome*: [Jupyter Notebook](https://github.com/tml-tuebingen/facct-post-hoc/blob/main/folktables.ipynb)

*German Credit*: [Jupyter Notebook](https://github.com/tml-tuebingen/facct-post-hoc/blob/main/german-credit.ipynb)

*UCI Diabetes*: [Jupyter Notebook](https://github.com/tml-tuebingen/facct-post-hoc/blob/main/uci-diabetes.ipynb)

*UCI Wisconsin Breast Cancer*: [Jupyter Notebook](https://github.com/tml-tuebingen/facct-post-hoc/blob/main/uci-cancer.ipynb)

*Reference Dataset Example*: [Jupyter Notebook](https://github.com/tml-tuebingen/facct-post-hoc/blob/main/reference-dataset.ipynb)

## Required Packages

- xgboost https://github.com/dmlc/xgboost (Version: 1.5.1)
- DiCE https://github.com/interpretml/DiCE (Version 0.7.2)
- folktables https://github.com/zykls/folktables (Version 0.0.11)

## Citing the paper

If you use this software please consider citing our paper:
```
@article{bordt2022facct,
  title={Post-hoc explanations fail to achieve their purpose in adversarial contexts},
  author={Bordt, Sebastian and Finck, Mich{\`e}le and Raidl, Eric and von Luxburg, Ulrike},
  journal={arXiv preprint arXiv:2201.10295},
  year={2022}
}

```
