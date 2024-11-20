def integer_sqrt(n):
    if n < 0:
        raise ValueError("Корень из отрицательного числа не определен")

    left, right = 0, n

    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            left = mid + 1
        else:
            right = mid - 1

    return right  # Возвращаем наибольшее целое число, квадрат которого <= n

n = 27
result = integer_sqrt(n)
print(f"Целая часть квадратного корня из {n} равна {result}")
