def pow_mod(B, E, M):
    if E == 0:
        return 1
    elif E == 1:
        return B % M
    else:
        root = pow_mod(B, E // 2, M)
        if E % 2 == 0:
            return (root * root) % M
        else:
            return (root * root * B) % M

M = 115792089237316195423570985008687907853269984665640564039457584007908834671663
E = 96514807760119017459957299373576180339312098253841362800539826362414936958669

print(pow_mod(2, E, M))
print(pow(2, E, M))
