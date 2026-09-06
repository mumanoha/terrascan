import torch
import torch.nn as nn

class TerraScanAI(nn.Module):
    """
    TerraScan v1 Physics-Informed Neural Network (PINN).
    Preserved exactly as presented in PJAS 2026 presentation (Slide 17).
    
    Inductive bias: Softplus activation on output layer to enforce
    non-negativity of soil chemical concentrations (non-negative mass constraint).
    """
    def __init__(self):
        super(TerraScanAI, self).__init__()
        self.encoder = nn.Sequential(
            nn.Linear(12, 128),
            nn.LeakyReLU(0.1),
            nn.BatchNorm1d(128),
            nn.Dropout(0.25),

            nn.Linear(128, 256),
            nn.LeakyReLU(0.1),
            nn.BatchNorm1d(256),
            nn.Dropout(0.25),

            nn.Linear(256, 128),
            nn.LeakyReLU(0.1),
        )
        self.head = nn.Linear(128, 3)
        self.constraint = nn.Softplus()

    def forward(self, x):
        feat = self.encoder(x)
        raw_out = self.head(feat)
        return self.constraint(raw_out)

if __name__ == "__main__":
    model = TerraScanAI()
    dummy_input = torch.randn(4, 12)
    output = model(dummy_input)
    print("TerraScan v1 Model Instantiated Successfully.")
    print("Input shape:", dummy_input.shape)
    print("Output shape (N, P, K):", output.shape)
    print("Sample output:", output)
