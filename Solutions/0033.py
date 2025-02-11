from fractions import Fraction

def is_curious_fraction(numerator, denominator):
    num_str = str(numerator)
    den_str = str(denominator)
    
    if '0' in num_str or '0' in den_str:
        return False
    
    for digit in num_str:
        if digit in den_str:
            new_num_str = num_str.replace(digit, '', 1)
            new_den_str = den_str.replace(digit, '', 1)
            if new_den_str != '0' and new_num_str != '' and new_den_str != '':
                new_num = int(new_num_str)
                new_den = int(new_den_str)
                if new_num / new_den == numerator / denominator:
                    return True
    return False

def find_curious_fractions():
    product = Fraction(1, 1)
    for numerator in range(10, 100):
        for denominator in range(numerator + 1, 100):
            if is_curious_fraction(numerator, denominator):
                product *= Fraction(numerator, denominator)
    return product.denominator

if __name__ == "__main__":
    result = find_curious_fractions()
    print(f"The denominator of the product of the four curious fractions in its lowest common terms is {result}")