import json
from django.shortcuts import render
from datetime import datetime
import os
from django.conf import settings

def process_ledger(ledger_data):
    # Remove duplicates by activity_id
    unique_transactions = {}
    for transaction in ledger_data:
        activity_id = transaction['activity_id']
        if activity_id not in unique_transactions:
            unique_transactions[activity_id] = transaction

    # Sort transactions by date
    sorted_transactions = sorted(unique_transactions.values(), 
                                 key=lambda x: datetime.strptime(x['date'][:19], "%Y-%m-%dT%H:%M:%S"))

    current_balance = 0
    processed_data = []
    for transaction in sorted_transactions:
        date = datetime.strptime(transaction['date'][:19], "%Y-%m-%dT%H:%M:%S")
        date_str = date.strftime('%Y-%m-%d %H:%M:%S')
        source_description = transaction.get('source', {}).get('description', 'Unknown source')
        destination_description = transaction.get('destination', {}).get('description', 'Unknown destination')

        # Construct the description based on the transaction type
        description = "Transaction"
        if transaction['type'] == 'DEPOSIT':
            description = "Deposit from {}".format(source_description)
        elif transaction['type'] == 'INVESTMENT':
            description = "Investment for {}".format(destination_description)
        elif transaction['type'] == 'REFUND':
            description = "Refund from {}".format(source_description)
        elif transaction['type'] == 'TRANSFER':
            if transaction['amount'] > 0:
                description = "Transfer from {}".format(source_description)
            else:
                description = "Transfer to {}".format(destination_description)
        elif transaction['type'] == 'WITHDRAWAL':
            description = "Withdrawal to {}".format(destination_description)

        current_balance += transaction['amount']

        transaction_dict = {
            'activity_id': transaction['activity_id'],
            'date': date_str,
            'type': transaction['type'],
            'amount': transaction['amount'],
            'description': description,
            'balance': current_balance
        }
        processed_data.append(transaction_dict)

    return processed_data, current_balance

def ledger_view(request):
    data_file = os.path.join(settings.BASE_DIR, 'ledger_app/data/simple_ledger.json')
    
    with open(data_file, 'r') as file:
        ledger_data = json.load(file)
    
    processed_data, current_balance = process_ledger(ledger_data)
    
    return render(request, 'ledger.html', {'ledger_data': processed_data, 'current_balance': current_balance})
