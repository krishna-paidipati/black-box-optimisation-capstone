# Raw data

Place the course-provided `initial_data` directory here.

Expected layout:

```text
data/raw/initial_data/function_1/initial_inputs.npy
data/raw/initial_data/function_1/initial_outputs.npy
...
data/raw/initial_data/function_8/initial_inputs.npy
data/raw/initial_data/function_8/initial_outputs.npy
```

Raw `.npy` files are ignored by Git by default. Remove the corresponding rule from `.gitignore` only if you have permission to redistribute the dataset.
