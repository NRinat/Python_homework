
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

src_list = [numb for n_src, numb in enumerate(src) if numb > src[n_src - 1] and n_src != 0]

print(src_list)


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

print([numb for numb in src if src.count(numb) == 1])
