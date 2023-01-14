import os
import csv

#Find the path of csv file
csvpath = os.path.join("C:/Users/juhis/Python_challenge/PyBank/", "Resources", "budget_data.csv") 

#Assigning variable to output required
total_months= 0
net_profit_loss= 0
changes_profit_loss= 0
average_change= 0
#Assign float(infinite) variable to max increase and decrease 
max_increase= float('-inf')
max_decrease= float('inf')
month_max_increase= ""
month_max_decrease= ""

print(csvpath)
print(os.getcwd())

#Read and open csv file with header
with open(csvpath) as csvfile:

    
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
#Finding previous row by using next to start the loop.   
    
    previous_row = next(csvreader)
    
#Condition for previous row (previous row is not equal to zero). Finding total months and net value 
    if len(previous_row) != 0:
        total_months= total_months + 1
        net_profit_loss= net_profit_loss + int(previous_row[1])

#Condition for current row       
    for current_row in csvreader:
        if len(current_row) != 0:
            total_months= total_months + 1
            net_profit_loss= net_profit_loss + int(current_row[1])
     
#Change is difference of current and previous       
            change = int(current_row[1]) - int(previous_row[1])

#Condition for finding out maximum values             
            if change > max_increase:
                max_increase = change
                month_max_increase = current_row[0]
                
            if change < max_decrease:
                max_decrease = change
                month_max_decrease = current_row[0]
            
            changes_profit_loss= changes_profit_loss + int(current_row[1]) - int(previous_row[1])
            
        previous_row = current_row
        
#average is division of change and total of change months(which is one less than total month)   
    average_change = changes_profit_loss/(total_months-1)
                    
                
#Printing out result and rounding of average change by 2    
print(total_months, net_profit_loss, round(average_change,2), max_increase, 
      max_decrease, month_max_increase, month_max_decrease)

#Output for the text file
output = (
    f"Financial Analysis\n"
    f"...................\n"
    f"Total Months {total_months}\n"
    f"Total ${net_profit_loss}\n"
    f"Average Change ${round(average_change,2)}\n"
    f"Greatest Increase in Profits: {month_max_increase} (${max_increase})\n"
    f"Greatest Decrease in Profits: {month_max_decrease} (${max_decrease})"
    )

#Write the output as text file in Analysis folder 
output_path= os.path.join("Analysis", "budget_analysis.txt")
with open(output_path, "w") as txt_file:
    txt_file.write(output)
         










   
        
        
        






     