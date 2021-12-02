# Keaton Shawhan
# Implement your own class based on a real_world object.
# Your_Own_Class_10_1.py
import random as rand

# Craete Phone class
class Phone:
    # Pass through apps, files, pictures, and storage
    def __init__(self, apps, files, pictures, storage):
        # make all attributes private
        self.__apps = apps
        self.__files = files
        self.__pictures = pictures
        self.__storage = storage
    # make get_[] function to access the private storage attribute
    def get_storage(self):
        # check if any of the private attributes are negative
        if self.__apps < 0 or self.__files < 0 or self.__pictures < 0 or self.__storage < 0:
            # return a statement telling the user that the amount of apps, files, pictures, or storage cannot be negative
            return("Amount of apps, files, pictures, or storage cannot be negative.")
        # return the amount of storage in the phone
        return(f"Amount of storage: {self.__storage}")
    # make get_[] function to access the private apps attribute
    def get_apps(self):
        # check if any of the private attribute are negative
        if self.__apps < 0 or self.__files < 0 or self.__pictures < 0 or self.__storage < 0:
            # return a statement telling the user that the amount of apps, files, pictures, or storage cannot be negative
            return("Amount of apps, files, pictures, or storage cannot be negative.")
        # return the amount of apps in the phone
        return(f"Amount of apps: {self.__apps}")
    # make another method to calculate the storage remaining
    def storage_remaining(self):
        # check if any of the private attribute are negative
        if self.__apps < 0 or self.__files < 0 or self.__pictures < 0 or self.__storage < 0:
            # return a statement telling the user that the amount of apps, files, pictures, or storage cannot be negative
            return("Amount of apps, files, pictures, or storage cannot be negative.")
        # calculate the amount of remaining storage with a certain amount of storage for each app, file, and picture
        self.__remaining = (self.__storage - ((self.__apps*10)+(self.__files*4)+(self.__pictures*3)))
        # check if the remaining storage is above 0, meaning if there is room for the apps, files, and pictures in the phone
        if self.__remaining < 0:
            # return a statement telling the user their storage isn't big enough
            return("You have too many apps, files, or pictures to store into the phone.")
        # return a statement telling the user of how much storage they have after calculations
        return(f"Amount of storage remaining after space of apps, files, and pictures calculated: {self.__remaining}")
    # create a function that adds a random amount of storage to the phone from 0-200
    def add_random_storage(self):
        # calculate the random number
        self.__randstorage = rand.randint(0,200)
        # add the random amount of storage to the previous storage
        self.__storage += self.__randstorage
        # return a statement will the new amount of storage
        return(f"Storage after adding random amount: {self.__storage}")


        

def main():
    x = Phone(2, 3, 2, 100)
    print(x.get_storage())
    print(x.get_apps())
    print(x.add_random_storage())
    print(x.storage_remaining())

if __name__ == "__main__":
    main()