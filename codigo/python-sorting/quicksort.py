# Pseudocode

# choose pivot
#swap a[1,rand(1,n)]

# 2-way partition
#k = 1
#for i = 2:n, if a[i] < a[1], swap a[++k,i]
#swap a[1,k]
## invariant: a[1..k-1] < a[k] <= a[k+1..n]

# recursive sorts
#sort a[1..k-1]
#sort a[k+1,n]


def partition(list, start, end):
    pivot = list[end]                          # Partition around the last value
    bottom = start-1                           # Start outside the area to be partitioned
    top = end                                  # Ditto

    done = 0
    while not done:                            # Until all elements are partitioned...

        while not done:                        # Until we find an out of place element...
            bottom = bottom+1                  # ... move the bottom up.

            if bottom == top:                  # If we hit the top...
                done = 1                       # ... we are done.
                break

            if list[bottom] > pivot:           # Is the bottom out of place?
                list[top] = list[bottom]       # Then put it at the top...
                break                          # ... and start searching from the top.

        while not done:                        # Until we find an out of place element...
            top = top-1                        # ... move the top down.
            
            if top == bottom:                  # If we hit the bottom...
                done = 1                       # ... we are done.
                break

            if list[top] < pivot:              # Is the top out of place?
                list[bottom] = list[top]       # Then put it at the bottom...
                break                          # ...and start searching from the bottom.

    list[top] = pivot                          # Put the pivot in its place.
    return top                                 # Return the split point


def qsort(list, start, end):
    if start < end:                            # If there are two or more elements...
        split = partition(list, start, end)    # ... partition the sublist...
        qsort(list, start, split-1)        # ... and sort both halves.
        qsort(list, split+1, end)

def sort(list):
    qsort(list, 0, len(list)-1)
    
