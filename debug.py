# n, m = list(map(int, input().split()))
#
# list_1 = list(map(int, input().split()))
# list_2 = list(map(int, input().split()))
#
# common = list_1 + list_2
# final = []
# while len(common) > 0:
# 	final.append(min(common))
# 	common.remove(min(common))
#
# print(*final)

# -------------------------------------------
# n = int(input())
# boys_input = list(map(int, input().split()))
# m = int(input())
# girls_input = list(map(int, input().split()))
#
# boys = sorted(boys_input)
# girls = sorted((girls_input))
#
# i = 0
# j = 0
# count = 0
# while i < n and j < m:
# 	if abs(boys[i] - girls[j]) <=1:
# 		count += 1
# 		i += 1
# 		j += 1
# 	elif boys[i] < girls[j]:
# 		i += 1
# 	else:
# 		j += 1
#
# print(count)

# -------------------------------------------