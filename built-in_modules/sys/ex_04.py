import sys

# my solution, but it is wrong because it is not universal and
# return error: list index out of range

# res = []
#
# for arg in sys.argv[1:]:
#     res.append(arg)
#
# print(int(res[0]) + int(res[1]))

if len(sys.argv) > 2:
    res = int(sys.argv[1]) + int(sys.argv[2])
    print(res)
