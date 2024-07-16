def classic_multiplication(num1, num2):
    n, m = len(num1), len(num2)
    result = [0] * (n + m + 1)  

    for i in range(n):
        for j in range(m):
            result[i + j] += num1[n - 1 - i] * num2[m - 1 - j]
            result[i + j + 1] += result[i + j] // 10
            result[i + j] %= 10

    while len(result) > 1 and result[-1] == 0:
        result.pop()

    return result[::-1]

def operator_add(num1, num2):
    result_size = max(len(num1), len(num2))
    result = [0] * (result_size + 1)
    carry = 0

    for i in range(result_size):
        num1_digit = num1[-(i + 1)] if i < len(num1) else 0
        num2_digit = num2[-(i + 1)] if i < len(num2) else 0

        _sum = carry + num1_digit + num2_digit
        result[-(i + 1)] = _sum % 10
        carry = _sum // 10

    result[0] = carry

    # Remove leading zeros
    while len(result) > 1 and result[0] == 0:
        result.pop(0)

    return result



def dq_prod(u, v, threshold):
    n = max(len(u), len(v))

    if n <= threshold:
        return classic_multiplication(u, v)
    
    else:
        m = n // 2

        x = u[:m]
        y = u[m:]
        w = v[:m]
        z = v[m:]

        p1 = dq_prod(x, w, threshold)
        p2 = dq_prod(y, z, threshold)
        p3 = dq_prod(x, z, threshold)
        p4 = dq_prod(w, y ,threshold)
        p5 = operator_add(p3, p4)

        p1 = p1 + [0] * (2 * m)
        p5 =  p5 + [0] * m 

        result = operator_add(operator_add(p1, p5), p2)
        return result



def main():

        num1 = [1,2,3,4]
        print("num 1:", num1)

        num2 = [3,2,1,3]
        print("num 2:", num2)

        classic_result = classic_multiplication(num1, num2)
        dq_result = dq_prod(num1, num2, 1)

        print("Classic Result: ")
        print(classic_result)

        print("Divide and Conquer Result: ")
        print(dq_result)


if __name__ == "__main__":
    main()

