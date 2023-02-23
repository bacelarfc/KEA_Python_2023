#difference between sets and list: sets can't have repeating values 
#dictionaries: you do not only have the value, but a key value pair 

# /-----------------------------------------------------/

# 1. Model an organisation of employees, management and board of directors in 3 sets.

# Board of directors: Benny, Hans, Tine, Mille, Torben, Troels, Søren

# Management: Tine, Trunte, Rane

# Employees: Niels, Anna, Tine, Ole, Trunte, Bent, Rane, Allan, Stine, Claus, James, Lars

board_of_directors = {'Benny', 'Hans', 'Tine', 'Mille', 'Torben', 'Troels', 'Søren'}
management = {'Tine', 'Trunte', 'Rane'}
employees = {'Niels', 'Anna', 'Tine', 'Ole', 'Trunte', 'Bent', 'Rane', 'Allan', 'Stine', 'Claus', 'James', 'Lars'}

print("Board of directors:", board_of_directors);
print("Management:", management);
print("Employees:", employees);

#     who in the board of directors is not an employee?

not_employees = board_of_directors.difference(employees)
print("Not employees:", not_employees)

#     who in the board of directors is also an employee?

common_elements = board_of_directors.intersection(employees)
print("Both in the board and an employee: ", common_elements);

#     how many of the management is also member of the board?

common_elements_management_board = management.intersection(board_of_directors);
print("Both in management and member of the board: ", common_elements_management_board);

#     All members of the managent also an employee
common_elements_management_employee = management.intersection(employees);
print("All members of the managent that are also an employee", common_elements_management_employee);
#     All members of the management also in the board?

if management & board_of_directors == management:
    print("All members of the management are also in the board of directors.")
else:
    print("Not all members of the management are in the board of directors.")

#     Who is an employee, member of the management, and a member of the board?

common_members = board_of_directors & management & employees
print("Common members:", common_members)

#     Who of the employee is neither a memeber or the board or management?

non_management_or_board_members = employees - board_of_directors - management
print("Employees who are neither members of the board nor management:", non_management_or_board_members)

# /---------------------------------------------/
# 2. Using a list comprehension create a list of tuples from the folowing datastructure

sets = {'a': 'Alpha', 'b': 'Beta', 'g': 'Gamma'}
tuple_list = list(sets.items())
print(tuple_list)

# 3.  From these 2 sets:

set1 = {'a', 'e', 'i', 'o', 'u', 'y'}

set2 = {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}

# Of the 2 sets create a:

# a. Union

union = set1.union(set2);
print("Union", union)

#converted into a list to display the union of sets in order 
union_list = sorted(list(set1.union(set2)))
print(union_list)

# b. Symmetric Difference

# display all elements that are in either of the sets, but not in both

sym_difference = set1.symmetric_difference(set2);
print("Symmetric Difference: ", sym_difference)

# c. Difference

sets_difference = set1.difference(set2);

#in this case is empty because all elements in set1 are also in set2 

#to make it look better:

sets_difference_beautified = set1.difference(set2)
print("Elements only in set 1:", ', '.join(list(sets_difference_beautified)))

# d. Disjoint
# checks whether or not the 2 sets have common elements 

if set1.isdisjoint(set2):
    print("The sets are disjoint")
else:
    print("The sets are not disjoint")

# it returns false, because the sets have common elements 

# /---------------------------------------------------------/

# 4. Date Decoder.

# a. A date of the form 8-MAR-85 includes the name of the month, which must be translated to a number.
from datetime import datetime

date_string = '8-MAR-85'
#%d represents the day, %b represents the abbreviated month name, and %y represents the year (85).
date_obj = datetime.strptime(date_string, '%d-%b-%y')
print("Month: ", date_obj.month) 

# b. Create a dict suitable for decoding month names to numbers.

month_dictionary = {
    'JAN': 1,
    'FEB': 2,
    'MAR': 3,
    'APR': 4,
    'MAY': 5,
    'JUN': 6,
    'JUL': 7,
    'AUG': 8,
    'SEP': 9,
    'OCT': 10,
    'NOV': 11,
    'DEC': 12
}
# c. Create a function which uses string operations to split the date into 3 items using the "-" character.
day, month_name, year = date_string.split('-')
month = month_dictionary[month_name]
print('{}-{}-{}'.format(day, month_name, year))


# d. Translate the month, correct the year to include all of the digits.

if int(year) >= 0 and int(year) <= 20:
    year = '20' + year
else:
    year = '19' + year

print(f'{day}-{month}-{year}')

# The function will accept a date in the "dd-MMM-yy" format and respond with a tuple of ( y , m , d ).

#since I have defined all properties above, I just printed the value, and also checked if I actualy returned a tuple. 
print(year, month, day)

my_tuple = year, month, day;

if isinstance(my_tuple, tuple):
    print(f"{my_tuple} is a tuple")
else:
    print(f"{my_tuple} is not a tuple")