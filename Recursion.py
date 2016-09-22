def num_beer(x):
    if x > 0:
        print (str(x) + " bottles of beer on the wall, " + str(x) + " bottles of beer.")
        print ("if one of those bottles should happen to fall")
        x -= 1
        print (str(x) + " bottles of beer on the wall.")
        num_beer(x)

num_beer(99)
