import json

with open('d:/MachineLearningIET/notebooks/Lab3_EDA.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    src = ''.join(cell.get('source', []))
    if any(term in src for term in ['C:', 'D:', 'http', '/', '\\', 'Path', 'csv', 'png', 'savefig', 'to_']):
        print(f"Cell {i} ({cell.get('cell_type')}):")
        print(src)
        print("=" * 40)
