import bisect

l = [i for i in range(10)]
'''target = -1
print('For list ', l, ' and target ', target, 'value >= target is ', bisect.bisect_left(l, target))

target = 5
print('For list ', l, ' and target ', target, 'value >= target is ', bisect.bisect_left(l, target))

target = 100
print('For list ', l, ' and target ', target, 'value >= target is ', bisect.bisect_left(l, target))
'''
l.pop(2)
target = 2
print('For list ', l, 'value ', bisect.bisect_left(l, target), ' >= target is ', target)
