def pay(bill, percentage, people):
    '''
    Percentage to give + bill on peoples persons
    '''
    return (bill * (percentage / 100) + bill) / people

print('Welcome to the tip calculator.')
bill = float(input('What is the total bill? $'))
percentage = int(input('What percentage tip would you like to give? 10, 12 or 15? %'))
while percentage != 10 and percentage != 12 and percentage != 15:
    percentage = int(input('What percentage tip would you like to give? 10, 12 or 15? %'))
people = int(input('How mant people to split the bill? '))
print(round(pay(bill, percentage, people), 2))
