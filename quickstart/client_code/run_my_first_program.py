from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    
    # Secret integers as coefficients and the threshold
    A = SecretInteger(Input(name="A", party=party1))
    B = SecretInteger(Input(name="B", party=party1))
    C = SecretInteger(Input(name="C", party=party1))
    T = SecretInteger(Input(name="T", party=party1))
    
    # Secret integer as the variable x
    x = SecretInteger(Input(name="x", party=party1))
    
    # Compute A * x^2
    x_squared = x * x
    Ax_squared = A * x_squared
    
    # Compute B * x
    Bx = B * x
    
    # Compute the polynomial A*x^2 + B*x + C
    poly_result = Ax_squared + Bx + C
    
    # Compare the result with the threshold T
    is_greater = poly_result > T

    return [
        Output(poly_result, "poly_result", party=party1),
        Output(is_greater, "is_greater", party=party1)
    ]

if __name__ == "__main__":
    nada_main()