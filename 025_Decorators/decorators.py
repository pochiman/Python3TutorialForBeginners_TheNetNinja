'''

Decorators extend the behavior of a function that it's used on 
without modifying the function itself and they're used a lot 
in web frameworks like Django.

A decorator is a wrapper function. It takes in a function (question), 
the thing that it's used upon and it's going to wrap some extra behavior 
around it.

So in this function:

def cough_dec(func):

what we need to do is actually define another function:

    def func_wrapper():

This is the wrapper function that's going to wrap around this function:

def question():

# code before function --- add a little cough before the question()
- so before question() runs, we can apply some code
- then we fire question() itself by invoking it --- that's the function we're passing in
# code after function --- add a little cough after the question()
- so we're coughing on both sides of the function itself

What we need to do next is return the func_wrapper() function 
- so when we're using the @cough_dec decorator on a function, what happens is this cough_dec(func) decorator 
of this function gets called and the question() function the decorator sits on is passed in right here: cough_dec(func)

- then what we're doing is we're defining some kind of func_wrapper() wrapper function and inside this function, we can 
wrap code around the actual func() function it sits on, this thing down here --- question()
- so we're extending the behavior of this question() functionality if you want.

- so once we've done that, then we need to return this func_wrapper() function which is going to be fired down here --- @cough_dec
- so let us now return the func_wrapper() function.
- so this gets returned so that when we use this @cough_dec decorator, we're basically firing this func_wrapper function
- and we're applying this behavior on both sides of the question() function 

- And the cool thing is we can apply now this decorator to any function, it doesn't have to be just this question() function right here.

@cough_dec
def answer():

We're just defining this decorator once, creating this wrapper function which is surrounding our function 
which we pass in and then we can use this decorator on whichever function we create from then on.

'''

def cough_dec(func):

    def func_wrapper():
        # code before function
        print('*cough*')
        func()
        # code after function
        print('*cough*')

    return func_wrapper

@cough_dec
def question():
    print('can you give me a discount on that?')

@cough_dec
def answer():
    print("it's only 50p you cheapskate")

question()
answer()
