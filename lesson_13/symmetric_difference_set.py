A = {1, 2, 3}
B = {2, 3, 4}

sym_diff_set = A.symmetric_difference(B)
print(sym_diff_set)  # {1, 4}

sym_diff_set_op = A ^ B
print(sym_diff_set_op)  # {1, 4}