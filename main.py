from gf import gf_mul
from gf import gf_div

if __name__ == '__main__':
    r = gf_mul(7, 5)
    print(bin(r))

    s = gf_div(7, 5)
    print(bin(s))