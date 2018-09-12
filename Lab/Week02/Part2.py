# define part2 list, check by printing
part2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]
print (part2)

# define SumList function
def SumList(part2):
    result2 = 0
    for i in part2:
        result2 = result2 + i
    return result2

# test by printing SumList function for part2 list
print (SumList(part2))