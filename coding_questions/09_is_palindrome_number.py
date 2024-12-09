def is_palindrome(number):
    number_copy = number
    reverse = 0

    while(True):
        if (number < 10):
            break
        remainder = number % 10
        reverse = (reverse * 10) + remainder
        number = int(number/10)

    return ((reverse*10) + number) == number_copy

number = 34543

if (is_palindrome(number)):
    print("Palindrome Number")
else:
    print("Not Palindrome")