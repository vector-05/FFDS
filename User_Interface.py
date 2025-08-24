import pandas as pd
from TrA_AcBa_Joint_Suspicion_Score import b1_score_system, b1_sheet_score_system
from TrA_AcBa_Joint_Suspicion_Scoreb2 import b2_score_system, b2_sheet_score_system
from Time_Suspicion_Score import time_score_system, time_sheet_score_system
from data_manipulation import manipulation
from data_analysis import analysis
import sys
        
def check_value(headline, high, low):
    value = int(input(headline + ': '))
    if value in range(low, high + 1):
        return value
    else:
        print('-- Invalid Input -- ', '-- Reinitiating System --',sep = '\n')
        main()

def main():

    individual_input = False
    sheet_input = False

    print('''Select the action to be performed
            1. Individual Query
            2. CSV Query
            3. Exit
            ''')
    user_input = int(input('-- Select the action to be performed: '))
    if user_input == 1:
        individual_input = True
    elif user_input == 2:
        sheet_input = True
    elif user_input == 3:
        print('-- Exiting the system --')
        sys.exit(0)
    else:
        print('-- Invalid Input --')
        main()

    if individual_input == True:
        tr_id = int(input('Enter Transaction ID: '))
        tr_a = check_value('Enter Transaction Amount (1 - 100)', 100, 1)
        ac_ba = check_value('Enter Account Balance (Before Transaction) (1000 - 10000)', 10000, 1000)
        tr_c = input('Enter Transaction Category: ')
        tr_t = check_value('Enter Transaction Time', 24, 1)

        ui = pd.DataFrame({
            'TransactionID (TrID)': tr_id,
            'TransactionAmount (TrA)': tr_a,
            'AccountBalance (AcBa)': ac_ba,
            'TransactionCategory (TrC)': tr_c,
            'TransactionTime (TrT)': tr_t,
            'Fraud' : None
        }, index = [0])

        b1 = b1_score_system(ui)
        b2 = b2_score_system(ui)
        a = time_score_system(ui)
        b = b1 + b2

        print(f'''
        The System estimates that the following transaction has a {(a + b )* 10}% chance of being a fraud. The accredetation is as follow:
        -- Estimation based on Transaction Time -- {a * 20}%
        -- Estimation based on Fraud Frequency in correspondence to the transaction -- {b * 20}%
        ''')
        
        ask = int(input('-- Re-Authorize the System (1) -- Exit (0): '))
        if ask == 1:
            main()
        elif ask == 0:
            print('-- Exiting Individual Query Service --')
            main()

    elif sheet_input == True:
        file_path = input('Enter CSV file path: ')
        ui = pd.read_csv(file_path)
        
        def sheet_analysis():
            def new():
                ask0 = int(input('-- Continue Sheet Analysis (1) -- Exit (0): '))
                if ask0 == 1:
                    sheet_analysis()
                else:
                    print('-- Exiting Sheet Analysis Service --')
                    main()

            print('-- Processing File --')
            print('-- Choose the function to be performed --')

            print('''
                    1. Manipulate the file.
                    2. Analyse the file.
                    3. Exit
                  ''')
            func = int(input('''-- Enter the choice: '''))
            
            if func == 1:
                manipulation(ui)
                new()

            elif func == 2:
                time_sheet_score_system(ui)
                b1_sheet_score_system(ui)
                b2_sheet_score_system(ui)
                ui['Score'] = ui['a'] + ui['b1'] + ui['b2']

                analysis(ui)
                new()
            elif func == 3:
                print('-- Exiting Sheet Analysis Service --')
                main()

            else:
                print('-- Invalid Input --', '-- Reinitiating the system --', sep = '/n')
            sheet_analysis()

        sheet_analysis()

        ask = int(input('-- Re-Authorize the System (1) -- Exit (0): '))
        if ask == 1:
            main()
        elif ask == 0:
            print('-- Thank You for using this service --')
            print('-- Shutting down service --')
            sys.exit(0)

        
            
        
if __name__ == "__main__":
    main()