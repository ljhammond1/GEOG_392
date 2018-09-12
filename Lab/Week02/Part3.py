# define part3 list and test by printing
part3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21]
print (part3) 

# define SumListEvens
def SumListEvens(part3):
    result3 = 0
    for i in part3:
        if i % 2 == 0:
            result3 = result3 + i
    return result3

print (SumListEvens(part3))