#EXCEPTION&DEBUGEXCEPTION&DEBUGEXCEPTION&DEBUGEXCEPTION&DEBUGEXCEPTION&DEBUGEXCEPTION&DEBUGEXCEPTION&DEBUGEXCEPTION&DEBUG
# 1.
try:
    div_zero = int(input())
    div_zero_act = div_zero/0
    print(div_zero)
except:
    print("Something went wrong!")
finally:
    print("Final")

# 2.
div_zero = int(input())
div_zero2 = int(input())
if div_zero2 == 0:
    raise Exception("You can`t divide by zero")
div_zero_act = div_zero/div_zero2
print(int(div_zero_act))