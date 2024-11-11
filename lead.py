base = 9.19375
int_base = 0.01771
int = input("your int: ")
wanted_stats = input("how many lead you want: ")
gain_from_int = int_base * float(int)
amt_gained = base + gain_from_int
result = float(wanted_stats)/amt_gained
print("you'll need approximately: ", str(result), " days or about ", float(result) * 24, " hours")
