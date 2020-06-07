# Linear Structures

# Stacks

A Stack is structured, ordered collection of items where items are added to and
removed from the end called the "top". Stacks are ordered LIFO.

# Queues

A queue is an ordered collection of items where the addition of new items happens
at one end, called the "rear", and the removal of existing items occurs at other 
end, commonly called the "front". As an element enters the queue it starts at 
the rear and makes its way toward the front, waiting until that time when it is the
next element to be removed.

# Deques

A deque, also known as a double-ended queue, is an ordered collection of items similar
to the queue. It has two ends, a front end and a rear, and the items remain positioned
in the collection. This hybrid linear structure provides all the capabilities of stacks
and queues in a single data structure.

# List

A list is a collection of items where each item holds a relative position with respect
to the others. 

# Recursion

Recursion is a method of solving problems that involves breaking a problem down
into smaller and smaller subproblems until you get to a small enough problem that
it can be solved trivially. Usually recursion involves a function calling itself.
While it may otherwise be very difficult to program.

All recursive algorithms must obey three importan laws:

    1. A recursive algorithm must have a base case.
        Is typically a problem that is small enough to solve directly
    2. A recursive algorithm must change its state and move toward the base case
        Means that some data that the algorithm is using is modified, Usually the data that
        represents our problem gets smaller in some way.
    3. A recursive algorithm must call itself, recursively.
        
    
# Sorting and Searching

We should always consider whether it is cost effective to take on the extra work of sorting to gain
searching benefits. If we can sort once and then search many times, the cost 
of the sort is not so significant. However, for larger list, sorting even once
can be so expensive that simply performing a sequential search from the start
may be the best choice.

**Binary Search** 

A binary search will start by examining the middle item. If that item is the one
we are searching, we are done. If it is not the correct item, we can ordered nature
of the list to eliminate half of the remaining items.

**Hashing** 

Data structure that can be searched in `O(1)` time. A hash table is a collection
of items which are stored in such a way as to make it easy to find them later. Each
position of the hash table, ofted called `slot`, can hold an item and is named
by integer value starting at 0.

    - Hash function: The mapping between an item and the slot where the that item belongs
      in the hash table.
                    
    - Load Factor l = number_ot_items/table_size
    
    - Collision: Two or more items would need to be in the same slot
    
    **Hashing Functions**
    
        - The folding method for constructing has functions begins by dividing the
        item into equal size peicces (the last piece may not be equl size(
        
        - mid-square method, we first square the item, and then extract some portion
        of the resulting digits.
        
        - Collision Resolution, When two items hash to the same slot, we must have
        a systematic method for placing the second item in the hash table.
    
            - Open addressing: Start at the origintal have value position and then 
            move in a sequential manner through the slots until we encounter the first
            slot that is empty. Note that we may need to go back to the first slot (circularly)
            to cover the entire hash table.
            
            - rehashing: Process of looking for another slot after a collision is rehashing
            with simple linear probing. Is often suggested that the table size be a primer number.
            
           - quadratic probing is a variation of the linear probing for avoid clustering, usuarlly
           search every 3 pos slot at solving collisions. Uses a skip consisting of successive perfect
           squares
        
           - Chaining allows many items to exist at the same location. When collision happens
           the item is still placed in the proper slot of the hash table.
       
**Bubble Sort**

Makes multiple passes through a list. It compares adjacent items and exchanges those are out of order
. Each pass through the list places the next largest value in its proper place. In essence, each item
"bubbles" up the location where it belongs.

A bubble sort can be modified to stop early if it finds that the list has become sorted. If during a 
pass there are no exchanges, then we know that the list must be sorted.

**Selection Sort**

The selection sort improves on the bubble sort by maing only one exchange for every pass through the
list. In order to do this, a selection sort looks for the largest value as it makes a pass and, after
completing the pass, places it in the proper location. As wish a bubble sort, after the first pass,
the largest item is in the correct place. After the second pass, the next largest is in place.

**The Insertion Sort**

The insertion sort, although still O(n^2), works in a slightly different way. It always maintains
a sorted sublist in the lower positions of the list. Each new item is then "inserted" back into the
previous sublist such that the sorted sublist is one item larger.

One note about shifting versus exchanging is also important, In general, a shift operation requires
approximetely a third of the processing work of an exchange since only one assignment is performed.
In benchmark studies, insertion sort will show very good performance.

**Shell Sort**

Sometimes called the "diminishing increment sort", improves on the insertion sort by breaking the 
original list into a number of smaller sublist, each of which is sorted using an insertion sort.
The unique way that these sublists are chosen is the key to the shell sort.
Instead of breaking the list into sublists of contiguous items, the shell sort uses an increment i,
sometimes called the gap, to create a sublist by choosing all items that are i items apart.

