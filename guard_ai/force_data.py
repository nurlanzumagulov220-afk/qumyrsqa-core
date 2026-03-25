import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

print("--- GENERATING DATA ---")

# 1. Dates setup
today = datetime.now()
dates_list = [(today - timedelta(days=x)) for x in range(730)]

# 2. Incidents (incidents_base.csv)
incidents = []
types = ['Micro', 'Light', 'Heavy']
costs = {'Micro': 500000, 'Light': 5000000, 'Heavy': 15000000}

for _ in range(550):
    t = random.choice(types)
    incidents.append({
        'date': random.choice(dates_list),
        'type': t,
        'location': random.choice(['Shop-1', 'NPS-4', 'Warehouse', 'Drilling']),
        'estimated_cost': costs[t] * 3.0
    })

pd.DataFrame(incidents).to_csv('incidents_base.csv', index=False, encoding='utf-8-sig')
print("File incidents_base.csv created!")

# 3. Korgau Cards (korgau_cards.csv)
korgau = []
for _ in range(1200):
    d = random.choice(dates_list)
    is_crit = (today - d).days <= 7
    
    korgau.append({
        'date': d,
        'obs_type': 'Bad Practice' if (is_crit or random.random() > 0.3) else 'Good Practice',
        'category': 'LOTO' if is_crit else random.choice(['PPE', 'Height', 'Electric']),
        'is_critical': is_crit
    })

pd.DataFrame(korgau).to_csv('korgau_cards.csv', index=False, encoding='utf-8-sig')
print("File korgau_cards.csv created!")
print("DONE! Now run app.py")