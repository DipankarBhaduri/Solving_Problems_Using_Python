def findTheTarget ( nums , target ) :
    start = 0 
    end = ( len(nums) - 1 )
    index = -1 

    while start <= end :
        mid = ( start + end ) // 2  
        if nums[mid] == target :
            index = mid 
            break 

        if nums[mid] > target :
            end = mid - 1 

        if ( nums[mid] < target ) : 
            start = mid + 1

    return index 

nums = [ 2 , 3 , 4 , 5 , 6 , 7 , 8 ] 
target = 8

ans = findTheTarget ( nums , target )
print(target , "Fount at index no :" , ans)