# tuple in python
* Tuple: Tuples are defined by enclosing the 
        elements in parentheses (()) instead of square brackets ([]).
    2. Tuples are immutable means we can not alter them after creation
    3. Tuple are order collection of data item. This store multiple item in single variable

* if we write tuple = (2) then python convert this is 'int' type then python did not find that is tuple.
  so overcome this problem we write an comma after the value
    tuple = (2,) now python will find that is tuple type.

* if we want to alter the tuple then we convert that tuple to the list and after performing operations
  we convert again list to tuple

# index(value, startIndex, endIndex)
* The index() method searches for the first occurrence of the given item and returns its index. 
  If specified item is not found, it raises ‘ValueError’ exception.
  * startIndex -> An index specifying where to start the search.Default is 0.
  * endIndex -> An index specifying where to stop the search.Default is the end of the tuple.