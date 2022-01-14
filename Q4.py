def solution(k, a, b):
    lenli = len(a)-1 #length of list
    ia = 0 #index of a
    ib = 0 #index of b
    flag = 0 #number of swiches
    a.sort()
    b.sort(reverse=True) #for goal, list b descending
    while flag < k and ia < lenli and ib < lenli:
        if(a[ia]<=b[ib]) : 
            a[ia] = b[ib]
            ia +=1
            ib +=1
            flag += 1
        else : ib +=1
    answer = sum(a)
    return answer

k = 3
a = [1,2,5,4,3]
b = [5,5,6,6,5]
answer = solution(k, a, b)
print(answer)
