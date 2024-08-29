
# what is set in python?
  
  Set is one of 4 built-in data types in Python used to store 
  collections of data, the other 3 are List, Tuple, and Dictionary, 
  all with different qualities and usage.

Set is collection of item and enclosed with curly braces {}.

   Set do not maintain the order of element. 
   Set are also used to store multiple item in a single variable.

   Set does not contain duplicate item.

   A set is a collection which is unordered, *unchangable, and unindexed.

   * Note: Set items are unchangeable, but you can remove items and add new items.

# union(set name required) method
  union() method return a set that contain all items from the original set, and all item
  from the specified set which is given inside the union method.
  If an item is present in more than one set, the result will contain only one appearance of this item.

  ############################
* The union() methods joins all items from both sets, means it contains only that unique item which is present in both set and 

# update() methods 
* joins all items from both sets, means it update the original set and join that. 

# The intersection(set1,set2...) method 
* keeps ONLY the duplicates, means it contains only that item which is present in both set.

# intersection_update(set1,set2...) method
 * set1 is required, set2 is optional
 * The intersection_update() method updates the set by removing the items that are not common to all the specified sets.

# The difference() method 
* keeps the items from the first set that are not in the other set(s). 

# The symmetric_difference(set1,set2...) method 
 * keeps all items EXCEPT the duplicates.
 * Means it give the uncommon value which not present in both set

# symmetric_difference_update(set1,set2...) method
* same as symmetric_difference() method but it update the original set

# issuperset(set1,set2..) method
* it check if all the item of particular set is present in the original set, if present the it
  return true otherwise false