import pandas as pd
import numpy as np

# Data Generation
data = pd.DataFrame({
    'TransactionID (TrID)': range(1, 101),
    'TransactionAmount (TrA)': np.random.choice(a = range(1, 101),size = 100),
    'AccountBalance (AcBa)': np.random.choice(a = range(1000, 10000),  size = 100),
    'TransactionCategory (TrC)': np.random.choice(['PRC 1', 'PRC 2', 'PRC 3', 'PRC 4'], 100),
    'TransactionTime (TrT)': np.random.choice(a = range(1, 25), size = 100),
})

data.to_csv('try1.csv', index = False)