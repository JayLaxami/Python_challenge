import os
import csv
csvpath = os.path.join("C:/Users/juhis/Python_challenge/PyBank/", "Resources", "budget_data.csv") 
total_months= 0
net_profit_loss= 0
changes_profit_loss= 0
average_change= 0
max_increase= float('-inf')
max_decrease= float('inf')
month_max_increase= ""
month_max_decrease= ""

print(csvpath)
print(os.getcwd())

with open(csvpath) as csvfile:

    
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    previous_row = next(csvreader)
    if len(previous_row) != 0:
        total_months= total_months + 1
        net_profit_loss= net_profit_loss + int(previous_row[1])
        
    for current_row in csvreader:
        if len(current_row) != 0:
            total_months= total_months + 1
            net_profit_loss= net_profit_loss + int(current_row[1])
            
            change = int(current_row[1]) - int(previous_row[1])
            
            if change > max_increase:
                max_increase = change
                month_max_increase = current_row[0]
                
            if change < max_decrease:
                max_decrease = change
                month_max_decrease = current_row[0]
            
            changes_profit_loss= changes_profit_loss + int(current_row[1]) - int(previous_row[1])
            
        previous_row = current_row
    
    average_change = changes_profit_loss/(total_months-1)
                    
                
    
print(total_months, net_profit_loss, round(average_change,2), max_increase, 
      max_decrease, month_max_increase, month_max_decrease)
output = (
    f"Financial Analysis\n"
    f"...................\n"
    f"Total Months {total_months}\n"
    f"Total ${net_profit_loss}\n"
    f"Average Change ${average_change}\n"
    f"Greatest Increase in Profits: {month_max_increase} (${max_increase})\n"
    f"Greatest Decrease in Profits: {month_max_decrease} (${max_decrease})"
    )
    
output_path= os.path.join("Analysis", "budget_analysis.txt")
with open(output_path, "w") as txt_file:
    txt_file.write(output)
         










   
        
        
        






     