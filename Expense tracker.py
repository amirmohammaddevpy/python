from datetime import datetime
import json
import os

def add_expense(price=0,category='None',description='None'):
    time = datetime.now().date()
    f_json = {'Data':str(time),'Price':price ,'Category':category,'Descriptions':description}
    new_data = []
    if os.path.exists('expense_tracker.json'):
        with open('expense_tracker.json','r') as file:
            new_data = json.load(file)
            new_data.append(f_json)
        with open('expense_tracker.json','w') as file:
            json.dump(new_data,file,indent=4)
        return "Updated"
    
    else:
        with open('expense_tracker.json','w') as file:
            json.dump([f_json],file,indent=4)
        return "file is created"

def view_expense():
    if os.path.exists('expense_tracker.json'):
        with open('expense_tracker.json','r') as file:
            read_file = json.load(file)
            for item in read_file:
                print(item,end="\n")
            return "end."
    else:
        return "file is not found"


def search_expense(data=datetime.now().date()):
    if os.path.exists('expense_tracker.json'):
        with open("expense_tracker.json",'r') as file:
            read_file = json.load(file)
            for values in read_file:
                if str(data) in values['Data']:
                    print(values)
            return "end."
    else:
        return 'File is not found!'

def show_total():
    sum_price = 0
    if os.path.exists('expense_tracker.json'):
        with open('expense_tracker.json','r') as file:
            file_json = json.load(file)
            for item in file_json:
                sum_price += item['Price']
        return f"total price: {sum_price}"
    else:
        return "File is not found!"
    
while True:
    print("""
Expense Tracker      
1. Add Expense
2. View Expense
3. Search Expense by data
4. Show total expense
5. Exit
""")
    try:
        choesse = int(input("enter a number:"))
    except ValueError:
        print('error enter number')
        break
    
    if choesse == 1:
        try:
            price = int(input("enter a price:"))
        except ValueError:
            print('error enter number')
            break
        category = input("enter a category:")
        description = input("enter a descriptions:")
        add_expense(price,category,description)
        
    elif choesse == 2:
        print(view_expense())
        
    elif choesse == 3:
        data = input('enter data:')
        print(search_expense(data))
        
    elif choesse == 4:
        print(show_total())
        
    elif choesse == 5:
        break
    
    else:
        print("request invalid")
        break