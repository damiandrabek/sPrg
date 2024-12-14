import re

pattern = "^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z0]{2,}$"

string = "john.doe@example.com"

# Check if the string matches the pattern
res = re.match(pattern, string)

print(res)

if res:
  True