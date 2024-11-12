base = 9.19375
int_base = 0.01771
int = input("your int: ")
wanted_stats = input("how many lead you want: ")
acad = input("Is academic training on?: (1/0, where 1 is yes and 0 is no)")
gain_from_int = int_base * float(int)
amt_gained = base + gain_from_int
if acad == 0:
        result = float(wanted_stats)/amt_gained
        print("you'll need approximately: ", str(result), " days or about ", float(result) * 24, " hours")
else:
        acad_total = (amt_gained/100)*110
        acad_results = float(wanted_stats)/acad_total

        print("Youll need approximately: ", str(acad_results), " or approximately ", str(acad_results*24), " hours")