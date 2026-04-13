import pandas as pd
import numpy as np
import os

# -------------------------
# PATH
# -------------------------
project_path = r"C:\Users\Nevena\Radna površina\OnlineRetail_Project"
data_path = os.path.join(project_path, "data")

# -------------------------
# LOAD DATA
# -------------------------
rfm = pd.read_csv(os.path.join(data_path, "rfm_scored.csv"))

print("✔ Loaded:", rfm.shape)

# -------------------------
# SEGMENTATION (VECTORISED VERSION)
# -------------------------

conditions = [
    (rfm["R_Score"] == 4) & (rfm["F_Score"] >= 3) & (rfm["M_Score"] >= 3),
    (rfm["F_Score"] >= 3) & (rfm["M_Score"] >= 2),
    (rfm["R_Score"] >= 3) & (rfm["F_Score"] <= 2),
    (rfm["R_Score"] <= 2) & (rfm["F_Score"] >= 2),
]

choices = [
    "Champions",
    "Loyal Customers",
    "Potential Loyalists",
    "At Risk"
]

rfm["Segment"] = np.select(conditions, choices, default="Lost Customers")

# -------------------------
# SAVE OUTPUT
# -------------------------
output_path = os.path.join(data_path, "rfm_segmented.csv")
rfm.to_csv(output_path, index=False)

print("✔ RFM segmentation completed")
print("✔ Saved to:", output_path)