"""
Generates a synthetic solar_system_census.csv with realistic biometric
distributions for the four homelands described in the subject.
Run once: python generate_dataset.py
"""
import numpy as np
import csv

rng = np.random.default_rng(42)

N = 100  # individuals per homeland

populations = {
    "Venus":  dict(height=(1.60, 0.05), weight=(55, 5),  bone=(1.3, 0.1)),
    "Earth":  dict(height=(1.75, 0.06), weight=(70, 8),  bone=(1.2, 0.1)),
    "Mars":   dict(height=(1.85, 0.07), weight=(75, 9),  bone=(1.1, 0.1)),
    "Belt":   dict(height=(2.00, 0.08), weight=(80, 10), bone=(0.7, 0.1)),
}

rows = []
idx = 0
for homeland, params in populations.items():
    h = rng.normal(params['height'][0], params['height'][1], N)
    w = rng.normal(params['weight'][0], params['weight'][1], N)
    b = rng.normal(params['bone'][0],   params['bone'][1],   N)
    for hi, wi, bi in zip(h, w, b):
        rows.append({'Index': idx, 'height': round(hi, 4),
                     'weight': round(wi, 4), 'bone_density': round(bi, 4)})
        idx += 1

rng.shuffle(rows)

with open('solar_system_census.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Index', 'height', 'weight', 'bone_density'])
    writer.writeheader()
    writer.writerows(rows)

print(f"Generated solar_system_census.csv  ({len(rows)} rows)")
