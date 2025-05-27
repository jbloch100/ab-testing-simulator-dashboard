import numpy as np

def summarize_results(results):
    summary = {}
    for variant, data in results.items():
        arr = np.array(data)
        summary[variant] = {
            "mean": np.mean(arr),
            "std": np.std(arr),
            "max": np.max(arr),
            "min": np.min(arr)
        }
    return summary
