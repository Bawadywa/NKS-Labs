# 14 Variant

data = [138, 951, 1584, 18, 1533, 3378, 130, 309,
218, 338, 1052, 521, 818, 1095, 68, 1196,
2618, 679, 506, 661, 172, 36, 1437, 700,
190, 4926, 649, 1442, 7, 1177, 927, 1455,
181, 337, 963, 7, 4658, 656, 1889, 1071,
2348, 934, 82, 424, 55, 1458, 124, 180, 461,
201, 329, 299, 864, 277, 636, 1403, 484,
1541, 899, 2432, 1822, 523, 357, 2627, 212,
20, 570, 7255, 916, 692, 755, 2370, 1340,
34, 397, 1074, 67, 445, 1555, 492, 185, 461,
1717, 1365, 1523, 1225, 188, 106, 541, 209,
3118, 779, 442, 1608, 466, 1307, 1006, 298,
143, 312
]

# y = float(input("Input y: "))
y = 0.96
# hours_1, hours_2 = int(input("Input hours_1: ")), int(input("Input hours_2: "))
hours_1, hours_2 = 4206, 6867


t_middle = sum(data) / len(data)
print("\nTср: ", t_middle)

data.sort()
k = 10
h = max(data) / k
intervals = []

for i in range(10):
    intervals.append([h*i, h*(i+1)])

print("Інтервали: ", intervals)
count_in_list = []

data_copy = data[::]
index = 0
for i in range(len(intervals)):
    count_in_list.append(0)
    data_copy = data_copy[index:]
    for j in range(len(data_copy)):
        if intervals[i][0] <= data_copy[j] <= intervals[i][1]:
            count_in_list[i] += 1
        else:
            index = j
            break


f_list = [count / (len(data) * h) for count in count_in_list]
print("Список f: ", f_list)
S_list = [f * h for f in f_list]

P_list = [1 - (sum(S_list[:i])) for i in range(len(f_list) + 1)]
print("Список P: ", P_list)
index = 0
for i in range(1, len(P_list)):
    if P_list[i-1] >= y >= P_list[i]:
        index = i - 1
        break


d = (P_list[index + 1] - y) / (P_list[index + 1] - P_list[index])

Ty = intervals[index][1] - h * d
print("Ty: ", Ty)


def find_P_F(t):
    value, index = 0, 0
    for interval in intervals:
        if interval[0] <= t <= interval[1]:
            value = interval[0]
            break
        index += 1

    P, F = 1, 0
    for i in range(len(f_list)):
        if i != index:
            P -= f_list[i] * h
        else:
            F = f_list[i]
            P -= f_list[i] * (t - value)
            break

    return P, F


def find_lambda(t):
    P, F = find_P_F(t)
    return F/P


P, F = find_P_F(hours_1)

lambda_t = find_lambda(hours_2)

print("Ймовірність безвідмовної роботи: {}\nІнтенсивність відмов: {}".format(P, lambda_t))

