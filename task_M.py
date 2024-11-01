import itertools as it

n = int(input())
lst = [' '.join(map(str,i)) for i in it.permutations(range(1,n+1),r=n)]
print(*lst,sep='\n')