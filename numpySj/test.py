import torch
print(torch.backends.mps.is_available())
print(torch.backends.mps.is_built())
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
print(device)
