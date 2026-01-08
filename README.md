### Joint SPX/VIX calibration problem with the quintic OU model 

This repository reproduces the results of [Abi Jaber, Illand and Li (2023)](https://arxiv.org/pdf/2212.10917). 

We implement:
- an optimal quantization-based approach to compute expectations of VIX functionals (see `quantization_VIX`),
- the so-called turbocharging method introduced in [McCrickerd, and Pakkanen (2018)](https://arxiv.org/pdf/1708.02563) to reduce drastically the variance on IV SPX computations (see `turbocharging.ipynb`), 
- joint SPX/VIX calibration using a parametric forward variance curve (see `calibration_parametric_xi.ipynb`),
- joint SPX/VIX calibration using the market forward variance curve, stripped via the Carr-Madan formula (see `genuine_calibration.ipynb`).

**Note:** Nous comparons les performances du noyau $K^\text{exp}$ avec les noyaux $K^\text{frac}$ et $K^\text{shift}$ comme illustré dans [Abi Jaber, Illand and Li (2024)](https://arxiv.org/pdf/2212.08297). 

### Examples of illustrations

![turbo_exp](assets/turbocharging_exp.png)

![iv_test](assets/test_iv_vix.png)


### Disclaimer

Full source code is avaible upon requests. Please contact me directly. Due to licensing restrictions, the raw data cannot be publicy released.