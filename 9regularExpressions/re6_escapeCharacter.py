import re
str='We just received $10.00 for cookies' #we want to extract amount from str
amount=re.findall('\$[0-9.]+',str)
print(amount)

#here we match a dollar sign as \$ which means matching starts with $ sign.
#so we have other ways to indicate beginning other then caret sign ^

#Since we prefix the dollar sign with a backslash, it actually matches the dollar
# sign in the input string instead of matching the “end of line”, and the rest of
# the regular expression matches one or more digits or the period character. Note:
# Inside square brackets, characters are not “special”.
#the dot or period inside square bracket called period
#outside it is a wild card means any character