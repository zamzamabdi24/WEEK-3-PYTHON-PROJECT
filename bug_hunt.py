# bug_hunt.py

count = 1
total = 0

# BUG: Missing colon (:) at the end of the while statement.
# FIX: Added ':' after 'while count < 5'.
# BUG: Condition 'count < 5' stops at 4, so 5 is never added (logic bug).
#      This bug causes a wrong answer but no error message.
# FIX: Changed 'while count < 5' to 'while count <= 5'.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Trying to concatenate a string with an integer (total) directly.
# FIX: Convert total to string using str(total).
print("Sum of 1 to 5 is: " + str(total))