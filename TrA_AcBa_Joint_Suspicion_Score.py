import pandas as pd
from tempdata import data_count, data0_count

# User Input (ui) Handling

def b1_score_system(df):
    df['Tra-AcBa Proportion'] = df['TransactionAmount (TrA)'] / df['AccountBalance (AcBa)']

    ui2 = pd.Series(df['Tra-AcBa Proportion'])

    for i in range(1, 100):
        c1 = ui2[(ui2*1000 < i)].count()
        if c1 == 0:
            continue
        elif c1 == 1:
            n_user_code = f'{i - 1} - {i}'
            u_user_code = f'{i} - {i + 1}'
            if i != 1:
                l_user_code = f'{i - 2} - {i - 1}'
            elif i == 1:
                l_user_code = f'{i + 1} - {i + 2}'
            break

    npf = data0_count[n_user_code]
    ff_npf = data_count[n_user_code]
    npfr = ff_npf / npf

    upf = data0_count[u_user_code]
    ff_upf = data_count[u_user_code]
    upfr = ff_upf / upf

    lpf = data0_count[l_user_code]
    ff_lpf = data_count[l_user_code]
    lpfr = ff_lpf / lpf

    # b1 scoring system

    if npfr > upfr and npfr > lpfr:
        b1 = 2.5
    elif npfr < upfr and npfr > lpfr:
        b1 = 1.5
    elif npfr > upfr and npfr < lpfr:
        b1 = 1.5
    elif npfr < upfr and npfr < lpfr:
        b1 = 1

    return b1

def b1_sheet_score_system(df):
    df['Tra-AcBa Proportion'] = df['TransactionAmount (TrA)'] / df['AccountBalance (AcBa)']
    df['b1'] = 0

    ui2 = pd.Series(df['Tra-AcBa Proportion'])

    for value in ui2:
        for i in range(1, 100):
            if (value * 1000) < i:
                n_user_code = f'{i - 1} - {i}'
                u_user_code = f'{i} - {i + 1}'
                if i != 1:
                    l_user_code = f'{i - 2} - {i - 1}'
                elif i == 1:
                    l_user_code = f'{i + 1} - {i + 2}'
                break
            else:
                continue

        npf = data0_count[n_user_code]
        ff_npf = data_count[n_user_code]
        npfr = ff_npf / npf

        upf = data0_count[u_user_code]
        ff_upf = data_count[u_user_code]
        upfr = ff_upf / upf

        lpf = data0_count[l_user_code]
        ff_lpf = data_count[l_user_code]
        lpfr = ff_lpf / lpf

        # b1 scoring system

        if npfr > upfr and npfr > lpfr:
            b1 = 2.5
        elif npfr < upfr and npfr > lpfr:
            b1 = 1.5
        elif npfr > upfr and npfr < lpfr:
            b1 = 1.5
        elif npfr < upfr and npfr < lpfr:
            b1 = 1

        df.loc[df['Tra-AcBa Proportion'] == value, 'b1'] = b1
