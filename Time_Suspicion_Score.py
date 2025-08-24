import pandas as pd
from tempdata import data

def time_score_system(df):

    grp = data.groupby(['TransactionTime (TrT)'])

    std = grp.size().std()

    ave = grp.size().mean()

    d = grp.size()[df['TransactionTime (TrT)']]
    d = d[df.loc[0]['TransactionTime (TrT)']]
    target_deviation = d - ave

    # Score Awarding System

    # for a1
    reverse = False


    if d >= ave :
        a1 = 2.5
        reverse = False
    else:
        a1 = 0
        reverse = True

    # For a2

    if reverse == False:
        if target_deviation == std:
            a2 = 1.5
        elif target_deviation > std:
            a2 = 2.5
        elif target_deviation < std:
            a2 = 1

    elif reverse == True:
        if target_deviation == std:
            a2 = 1.5
        elif target_deviation > std:
            a2 = 1
        elif target_deviation < std:
            a2 = 2.5

    a = a1 + a2
    return a

def time_sheet_score_system(df):

    grp = data.groupby(['TransactionTime (TrT)'])

    std = grp.size().std()

    ave = grp.size().mean()

    df['a'] = 0

    for value in df['TransactionID (TrID)']:
        
        time = df.loc[df['TransactionID (TrID)'] == value, 'TransactionTime (TrT)']
        time = time[value - 1]
        
        d = grp.size()[time]
        target_deviation = d - ave
        

        # Score Awarding System

        # for a1
        reverse = False


        if d >= ave :
            a1 = 2.5
            reverse = False
        else:
            a1 = 0
            reverse = True

        # For a2

        if reverse == False:
            if target_deviation == std:
                a2 = 1.5
            elif target_deviation > std:
                a2 = 2.5
            elif target_deviation < std:
                a2 = 1

        elif reverse == True:
            if target_deviation == std:
                a2 = 1.5
            elif target_deviation > std:
                a2 = 1
            elif target_deviation < std:
                a2 = 2.5

        a = a1 + a2
        
        df.loc[df['TransactionID (TrID)'] == value, 'a'] = a