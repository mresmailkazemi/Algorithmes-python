def zero(seq):
    result=[]
    zeroes=0
    for i in seq:
        if i ==0 and type(i)!= bool:
            zeroes +=1
        else:
            result.append(i)

    result.extend([0] * zeroes)
    return result

print(zero([False,1,3,0,5,8,"a",0,4,"b"]))