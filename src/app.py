import streamlit as st
import json
import matplotlib.pyplot as plt
import numpy as np
from simulator import summarize_results

# Load test results
with open("data/test_results.json") as f:
    test_results = json.load(f)

summary = summarize_results(test_results)

st.title("A/B Testing Simulator Dashboard")

# Show summary metrics
st.header("Summary Statistics")
for variant, stats in summary.items():
    st.subheader(f"Variant {variant.upper()}")
    st.write(stats)

# Plot histograms
st.header("Distribution Comparison")
fig, ax = plt.subplots()
for variant, data in test_results.items():
    ax.hist(data, bins=5, alpha=0.5, label=variant)
ax.set_title("Histogram of Conversion Rates")
ax.set_xlabel("Rate")
ax.set_ylabel("Frequency")
ax.legend()
st.pyplot(fig)
