import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def analysis(df):

    def check_value(headline, high, low):
        value = int(input(headline + ': '))
        if value in range(low, high + 1):
            return value
        else:
            print(f'-- Value out of range ({low}-{high}) -- ', '-- Reinitiating Process --', sep = '\n')
            analysis(df)

    def reask_analysis():
        print('-- Select further proceeding --')
        ask = check_value('''1. Continue Analysis
                          2. Exit Analysis
                          ''', 2, 1)
        if ask == 1:
            analysis(df = df)
        elif ask == 2:
            print('-- Analysis Completed --')
    
    def fraud_analysis(database):
        database['Fraud Estimation (%)'] = database['Score'] * 10

        print('-- The Analyzed Databse is as follows:',database, sep = '\n')

        critical = database.loc[database['Fraud Estimation (%)'] > 80, 'TransactionID (TrID)'].count()
        mild = database.loc[database['Fraud Estimation (%)'] > 30, 'TransactionID (TrID)'].count() - critical

        print(f'''
        The analysis estimates that:
        -- {critical} transaction(s) have a more than 80% chance of being a fraud.
        -- {mild} transaction(s) have a 30 - 80 % chance to be a fraud case.
        ''')

        # Visualization

        enter = input('-- Enter to proceed to visualization: ')

        # Line chart

        database.plot(kind = 'line', x = 'TransactionID (TrID)', y = 'Fraud Estimation (%)', title = 'Fraud Estimation Graph')
        
        # Bar chart
        critical_df = database[database['Fraud Estimation (%)'] >= 80]
        critical_grp = critical_df.groupby('TransactionTime (TrT)').aggregate('count')
        critical_grp.plot(kind = 'bar', y = 'Fraud Estimation (%)', label = 'Critical Chances', title = 'Critical Chances Frequency Graph')

        mild_df = database[database['Fraud Estimation (%)'] < 80][database['Fraud Estimation (%)'] >= 30]
        mild_grp = mild_df.groupby('TransactionTime (TrT)').aggregate('count')
        mild_grp.plot(kind = 'bar', y = 'Fraud Estimation (%)', label = 'Mild Chances', title = 'Mild Chances Frequency Graph')
        plt.show()


    print('-- Initiating Analysis --')
    print('''
    -- Menu
        1. Analyze the entire file
        2. Analyze first n records
        3. Analyze last n records
        4. Analyze specific record
        5. Analyze non - adjacent records
    ''')

    choice = int(input('-- Enter Function Code: '))

    if choice == 1:
        print('-- File Analysis --')

        fraud_analysis(database = df)

        reask_analysis()
        
    elif choice == 2:
        print('-- Analysis of first n records --')

        n = int(input('-- Enter the number of records: '))
        if n > len(list(df.index)):
            print('-- Entered Number of records exceeds the total number of records --')
            reask_analysis()
           
        else:
            df2 = df.head(n)
            fraud_analysis(df2)
            reask_analysis()

    elif choice == 3:
        print('-- Analysis of last n records --')

        n = int(input('-- Enter the number of records: '))
        if n > len(list(df.index)):
            print('-- Entered Number of records exceeds the total number of records --')
            reask_analysis()
  
        else:
            df2 = df.tail(n)
            fraud_analysis(df2)
            reask_analysis()   
        
    elif choice == 4:
        print('-- Analysis of Specific record --')

        record_id = int(input('-- Enter record Transaction ID: '))
        df2 = df[df['TransactionID (TrID)'] == record_id]
        fraud_analysis(df2)

        reask_analysis()
   
    elif choice == 5:
        print('-- Analysis of non-adjacent records --')

        df2 = df.iloc[::2, :]
        fraud_analysis(df2)

        reask_analysis()

