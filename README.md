# Negating propositions

You now understand how two logical propositions can be combined using the logical conjunction and disjunction operators.  You can hopefully also imagine how three or more logical propositions can be combined using these operators.  We will complete a task to consolidate your understanding of this in a few tasks from now.  Before we get on to that, however, I would like you to consider the Python program below:

````
if a==1 : 
   b = 2 
else : 
   b = 3
````

When this code is run the variable `b` is set equal to 2 if `a` is equal to 1.  If, by contrast, the negation of this proposition (i.e. if `a` is not equal to 1) is true then `b` is set equal to 3.

The negation of a logical proposition is a proposition that is always and only true when the original logical proposition is false.  We can express this idea using mathematical symbols as follows:

![](https://render.githubusercontent.com/render/math?math=\neg(a=1)\leftrightarrow\a\ne1)

In words, this set of symbols tells us that the negation of a=1 is true if and only if a is not equal to 1.

To see if you have understood this idea I would like you to write three functions in the cell on the right.  I have already written three functions for you.  All of the six functions that will eventually be written take two arguments:

1. `data` - a numpy array that contains multiple integers
2. `n` - an integer

The three functions that I have written are then as follows:

1. `numberEqualTo` - this function returns the number of elements in `data` which are equal to `n`
2. `numberLessThan` - this function returns the number of elements in `data` which are less than `n`
3. `numberMoreThan` - this function returns the number of elements in `data` which are greater than `n`

When the exercise is complete you should write three further functions:

1. `negationEqualTo` - should return the number of elements in `data` for which the negation of logical proposition in `numberEqualTo` is true.
2. `negationLessThan` - should return the number of elements in `data` for which the negation of logical proposition in `numberLessThan` is true.
3. `negationMoreThan` - should return the number of elements in `data` for which the negation of logical proposition in `numberMoreThan` is true.

You should not need to adjust the code at the end of the program in `main.py`.  The output this code produces will tell you if you code is working correctly.

