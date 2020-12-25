# day 4

LOTS of small errors here that cost a ton of time

1. assuming that a substring was always 9 characters long.
a valid pid is a string of 9 characters from '0-9'. i just took `input[location:location+9]` and did the validity check on that. however, there are pids which are 10 characters long and are hence invalid but still treated as valid by this method.

should instead do `input[location:location+10].split()[0]`, which is admittedly still a bit bruteforce, but now you can check if the string is exactly length 9. using `split()` without any arguments also kills all newlines and spaces.

2. truthiness of objects
one thing great about Python's list comprehension is that you can simplify a lot of things into one line. however, remember to actually check the values of the list.

i had to check some string whether it constituted a valid RGB color code. meaning it must start with a `#` symbol and have 6 characters of `0-9 a-f`. what i initiall did was `code[0] == '#' and char in '0123456789abcdef' for char in code[1:]`

HOWEVER, note the small bug here! the list comprehension produces a generator Object, and Objects always are `True` in python! what we have might be `[True, True, False, True, True, True]`, but this whole list is evaluated to `True`!

so, you can use the primitive functions `all()` to reduce the list to a truth value. as an example,

`all(c in 'aeiou' for c in 'sequoia')` returns `False`
`all(c in 'aeiou' for c in 'euoia')` returns `True`

similarly, there is a `any()` function that returns `True` if at least one member of the list is `True`, otherwise `False`

# day 5

`mystring = '0123456'`
`mystring[1:5]` returns the 1st to 5th items, 5th not included. i.e. `1234`
`mystring[5]` is `5`

# day 10

my logic for part 2:
get all pairs of distance 3. these are compulsory in any solution. also the largest adapter is always compulsory.
get the complement of this. these are the optional blocks.

e.g. (sorted) input is 1 2 5 7 8 9 12 13 14 15 16
then compulsory ones are (2,5), (9,12), (16)
optional blocks are (1), (7,8), (13, 14, 15)

do combinations on each of the optional blocks (i.e. there are 2 ways to use the (1) block, 4 ways to use the (7,8) block, 7 ways to use the (13,14,15) => final ans: 2*4*7)

issues:
i was lucky that my optional blocks were all less than len 3, and also were contiguous. would be much harder to calculate if there were different kinds of optional blocks. apparently there's a fibonacci-like solution for this problem.

# day 11

when doing direction traversal and out of bounds checking for arrays, much neater to do it this way:

```
def check_point(i,j,direction,arr): #i,j are points where you want to check direction in, direction is tuple/2-value array, arr is overall search field
    i_change, j_change = direction
    i = i + i_change
    j = j + j_change

    if not (0 <= i < len(arr) and 0 <= j < len(arr[0])): return False # out of bounds condition
    else:
        ...
```

you can even call this function recursively, to continuously search in a given direction!

# day 12

rotation around a point using matrices:

```
def turn(dir, angle, pt):
    x, y = pt
    if dir == "L": #anticlockwise, using rotation matrix
        new_x = round( x*cos(radians(angle)) - y*sin(radians(angle)))
        new_y = round( x*sin(radians(angle)) + y*cos(radians(angle)))
        return [new_x, new_y]
    elif dir == "R": #clockwise, using rotation matrix
        new_x = round( x*cos(radians(angle)) + y*sin(radians(angle)))
        new_y = round(-x*sin(radians(angle)) + y*cos(radians(angle)))
        return [new_x, new_y]
```

# day 17

for these kind of Conway-style problems, can improve efficiency a lot by 1. having a separate list which records the changes to be made, then 2. directly modifying the master list after all the changes have been calculated. it saves a lot from having to make multiple deepcopies to send changes around.

# day 18

TODO: learn to build binary arithmetic trees with variable operator precedence
TODO: for fun: also let this class be able to output the prefix/postfix/infix of the expression

i used this with some changes [Evaluation of Infix Expressions]( https://algorithms.tutorialhorizon.com/evaluation-of-infix-expressions/ )

# day 20

TODO: write a real solution for part 2 lol

# day 22

my original solution was TOO recursive such that it broke the stack. refactoring into a while loop makes it much easier on the system. i left the original solution there as reference.

yet another off by one error because of what happened in day5. cost an hour or so of debugging.

why don't we need deepcopy? because in Python, list slices are actually passing by value. i.e. `functioncall(mylist[2:5])` does not actually modify `mylist`! the list slice makes a completely new list object!!

neater way instead of `while not len(list1) == 0 or len(list2) == 0`, just `while list1 and list2` since an empty list is Falsy (why!? anyway, empty lists, tuples, dicts, sets, strings, and ranges are all Falsy)

# day 23

why is a linked list faster than a list? because array deletion and insertion is O(n), but linked list is O(1) since you are just moving pointers around. in an array, you have to shift the indexes of all 1 million elements!

although i didn't use a real linked list for this anyway... a dictionary is sufficient to emulate a linked list :) the keys are the current label and the value is the next element.

apparently this problem was similar to 2018 day 9

# day 24

basically a conway again. main challenge is expressing hex coordinates, which is easily done with the systems found [here](https://www.redblobgames.com/grids/hexagons/). then the rest of the code is exactly like day 17.
