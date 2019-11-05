```
Usage: python gpuseizer.py [num_gpu_needed] [script]

When enough GPUs are available, the script would point CUDA_VISIBLE_DEVICES 
envrion to them and run the script.

Example:
  $ python gpuseizer.py 2 python run.py
```
