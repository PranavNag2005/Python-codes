# from math import factorial

# def print_pascal_triangle(n):
#     for i in range(n):
#         for j in range(n - i + 1):
#             print(end=" ")  # for left spacing
#         for j in range(i + 1):
#             # nCr = n! / (r! * (n - r)!)
#             print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
#         print()  # for new line

# # Example usage
# print_pascal_triangle(5)
# from math import factorial
# for i in range(6):
#     for j in range(6-i+1):
#         print(end=" ")
#     for j in range(i+1):
#         print(factorial(i)//(factorial(j)*factorial(i-j)),end=" ")
#     print()

n=5
for i in range(n):
    for j in range(n-i+1):
        num=1
        print(end=" ")
    for j in range(i+1):
        print(num,end=" ")
        num=num*(i-j)//(j+1)
       
    print()