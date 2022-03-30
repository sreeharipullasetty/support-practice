def numOfIds(pool):
    return min(len(pool) // 11, pool.count('8'))

print(numOfIds("8095688777777777776544"))