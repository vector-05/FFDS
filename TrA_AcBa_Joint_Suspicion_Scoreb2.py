import pandas as pd
from tempdata import prc1_0_count, prc1_count, prc2_0_count, prc2_count, prc3_0_count, prc3_count, prc4_0_count, prc4_count

# User Input (ui) Handling

def b2_score_system(df):
    df['Tra-AcBa Proportion'] = df['TransactionAmount (TrA)'] / df['AccountBalance (AcBa)']

    user_category = df['TransactionCategory (TrC)'][0]

    ui2 = pd.Series(df['Tra-AcBa Proportion'])

    # User Codes
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

    if user_category == 'PRC 1':
        npf = prc1_0_count[n_user_code]
        ff_npf = prc1_count[n_user_code]
        npfr = ff_npf / npf

        upf = prc1_0_count[u_user_code]
        ff_upf = prc1_count[u_user_code]
        upfr = ff_upf / upf

        lpf = prc1_0_count[l_user_code]
        ff_lpf = prc1_count[l_user_code]
        lpfr = ff_lpf / lpf
    elif user_category == 'PRC 2':
        npf = prc2_0_count[n_user_code]
        ff_npf = prc2_count[n_user_code]
        npfr = ff_npf / npf

        upf = prc2_0_count[u_user_code]
        ff_upf = prc2_count[u_user_code]
        upfr = ff_upf / upf

        lpf = prc2_0_count[l_user_code]
        ff_lpf = prc2_count[l_user_code]
        lpfr = ff_lpf / lpf
    elif user_category == 'PRC 3':
        npf = prc3_0_count[n_user_code]
        ff_npf = prc3_count[n_user_code]
        npfr = ff_npf / npf

        upf = prc3_0_count[u_user_code]
        ff_upf = prc3_count[u_user_code]
        upfr = ff_upf / upf

        lpf = prc3_0_count[l_user_code]
        ff_lpf = prc3_count[l_user_code]
        lpfr = ff_lpf / lpf
    elif user_category == 'PRC 4':
        npf = prc4_0_count[n_user_code]
        ff_npf = prc4_count[n_user_code]
        npfr = ff_npf / npf

        upf = prc4_0_count[u_user_code]
        ff_upf = prc4_count[u_user_code]
        upfr = ff_upf / upf

        lpf = prc4_0_count[l_user_code]
        ff_lpf = prc4_count[l_user_code]
        lpfr = ff_lpf / lpf
    else:
        raise KeyError

    # b1 scoring system

    if npfr > upfr and npfr > lpfr:
        b2 = 2.5
    elif npfr < upfr and npfr > lpfr:
        b2 = 1.5
    elif npfr > upfr and npfr < lpfr:
        b2 = 1.5
    elif npfr < upfr and npfr < lpfr:
        b2 = 1

    return b2

def b2_sheet_score_system(df):
    df['Tra-AcBa Proportion'] = df['TransactionAmount (TrA)'] / df['AccountBalance (AcBa)']
    df['b2'] = 0

    ui2 = pd.Series(df['TransactionID (TrID)'])

    # User Codes
    for id in ui2: #---
        value = df.loc[df['TransactionID (TrID)'] == id, 'Tra-AcBa Proportion'][id - 1]
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
        
        user_category = df.loc[df['TransactionID (TrID)'] == id, 'TransactionCategory (TrC)'][id - 1]

        if user_category == 'PRC 1':
            npf = prc1_0_count[n_user_code]
            ff_npf = prc1_count[n_user_code]
            npfr = ff_npf / npf

            upf = prc1_0_count[u_user_code]
            ff_upf = prc1_count[u_user_code]
            upfr = ff_upf / upf

            lpf = prc1_0_count[l_user_code]
            ff_lpf = prc1_count[l_user_code]
            lpfr = ff_lpf / lpf
        elif user_category == 'PRC 2':
            npf = prc2_0_count[n_user_code]
            ff_npf = prc2_count[n_user_code]
            npfr = ff_npf / npf

            upf = prc2_0_count[u_user_code]
            ff_upf = prc2_count[u_user_code]
            upfr = ff_upf / upf

            lpf = prc2_0_count[l_user_code]
            ff_lpf = prc2_count[l_user_code]
            lpfr = ff_lpf / lpf
        elif user_category == 'PRC 3':
            npf = prc3_0_count[n_user_code]
            ff_npf = prc3_count[n_user_code]
            npfr = ff_npf / npf

            upf = prc3_0_count[u_user_code]
            ff_upf = prc3_count[u_user_code]
            upfr = ff_upf / upf

            lpf = prc3_0_count[l_user_code]
            ff_lpf = prc3_count[l_user_code]
            lpfr = ff_lpf / lpf
        elif user_category == 'PRC 4':
            npf = prc4_0_count[n_user_code]
            ff_npf = prc4_count[n_user_code]
            npfr = ff_npf / npf

            upf = prc4_0_count[u_user_code]
            ff_upf = prc4_count[u_user_code]
            upfr = ff_upf / upf

            lpf = prc4_0_count[l_user_code]
            ff_lpf = prc4_count[l_user_code]
            lpfr = ff_lpf / lpf
        else:
            raise KeyError

        # b1 scoring system

        if npfr > upfr and npfr > lpfr:
            b2 = 2.5
        elif npfr < upfr and npfr > lpfr:
            b2 = 1.5
        elif npfr > upfr and npfr < lpfr:
            b2 = 1.5
        elif npfr < upfr and npfr < lpfr:
            b2 = 1

        df.loc[df['TransactionID (TrID)'] == id, 'b2'] = b2
        