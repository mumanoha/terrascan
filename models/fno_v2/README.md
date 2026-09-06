# Fourier Neural Operator (FNO) 2D Architecture
_Last updated: 2026-09-06 · Status: verified_

## TL;DR
The Fourier Neural Operator (FNO) in TerraScan v2 maps continuous multi-channel satellite and rover spectral fields to 2D continuous spatial nutrient concentration distributions. Unlike standard CNNs or MLPs, FNO performs parameter learning in the frequency domain via Fast Fourier Transforms (FFT), enabling mesh-independent resolution invariance and direct coupling with physics-informed conservation PDEs.

## PyTorch Implementation

Source file: [`model.py`](file:///Users/muthumano/Documents/WORK/code/personal_projects/terrascan_project/models/fno_v2/model.py)

```python
"""
TerraScan v2: 2D Fourier Neural Operator (FNO2d) Architecture
Resolution-invariant neural operator for continuous spatial field estimation of soil nutrients.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F

class SpectralConv2d(nn.Module):
    """2D Fourier Layer: performs FFT, linear transform on lower Fourier modes, and IFFT."""
    def __init__(self, in_channels: int, out_channels: int, modes1: int, modes2: int):
        super().__init__()
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.modes1 = modes1
        self.modes2 = modes2
```

### Core Architecture

- **Spectral Convolution**: Computes continuous global convolutions in frequency space:
  $$\mathcal{K}(v)(x) = \mathcal{F}^{-1} \left( R_{\phi} \cdot (\mathcal{F} v) \right)(x)$$
- **Resolution Invariance**: The model can be trained on a coarse $32 \times 32$ grid and directly evaluated on a fine $128 \times 128$ grid without retraining or losing spatial coherence.
- **Physics Loss Regularization**: Embedded directly into the loss objective to enforce nutrient mass conservation and terrain-guided hydrological advection-dispersion.
