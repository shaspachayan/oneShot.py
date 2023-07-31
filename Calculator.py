# n=-1
# n = int(input())
#
# if n % 2 == 0:
#     if 2>=n<=5:
#         print("Not Weird")
#     if 6 >= n <= 20:
#         print("Weird")
#     else:
#         print("Not Weird")
# else:
#     print("Weird")

"""
things to remember : 01
In Python, the expression 6 >= n <= 20 is evaluated from left to right. It is equivalent to (6 >= n) and (n <= 20).
Similarly, 26 <= n <= 20 would be evaluated as (26 <= n) and (n <= 20).

Now, let's analyze the two expressions:

6 >= n <= 20:

When n is less than or equal to 6, both parts of the expression will be true, and the entire expression will be true.
When n is greater than 6 and less than or equal to 20, the first part of the expression will be false (6 >= n is false),
and the entire expression will be false.
When n is greater than 20, both parts of the expression will be false, and the entire expression will be false.
So, 6 >= n <= 20 will be true only when n is less than or equal to 6.

26 <= n <= 20:

This expression doesn't make logical sense since it requires n to be both greater than or equal to 26 and less than or
equal to 20, which is not possible.

things to remember : 02

You used if 2 times, remember when the 1st if executed the authority will go to next if and that's what if you want
then  ok!! But in this case it seems that we want if once the no is decided weather it is weird or not then another
check is unnecessary, so in this case using elif is good , because if elif.... elif else will create the scenario
once to check only . If checked , terminate the statement"""
n = int(input())
if n % 2 == 0:
    if 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")
else:
    print("Weird")