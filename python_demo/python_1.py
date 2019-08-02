for x in range(0,10):
    for y in range(0,10):
        for z in range(1,10):
            if x**3+y**3+z**3==x+10*y+100*z:
                print(x+10*y+100*z)
print("finish")