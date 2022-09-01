def fizzbuzz(r):
    for i in range(1,r):
        if(i%3==0 and i%5==0):
                    print(i,"= fizzBuzz")
        else:
            if(i%5==0):
                print(str(i),"= Buzz")
            else:
                if(i%3==0):
                    print(str(i),"= Fizz")
                else:
                    print(str(i))
fizzbuzz(31)
