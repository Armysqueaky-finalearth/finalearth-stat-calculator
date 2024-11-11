base = 8.28793
int_base = 0.0154335
int = input("your int: ")
wanted_stats = input("how many comms you want: ")
gain_from_int = int_base * float(int)
amt_gained = base + gain_from_int
result = float(wanted_stats)/amt_gained
print("you'll need approximately: ", str(result), " days or about ", float(result) * 24, " hours")
