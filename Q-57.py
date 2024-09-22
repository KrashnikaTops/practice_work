#57.How will you randomizes the items of a list in place?

#ans:-The shuffle() method is used in python to randomly shuffle the elements of a list.
#-this method is part of the random module,the method shuffle() can be used to randomize the items of a list in place.

#ex:-

import random
list=[1,2,3,4,5]
random.shuffle(list)
print(list)

