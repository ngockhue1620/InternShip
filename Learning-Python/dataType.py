# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview

#Example 
str ="My Name is Ngoc Khue"
a_int=3
b_float=3.4
c_complex=5j

d_list =['khue',1,3,5,2.4]
for i in d_list:
    print(i)
type_tuple=("a",1,"c")


for i in type_tuple:
    print(i)
type_range=(4,6)
type_dict={"name":"khue","age":20}
print(type_dict['name'])

type_frozenset=frozenset({"khue",20,"tuoi"})
for i in type_frozenset:
    print(i)

print(d_list*2)
#format number (Python Casting)
format_to_int = int(b_float)
format_to_int_from_string = int(int("3")/3)
print(format_to_int_from_string)

#string , method
#string are  arrays
for i in str:
    print(i)
print("Khue" in str)
#upper case 
print(str.upper())
#lower case
print(str.lower())
# s
