# Access Modifier
* There are three type of Access Modifier
1. Public ->  Accessible anywhere from outside of the class.

2. Private -> Accessible within the class

3. Protected -> Accessible within the class and its sub-classes

# Note 
* In Python, we don’t have direct access modifiers like public, private, and protected. We can achieve this by using "single underscore" and "double underscores".


# Private Member
* We can protect variables in the class by marking them private. 
* To define a private variable add "two underscores" as a prefix at the start of a variable name.

* Private members are accessible only within the class, and we can’t access them directly from the class objects.

# We can access private members from outside of a class using the following two approaches
# 1. Create public method to access private members

# 2. Use name mangling

# Name Mangling to access private members
1. We can directly access private and protected variables from outside of a class through name mangling. 
2. The name mangling is created on an identifier by adding two leading underscores and one trailing underscore, like this _classname__dataMember, 
* where classname is the current class, and data member is the private variable name.


# Protected Data Member
* Protected members are accessible within the class and also available to its sub-classes. 
* to make protected data member add a single _ at the prefix of the varibale
# Note
* Protected data members are used when we implement inheritance and want to allow data members access to only child classes.