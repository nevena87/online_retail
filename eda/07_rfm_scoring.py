import pandas as pd
import os

# -------------------------
# PATH SETUP
# -------------------------
project_path = r"C:\Users\Nevena\Radna površina\OnlineRetail_Project"
data_path = os.path.join(project_path, "data")

# -------------------------
# LOAD RFM DATA
# -------------------------
rfm = pd.read_csv(os.path.join(data_path, "rfm.csv"))

print("✔ Loaded RFM shape:", rfm.shape)

# -------------------------
# CLEAN SAFETY (IMPORTANT)
# -------------------------
rfm = rfm.dropna(subset=["Recency", "Frequency", "Monetary"])

# -------------------------
# RFM SCORING (QUARTILES)
# -------------------------

# Recency (manje = bolje → obrnuto scoring)
rfm["R_Score"] = pd.qcut(
    rfm["Recency"],
    4,
    labels=[4, 3, 2, 1],
    duplicates="drop"
)

# Frequency
rfm["F_Score"] = pd.qcut(
    rfm["Frequency"].rank(method="first"),
    4,
    labels=[1, 2, 3, 4]
)

# Monetary
rfm["M_Score"] = pd.qcut(
    rfm["Monetary"],
    4,
    labels=[1, 2, 3, 4]
)

# -------------------------
# TYPE FIX
# -------------------------
rfm[["R_Score", "F_Score", "M_Score"]] = rfm[
    ["R_Score", "F_Score", "M_Score"]
].astype(int)

# -------------------------
# COMBINED SCORE
# -------------------------
rfm["RFM_Score"] = (
    rfm["R_Score"].astype(str) +
    rfm["F_Score"].astype(str) +
    rfm["M_Score"].astype(str)
)

# -------------------------
# SAVE OUTPUT
# -------------------------
output_path = os.path.join(data_path, "rfm_scored.csv")
rfm.to_csv(output_path, index=False)

print("✔ RFM scoring completed")
print("✔ Saved to:", output_path)