import pandas as pd

data0 = pd.read_csv('DFF/data.csv')

data0['Tra-AcBa Proportion'] = data0['TransactionAmount (TrA)'] / data0['AccountBalance (AcBa)']

# Fraud Accounts
data = data0[data0['Fraud'] == True]

# Series for fraud and non-fraud accounts
data0_series = pd.Series(data0['Tra-AcBa Proportion'])
data_series = pd.Series(data['Tra-AcBa Proportion'])

# Proximity Value Counter Function
def counter(series, dict):
    c0 = 0
    for i in range(1, 100):
        c = series[(series*1000 < i)].count()
        c1 = c - c0
        dict[f'{i-1} - {i}'] = c1
        c0 = c1
    return dict

# Counting Accounts for individual set | b1 system
data_dict = {}
data0_dict = {}
data_count = counter(data_series, data_dict)
data0_count = counter(data0_series, data0_dict)

# Counting Accounts for individual set | b2 system
# -- PRC 1 --
prc1_0 = data0[data0['TransactionCategory (TrC)'] == 'PRC 1']
prc1 = prc1_0[prc1_0['Fraud'] == True]

prc1_0_series = pd.Series(prc1_0['Tra-AcBa Proportion'])
prc1_series = pd.Series(prc1['Tra-AcBa Proportion'])

prc1_dict = {}
prc1_0_dict = {}

prc1_0_count = counter(prc1_0_series, prc1_0_dict)
prc1_count = counter(prc1_series, prc1_dict)

# -- PRC 2 --
prc2_0 = data0[data0['TransactionCategory (TrC)'] == 'PRC 2']
prc2 = prc2_0[prc2_0['Fraud'] == True]

prc2_0_series = pd.Series(prc2_0['Tra-AcBa Proportion'])
prc2_series = pd.Series(prc2['Tra-AcBa Proportion'])

prc2_dict = {}
prc2_0_dict = {}

prc2_0_count = counter(prc2_0_series, prc2_0_dict)
prc2_count = counter(prc2_series, prc2_dict)

# -- PRC 3 --
prc3_0 = data0[data0['TransactionCategory (TrC)'] == 'PRC 3']
prc3 = prc3_0[prc3_0['Fraud'] == True]

prc3_0_series = pd.Series(prc3_0['Tra-AcBa Proportion'])
prc3_series = pd.Series(prc3['Tra-AcBa Proportion'])

prc3_dict = {}
prc3_0_dict = {}

prc3_0_count = counter(prc3_0_series, prc3_0_dict)
prc3_count = counter(prc3_series, prc3_dict)

# -- PRC 4 --
prc4_0 = data0[data0['TransactionCategory (TrC)'] == 'PRC 4']
prc4 = prc4_0[prc4_0['Fraud'] == True]

prc4_0_series = pd.Series(prc4_0['Tra-AcBa Proportion'])
prc4_series = pd.Series(prc4['Tra-AcBa Proportion'])

prc4_dict = {}
prc4_0_dict = {}

prc4_0_count = counter(prc4_0_series, prc4_0_dict)
prc4_count = counter(prc4_series, prc4_dict)

# Data for visualization
