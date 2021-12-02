Github repository:
https://github.com/KeatonShawhan/Assignment_10_1

Class description:
The Phone class is one that takes in a specified amount of apps, files, pictures, and storage on the phone. It uses the apps, files, and pictures to calculate the amount of storage being used or the amount of storage left. There are 4 methods inside of it, get_storage(), get_apps(), storage_remaining(), and add_random_storages().

Variable description:
apps represents the amount of apps that are on the phone. They are each valued at 10 storage units when calculating the amount left. 
files represents the amount of files that are on the phone. They are each valued at 4 storage units when calculating the amount left.
pictures represents the amount of pictures that are on the phone. They are each valued at 3 storage units when calculating the amount left.
storage represents the amount of storage on the phone. Storage subtracting the sum of all the storage units used by the apps, files, and pictures will be used in storage_remaining().
remaining is the amount of storage left after subtracting the sum of all the storage units used by the apps, files, and pictures from the original storage. This is used in storage_remaining().
randstorage is the random number of storage from 0-200 units that is added to the original storage in add_random_storage().

Method description:
get_storage() simply returns the amount of storage on the phone at the given moment. It also checks if any of the attributes (apps, files, pictures, storage) are negative because you can't have these be negative. If any are negative, the method will return an error statement.
get_apps() simply returns the amount of apps on the phone at the given moment.  It also checks if any of the attributes (apps, files, pictures, storage) are negative because you can't have these be negative. If any are negative, the method will return an error statement.
storage_remaining() subtracts the sum of all the storage units used by the apps, files, and pictures from the current storage to return the remaining storage left on the phone.  It also checks if any of the attributes (apps, files, pictures, storage, remaining) are negative because you can't have these be negative. If any are negative, the method will return an error statement.
add_random_storage() adds a random amount of storage from 0-200 units (by using import random) to the current amount of storage. Then it will return the amount after the addition in a statement.

Demo program description:
The demo program will utilize all 4 methods. In order, it will print the return statements from each method inside the Phone class (get_storage(), get_apps(), storage_remaining(), and add_random_storages()).

Demo program instructions:
To use the demo program correctly, run the file and look at the terminal for the return statements and calculations of storage. To test a different number of apps, files, pictures, or storage, you can change the numbers in the line "x = Phone(2, 3, 2, 100)".