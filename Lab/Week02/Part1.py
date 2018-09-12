# define part1 list, test by printing
part1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
print (part1)

# define MultiplyList
def MultiplyList(part1):
    result1 = 1
    for i in part1:
        result1 = result1 * i
    return result1 

# test by printing multiplyList for part1 list
print (MultiplyList(part1))
# should return 302231454903657293676544