import json
from pathlib import Path

# 1. Update Lab3_EDA.ipynb
with open('d:/MachineLearningIET/notebooks/Lab3_EDA.ipynb', 'r', encoding='utf-8') as f:
    nb_eda = json.load(f)

# Cell 2
cell2_src = """from pathlib import Path

possible_paths = [
    Path("../data/processed/olist_orders_abt.csv"),
    Path("../Notebook/data/processed/olist_orders_abt.csv"),
    Path("data/processed/olist_orders_abt.csv"),
    Path("olist_orders_abt.csv")
]
data_path = next((p for p in possible_paths if p.exists()), None)
if data_path is None:
    raise FileNotFoundError("Could not find olist_orders_abt.csv")
df = pd.read_csv(data_path)
df.head()
"""
nb_eda['cells'][2]['source'] = [line + '\n' for line in cell2_src.splitlines()]

# Cell 46
cell46_src = """#Saving Cleaned ABT
output_dir = Path("../data/processed") if Path("../data/processed").exists() else Path("../Notebook/data/processed")
output_dir.mkdir(parents=True, exist_ok=True)
clean_df.to_csv(output_dir / "olist_orders_abt_cleaned.csv", index=False)
if Path("../Notebook/data/processed").exists() and output_dir != Path("../Notebook/data/processed"):
    clean_df.to_csv(Path("../Notebook/data/processed/olist_orders_abt_cleaned.csv"), index=False)
print("Cleaned ABT saved successfully.") 
print(clean_df.shape)
"""
nb_eda['cells'][46]['source'] = [line + '\n' for line in cell46_src.splitlines()]

with open('d:/MachineLearningIET/notebooks/Lab3_EDA.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb_eda, f, indent=1)
print("Lab3_EDA.ipynb paths updated successfully.")

# 2. Update Lab_4_SckitLearning.ipynb
with open('d:/MachineLearningIET/notebooks/Lab_4_SckitLearning.ipynb', 'r', encoding='utf-8') as f:
    nb_lab4 = json.load(f)

# Cell 2
cell2_lab4_src = """possible_paths = [ 
    Path("../data/processed/olist_orders_abt.csv"),
    Path("../Notebook/data/processed/olist_orders_abt.csv"), 
    Path("data/processed/olist_orders_abt.csv"), 
    Path("olist_orders_abt.csv") 
]

data_path = None 
for path in possible_paths: 
    if path.exists(): 
        data_path = path 
        break
if data_path is None: 
    raise FileNotFoundError("Could not find olist_orders_abt.csv. Please check the file path.")

df = pd.read_csv(data_path)
df.head()
"""
nb_lab4['cells'][2]['source'] = [line + '\n' for line in cell2_lab4_src.splitlines()]

# Cell 33
cell33_lab4_src = """output_dir = Path("../models") if Path("../models").exists() else Path("../Notebook/models")
output_model_path = output_dir / "late_delivery_pipeline.joblib"
output_model_path.parent.mkdir(parents=True, exist_ok=True) 
joblib.dump(model_pipeline, output_model_path)
if Path("../Notebook/models").exists() and output_dir != Path("../Notebook/models"):
    joblib.dump(model_pipeline, Path("../Notebook/models/late_delivery_pipeline.joblib"))
print("Pipeline saved at:", output_model_path)
"""
nb_lab4['cells'][33]['source'] = [line + '\n' for line in cell33_lab4_src.splitlines()]

with open('d:/MachineLearningIET/notebooks/Lab_4_SckitLearning.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb_lab4, f, indent=1)
print("Lab_4_SckitLearning.ipynb paths updated successfully.")
