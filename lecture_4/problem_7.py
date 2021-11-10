x = "1.....9"
occurances = x.count(".")

multi = 0
if occurances > 1 and occurances < 3:
    multi = occurances * 10
elif occurances > 4 and occurances < 6:
    multi = occurances * 100
elif occurances > 7 and occurances < 9:
    multi = occurances * 1000
elif occurances == 0 or occurances > 9:
    print("Error")

if multi != 0:
    print("1" + "."*multi + "9")
