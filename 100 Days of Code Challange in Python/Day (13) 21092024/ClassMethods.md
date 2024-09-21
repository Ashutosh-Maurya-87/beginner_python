# What are class method's in Python
* There are three type of class methods
1. Instance Method
2. Class Method
3. Static Method

# Instance Method
* Used to access or modify the object state. If we use instance variables inside a method, such methods are called instance methods.
* It can Access and modified both class and instance varibales value


# Class Method
* Used to access or modify the class state. In method implementation, if we use only class variables, then such type of methods we should declare as a class method.
* we use @classmethod decorator to define the class method
* It can access only class variables

# Static Method
* It is a general utility method that performs a task in isolation. Inside this method, we don’t use instance or class variable because this static method doesn’t have access to the class attributes.
* It can not access or modified  the class and instance variables