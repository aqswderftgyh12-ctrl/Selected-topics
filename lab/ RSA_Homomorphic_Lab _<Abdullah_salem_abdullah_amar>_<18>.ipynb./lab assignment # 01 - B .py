

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def choose_e(phi):
    candidates = [e for e in range(3, phi) if gcd(e, phi) == 1]

    if not candidates:
        return None
    else:
        return candidates[0]


if __name__ == "__main__":
    
    p = 11
    q = 17

    
    n = p * q
    phi = (p - 1) * (q - 1)

    
    e = choose_e(phi)  

    if e is None:
        raise ValueError("No suitable value was found for e")

    
    d = pow(e,-1,phi)
    
    public_key = (e, n)
    private_key = (d, n)

    print("e : ", e)
    print("d : ", d)
    print("public_key : ", public_key)
    print("private_key : ", private_key)

# ----------------------- encrypt and decrypt ----------------------------------------------- - -
    messages = [9, 12]

    print("\n messages :", messages)

    #encrypt
    encrypted_messages = [pow(m, e, n) for m in messages]
    print("encrypted_messages:", encrypted_messages)

    # decrypt
    decrypted_messages = [pow(c, d, n) for c in encrypted_messages]
    print("decrypted_messages : ", decrypted_messages)

# ---------------------- Demonstrate  -----------------------------------
    m1 = 9 
    m2 = 12

    def E(m):
        return pow(m, e, n)

    left = (E(m1) * E(m2)) 
    right = E((m1 * m2) )
 
    print(left)
    print(right)