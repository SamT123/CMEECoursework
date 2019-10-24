""" list comprehension demonstration """

# Average UK Rainfall (mm) for 1910 by month
# http://www.metoffice.gov.uk/climate/uk/datasets
rainfall = (('JAN',111.4),
            ('FEB',126.1),
            ('MAR', 49.9),
            ('APR', 95.3),
            ('MAY', 71.8),
            ('JUN', 70.2),
            ('JUL', 97.1),
            ('AUG',140.2),
            ('SEP', 27.0),
            ('OCT', 89.4),
            ('NOV',128.4),
            ('DEC',142.2),
           )

# (1) Use a list comprehension to create a list of month,rainfall tuples where
# the amount of rain was greater than 100 mm.

greater_hundred_month_fall_lc = [month_fall for month_fall in rainfall if month_fall[1] > 100.0]
 
# (2) Use a list comprehension to create a list of just month names where the
# amount of rain was less than 50 mm. 

less_fifty_month_lc = [month_fall[0] for month_fall in rainfall if month_fall[1] < 50.0]

# (3) Now do (1) and (2) using conventional loops (you can choose to do 
# this before 1 and 2 !). 

greater_hundred_month_fall_loop = []

for month_fall in rainfall:
    if month_fall[1] > 100:
        greater_hundred_month_fall_loop.append(month_fall)

less_fifty_month_loop = []

for month_fall in rainfall:
    if month_fall[1] < 50:
        less_fifty_month_loop.append(month_fall[0])