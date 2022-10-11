import numpy as np
# Function manipulates input to desired output.
def i2o(seq):
    # Initializing output.
    out = []
    # calculating product of input elements.
    product = np.prod(seq)
    # Check if the product is zero.
    if product != 0:
        for a in seq:
            # Output formation.
            out.append(product/a)
    else:
        # Calculating 0 eleminated product.
        product = 1
        for a in seq:
            if a != 0:
                product *= a
        # Output formation.
        out = list(np.zeros(n))
        for i in range(n):
            if seq[i] == 0:
                out[i] = product
    print(out)
# Taking user input.
try:
    n = int(input("Enter no. of elements: "))
    seq = []
    for i in range(n):
        seq.append(float(input("Enter the element: ")))
    i2o(seq)
except:
    print("Invalid entry.")