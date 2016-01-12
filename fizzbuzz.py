"""Basic script for Fizz Buzz : http://c2.com/cgi/wiki?FizzBuzzTest
"""

def check_fizz_buzz(num=0):
    FB=""
    if num%3 == 0:
        FB += "Fizz"
    if num%5 == 0:
        FB += "Buzz"
    return FB

for i in range(1,100):
    print(i)
    IS_FB = check_fizz_buzz(i)
    print("%s\n" % (IS_FB))
