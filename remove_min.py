def remove_min(stack):
    result=[]
    if len(stack)==0:
        return stack

    min=stack.pop()
    stack.append(min)
    for i in range(len(stack)):
        val=stack.pop()
        if val <= min:
            min=val
        result.append(val)

    for i in range(len(result)):
        if result[i] != min:
            stack.append(result[i])
    return stack,min

