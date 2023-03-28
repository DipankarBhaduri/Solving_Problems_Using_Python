nums = [ 5 ,2 ,1, 6, 4 ,8 ]
para = "asc" 

if para == "asc" :
    nums.sort() 
    print(nums) 
else :
    desc_nums = sorted ( nums , reverse= True)
    print(desc_nums)