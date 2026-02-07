# Syntax2: {key:value for variable in iterable if test}
# This syntax allows adding key and values based on condition or test.


grade_dict={'nk':'A',
            'suresh':'B',
            'ramesh':'A',
            'rajesh':'A',
            'kishore':'B'}
print(grade_dict)
gradeA_dict={name:grade for name,grade in grade_dict.items() if grade=='A' }
print(gradeA_dict)
gradeB_dict={name:grade for name,grade in grade_dict.items() if grade=='B' }
print(gradeB_dict)

sales_dict={2000:45000,
            2001:35000,
            2002:25000,
            2003:22000,
            2004:47000,
            2005:38000,
            2006:65000,
            2007:75000}
# Condition can be made on keys and values both OR any
sales1_dict={year:sales for year,sales in sales_dict.items() if sales<45000}
sales2_dict={year:sales for year,sales in sales_dict.items() if sales>=45000}
print(sales1_dict)
print(sales2_dict)

dict1={num:num**2 for num in range(1,11)}
print(dict1)