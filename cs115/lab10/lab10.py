'''
Prolog:
	University of Kentucky
        CS115
        Lab 10

Description:
	Takes user input to calculate and return employee paycheck details.

Pre-conditions:
        Takes comma seperated user input of employee ID, hours worked in first week,
	hours worked in second week, and payrate.

Post-conditions:
	Prints table with employees and their paycheck amounts, then total of pay, 
	number of employees processed, and average paycheck amount.
'''

def main():
	
	# list of list of values from user input
	table=[]
	
	# sentinel loop to get user input
	# strips whitespace and adds to list delimited by commas
	print("Enter Employee ID, hours worked in week 1, hours worked in week 2 \
	and payrate separated by commas")
	in_str = input("ID, week 1,  week 2, payrate separated by commas: ")
	while in_str != '':
		in_str = in_str.replace(" ","")
		table_entry = in_str.split(',')
		table.append(table_entry)
		in_str = input("ID, week 1,  week 2, payrate separated by commas: ")

	# list of list of values calculated from table 
	pay_table = []
	
	employees = 0
	total_payroll = 0
	
	# iterates over first table to calculate paychecks and adds to pay_table
	# also increments number of employees and paycheck amount
	for entry in table:
		employees += 1
		paycheck = round((float(entry[1]) + float(entry[2])) * float(entry[3]), 2)
		total_payroll += paycheck
		pay_table.append([entry[0], paycheck])
	
	# calculates mean if any employees are entered
	mean_pay = 0.0
	if employees:
		mean_pay = round(total_payroll / employees, 2)
	
	# prints output
	print("Employee ID \t Check Amount\n")
	for entry in pay_table:
		print(str(entry[0]) + "\t\t" + str(entry[1]))
		
	print()
	print("Total Payroll $" + str(total_payroll))
	print("Number of Employees: " + str(employees))
	print("Average pay check $" + str(mean_pay))
main()
