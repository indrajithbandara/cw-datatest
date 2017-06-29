aa = [[1,2,3], 8,9, [23,[45,78,67]]]

single_list = []

def parse_list(alist):
    if isinstance(alist, list):
        for item in alist:
            parse_list(item)
    else:
        single_list.append(alist)

parse_list(aa)
print "single_list", single_list