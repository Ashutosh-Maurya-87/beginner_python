# Virtual Envoirnment
'''
a virtual envoirnment is a tool used to isolate specific python
envoirnment on a single machine. allowing we to work on multiple project
with different dependencies and packages without conflicts. this can be especially
useful when working on projects that have conflicting package that are not compatible with each other

To create virtual envoirnment in Python , we can use venv module that comes
with Python.

'''

# Create virtual envoirnment
#   python -m venv myenv

# Activate the virtual enviornment
#   myenv\Scripts\activate.bat

'''
Once the virtual envoirnment is activated any packages
that we installed pip will be installed in the virtual enviornment
rather than in the global Python enviornment . This allows we
to have separate set of packages for each project without affecting 
the packages installed in the global enviornment

'''

# To deactivate the virtual enviornemnt 
#    deactivate


# requirnment.txt file ---------------------
'''
In addition to creating and activation a virtual enviornment . It can be useful to create a requirnment
file that list the packages and their version that our projects depends on.
This file can be used to easily installed all the required package and their version 

For ex->
'''
# Output the list of installed package and their version to a file---
# pip freeze > requirnment.txt

'''
To installed package listed in the requirnment txt file on our enviornment then 

We can use the pip install command with the -r flag
'''
# installed the package listed in the requirnments.txt file
# pip install -r requirnments.txt