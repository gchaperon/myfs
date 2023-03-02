import io
import torch
import fsspec

with fsspec.open(
    "gchapero://models/cifar10-classifier/checkpoints/epoch=4-step=3910.ckpt", "rb"
) as f:
    asd = torch.load(io.BytesIO(f.read()))

breakpoint()
pass

# gchapero://models/cifar10-classifier@<hash>:<voter>
