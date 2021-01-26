# Assigning elements to different lists

langs = []
langs.append("Python")
langs.append("Perl")
langs.extend(("JavaScript", "ActionScript"))
print(langs)

#OUTPUT
['Python', 'Perl', 'JavaScript', 'ActionScript']

#################################################################################

# Accessing elements from Tuple

tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );
print "tup1[0]: ", tup1[0];
print "tup2[1:5]: ", tup2[1:5];

#OUTPUT
tup1[0]:  physics
tup2[1:5]:  [2, 3, 4, 5]


#################################################################################

# DELETING Different Dictionary Elements 

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

del dict['Name']   # remove entry with key 'Name'
print(dict) 
#OUTPUT
{'Age': 7, 'Class': 'First'}

dict.clear()   # remove all entries in dict
print(dict)
#OUTPUT
{}
