# Author: Jasmine Singh
# Github Username: Jassig98
# Date: November 1, 2022
# Description: Function that finds the median of a list of numbers

def find_median(num):
   num.sort()
   if(len(num) %2 ==1):
        return num[len(num)//2]
   else:
        return(num[len(num)//2] + num[(len(num) -1)//2])/2

