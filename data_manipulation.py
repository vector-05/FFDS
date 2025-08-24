import pandas as pd

def manipulation(df):

    def check_value(headline, high, low):
        value = int(input(headline + ': '))
        if value in range(low, high + 1):
            return value
        else:
            print(f'-- Value out of range ({low}-{high}) -- ', '-- Reinitiating Process --', sep = '\n')
            manipulation(df)  
    
    def reask_manipulation():
        print('-- Select further proceeding --')
        ask = check_value('''1. Continue Manipulation
                          2. Exit Manipulation
                          ''', 2, 1)
        if ask == 1:
            manipulation(df=df)
        elif ask == 2:
            print('-- Manipulation Completed --')
    

    print('-- Initiating Manipulation --')
    print('''
    -- Menu
        1. Add record
        2. Add field
        3. Delete record
        4. Delete Column
        5. Modify record
        6. Modify field
        7. Modify value
    ''')

    choice = int(input('-- Enter function code: '))

    if choice == 1:
        record_labels = []
        for i in list(df.columns):
            if i == 'TransactionAmount (TrA)':
                record_value = check_value(f'Enter value for {i} column: ', 100, 1)
                record_labels.append(record_value)
            elif i == 'AccountBalance (AcBa)':
                record_value = check_value(f'Enter value for {i} column: ', 10000, 1000)
                record_labels.append(record_value)
            elif i == 'TransactionTime (TrT)':
                record_value = check_value(f'Enter value for {i} column: ', 24, 1)
                record_labels.append(record_value)
            elif i == 'TransactionCategory (TrC)':
                record_value = input(f'Enter value for {i} column: ')
                if record_value not in ['PRC 1', 'PRC 2', 'PRC 3', 'PRC 4']:
                    print(f'-- Invalid {i} --', '-- Reinitiating Process --', sep = '\n')
                    manipulation(df)
            else:
                record_value = input(f'Enter value for {i} column: ')

        df.loc[len(df.index)] = record_labels
        print(' -- Updation Successful --',' -- Printing File --', df, sep = '\n')
        reask_manipulation()

    elif choice == 2:
        field_labels = []
        field_name = input('-- Enter new field name: ')
        for i in list(df.index):
            field_value = input(f'-- Enter field value for Transaction ID {i + 1}: ')
            field_labels.append(field_value)
        
        df[field_name] = field_labels

        print(' -- Updation Successful --',' -- Printing File --', df, sep = '\n')    
        reask_manipulation()  
    
    elif choice == 3:
        tr_id = int(input('-- Enter Transaction ID of record to be deleted: '))

        df.drop(tr_id - 1, axis = 0, inplace = True)

        print(' -- Updation Successful --',' -- Printing File --', df, sep = '\n') 
        reask_manipulation()

    elif choice == 4:
        field_name = input('-- Enter name of field to be deleted: ')
        if field_name in ['TransactionID (TrID)','TransactionAmount (TrA)','AccountBalance (AcBa)','TransactionCategory (TrC)','TransactionTime (TrT)','Fraud','Tra-AcBa Proportion']:
            print('-- Essential Fields cannot be deleted --', '-- System will exit --', sep = '\n')
            manipulation(df)
        else:
            df.drop(field_name, axis = 1, inplace = True)
            print(' -- Updation Successful --',' -- Printing File --', df, sep = '\n') 
            reask_manipulation()

    elif choice == 5:
        tr_id = int(input('-- Enter Transaction ID of record to be updated: '))
        record_labels = []
        for i in list(df.columns):
            if i == 'TransactionAmount (TrA)':
                record_value = check_value(f'Enter value for {i} column: ', 100, 1)
                record_labels.append(record_value)
            elif i == 'AccountBalance (AcBa)':
                record_value = check_value(f'Enter value for {i} column: ', 10000, 1000)
                record_labels.append(record_value)
            elif i == 'TransactionTime (TrT)':
                record_value = check_value(f'Enter value for {i} column: ', 24, 1)
                record_labels.append(record_value)
            elif i == 'TransactionCategory (TrC)':
                record_value = input(f'Enter value for {i} column: ')
                if record_value not in ['PRC 1', 'PRC 2', 'PRC 3', 'PRC 4']:
                    print(f'-- Invalid {i} --', '-- Reinitiating Process --', sep = '\n')
                    manipulation(df)
            else:
                record_value = input(f'Enter value for {i} column: ')
        
        df.loc[tr_id - 1] = record_labels

        print(' -- Updation Successful --',' -- Printing File --', df, sep = '\n') 
        reask_manipulation()

    elif choice == 6:
        field_name = input('-- Enter name of field to be updated: ')
        field_labels = []
        for i in list(df.index):
            field_value = input(f'-- Enter field value for Transaction ID {i + 1} for field {field_name}: ')
            field_labels.append(field_value)

        df[field_name] = field_labels

        print(' -- Updation Successful --',' -- Printing File --', df, sep = '\n')
        reask_manipulation()
    
    elif choice == 7:
        field_name = input('-- Enter name of field of value to be updated: ')
        tr_id = int(input('-- Enter Transaction ID of record of value to be updated: '))
        if field_name == 'TransactionAmount (TrA)':
                new_value = check_value(f'Enter value for {field_name} column: ', 100, 1)
        elif field_name == 'AccountBalance (AcBa)':
            new_value = check_value(f'Enter value for {field_name} column: ', 10000, 1000)
        elif field_name == 'TransactionTime (TrT)':
            new_value = check_value(f'Enter value for {field_name} column: ', 24, 1)
        elif field_name == 'TransactionCategory (TrC)':
            new_value = input(f'Enter value for {field_name} column: ')
            if new_value not in ['PRC 1', 'PRC 2', 'PRC 3', 'PRC 4']:
                print(f'-- Invalid {field_name} --', '-- Reinitiating Process --', sep = '\n')
                manipulation(df)
        else:
            new_value = input('-- Enter new value: ')

        df.loc[tr_id - 1, field_name] = new_value

        print(' -- Updation Successful --',' -- Printing File --', df, sep = '\n')
        reask_manipulation()
        
            

