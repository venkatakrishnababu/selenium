# import re
# with open('source1.txt','r') as R,open('Target3.txt','w') as W:
#     b=R.readlines()
#     p='[a-zA-Z0-9_%+-]+[@][a-z]+[.]com$'
#     for i in b:
#         c=i.strip()
#         if re.findall(p,c):
#             W.write(c+"\n")

####re.sub:-
# text = "My phone number is 9876543210."
# pattern = "[A-Za-z]"
# pattern_1="[0-9]"
# replacement = "X"
# new_text = re.sub(pattern,replacement,text)
# new_text1 = re.sub(pattern_1,replacement,text)
# print(new_text)
# print(new_text1)

### Search
## it will search for the substring if exist it will be true
import re
text = "Python is an programming language."
pattern = "programm"
match = re.search(pattern, text)
if match:
    print("Match found")
else:
    print("No match found")

