import json

with open('d:/MachineLearningIET/notebooks/Lab_4_SckitLearning.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

print(f"Total cells: {len(nb['cells'])}")
for i, cell in enumerate(nb['cells']):
    src = ''.join(cell.get('source', []))
    if any(k in src.lower() for k in ['read_csv', 'path', 'csv', 'save', 'savefig', 'to_csv', 'dir', 'import', 'c:']):
        print(f"=== Cell {i} ({cell.get('cell_type')}) ===")
        print(src)
        print("-" * 50)
