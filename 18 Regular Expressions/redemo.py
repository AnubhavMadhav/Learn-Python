import re

str = "Take up one idea.One idea at a time"
# Now, we want a sub-string which has it's first letter as 'o' and is followed by any 2 characters
result = re.search(r'o\w\w',str)            # 'str' is the string in which we want to search for the substring
print(result.group())
