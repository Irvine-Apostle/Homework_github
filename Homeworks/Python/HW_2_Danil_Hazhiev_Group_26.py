import math

item_1 = 3
item_2 = 6

result_sum = item_1 + item_2
print(result_sum)

result_subtr = item_2 - item_1
print(result_subtr)

result_multi = item_1 * item_2
print(result_multi)

result_exp = item_1 ** item_2
print(result_exp)

result_m_exp = math.pow(item_1, item_2)
print(result_m_exp)

result_s_root = item_1 ** 0.5
print(result_s_root)

result_m_s_root = math.sqrt(item_1)
print(result_m_s_root)

result_mp_s_root = math.pow(item_1, 0.5)
print(result_mp_s_root)

item_1_odd = 39
item_2_even = 4

result_division = item_1_odd / item_2_even
print(result_division)

result_m_floor = math.floor(result_division)
print(result_m_floor)

result_m_ceil = math.ceil(result_division)
print(result_m_ceil)

result_int = int(result_division)
print(result_int)

result_no_division_lost = item_1_odd // item_2_even
print(result_no_division_lost)

result_division_lost = item_1_odd % item_2_even
print(result_division_lost)

#========================================

item_3 = 5

item_3 += 10
print(item_3)

item_3 -= 5
print(item_3)

item_3 *= 3
print(item_3)

item_3 /= 2
print(item_3)

item_3 **= 2
print(item_3)

item_3 **= 0.5
print(item_3)

item_3 %= 2
print(item_3)

#===============================================

b_item_t = True
b_item_f = False

b_item_result_sum = b_item_t + b_item_f
print(b_item_result_sum)

b_item_result_subtr = b_item_t - b_item_f
print(b_item_result_subtr)

b_item_result_multi = b_item_t * b_item_f
print(b_item_result_multi)

#b_item_result_division = b_item_t / b_item_f
#print(b_item_result_division)

b_item_1_int = int(b_item_t)
print('b_item_1_int =', b_item_1_int)

b_item_2_int = int(b_item_f)
print('b_item_2_int =', b_item_2_int)



