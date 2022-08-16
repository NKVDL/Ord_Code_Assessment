# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 11:26:08 2022

@author: NVDL
"""
"""
Exercise 1.
Each item in the bookshop’s catalogue can be identified by its unique 
Catalogue Identification Number (CIN). 
A CIN is a sequence of 14 digits that follows a fixed structure:
    -The first two digits identify the type of publication 
    (e.g., “17” for book or “42” for a magazine),
    -the next 10 digits form an article number, and the last 2 digits form 
    a checksum that can be used to validate the CIN. 
    - Leading zeros are included as part of the CIN.


The checksum is computed by taking the first 12 digits of CIN, 
multiplying each individual digit by
its position (note: the position number starts at one),
calculating the sum of all those multiplications, 
and, finally, 

by computing the modulo 97 of that sum. 

For instance, for the CIN 17000372214424, you can 
validate its checksum, 24, as follows:
(1*1 + 2*7 + 3*0 + 4*0 + 5*0 + 6*3 + 7*7 + 8*2 + 9*2 + 10*1 + 11*4 + 12*4) % 97 = 24


Write a function, is_valid_cin, that validates a CIN. 
- If a CIN follows the correct format and its checksum checks out, the function
  should return True. 
- In all other cases, the function should return False. The function should 
  have the following signature:
    
  def is_valid_cin(cin: str) -> bool:
  ...
"""
######################## 2.1 Catalogue Identification Number #################################
cin = [1, 7, 4,5,6,7,8,9,3,4,5,6, 2,4] # Article no, article id, checksum 

def is_valid_cin(cin_seq):
    #Check structure
    if len(cin_seq) == 14: # If length of CIN input equals CIN structure of 14 digits
        index = 1 # Add counting parameter initialisation
        summation = 0 # Initialise variance mapping
        for i in cin_seq[:12]: # iterate over first 12 digits
           summation += i * index # for every index multiply the digit, add to summation
           print(summation)
           index += 1 # increase index to multiply per iteration
           print(index)
    
    check_sum = ''.join([str(i) for i in cin_seq[12:]]) # join last two digits as str
    
    if summation%int(check_sum) != 0: # if the remainder of summation mod check_sum is not 0, then the digits are not a valid checksum of the first 12 digits
        print("Error: The input has no matched CIN structure")
        return False
    else:
        return True

is_valid_cin(cin)          
            
######################## 2.1 Catalogue Identification Number #################################       
        
    
    