# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 15:34:30 2022
DAILY BEST SELLERS
@author: NVDL
"""
"""
Exercise 3.
Write a function, calculate_best_sellers, that returns a list of 
the n best selling items sorted by the number of copies sold (highest first). 
Ties are broken by using the ascending lexicographical (alphabetical)
ordering of the CINs. The elements in the list should be instances of the
BestSeller class described below.

The function takes two required arguments and one optional argument:
 - transaction_log: the transaction log (a single, potentially multiline, str)
 - n: the transaction log (a single, potentially multiline, str)
 - publication_type: an (optional) publication type to filter the items by

The function returns a list of BestSeller instances, sorted as described above.

Additional requirements
The function may return a list with fewer than n elements if the transaction 
log does not contain enough items to fill the list.

If the quantity sold of an item is 0, it is not included in a best sellers 
list even if that means returning a list with fewer than n elements.

The BestSeller class
Create a class, BestSeller, with three read-only properties:
- cin (str): the item’s Catalogue Identification Number
 - publication_type (str): the item’s publication type (see exercise 2.1)
- quantity_sold (int): The number of copies sold of this item
"""

######################## 2.3 Daily Best Sellers #################################

# Import Libs
import random

"""Simulate inventory"""
############### Dict of {CIN : 'inventory amount'} ############## 
def start_inventory(size):
    inv_amount = random.sample(range(10000000000000,90000000000000 ), size) #create sample of size {size} with 14 digit numbers representing CIN 
    item_amount_list = [] # empty list to initialise inventory amount per CIN
    for i in inv_amount: # iterate over samples
        amt_per_item = random.randint(0, 100) # create inventory amount
        item_amount_list.append(amt_per_item) # append inventory amount per sample
    res = {inv_amount[i]: item_amount_list[i] for i in range(len(inv_amount))}  # create dictionairy for every {CIN, inventory amount} in range length of total created CINs   
    return res # return dict

# Run 1    
archive = start_inventory(1000)
############### Dict of {CIN : 'inventory amount'} ############## 

##############  List of transactions [[CIN, INCOMING/OUTGOING, QUANTITY]] ##############
def transaction_log_(start_inventory): # takes in dict
    transaction_log_new = [] # empty list to list transaction logs
    for key in start_inventory.keys(): # iterate over dict keys of created CINs
        transaction_log_new.append([key,'incoming', random.randint(1, 5)]) # for every CIN (key) create a list that holds CIN, 'incoming', random number between 1 and 5
        transaction_log_new.append([key,'outgoing', random.randint(1, 5)]) # idem for outgoing and append both to the list
    return transaction_log_new # return list of transaction logs

# Run 2     
transaction_log_ = transaction_log_(archive) 
##############  List of transactions [[CIN, INCOMING/OUTGOING, QUANTITY]] ##############


"""Calculate best sellers"""
##############  List of best sellers based on [LOG, N and PUB_TYPE] ##############
def calculate_best_sellers (transaction_log, n, publication_type):
    d_best_list = []
    d_sp_list = []
    temp_best_dict = {}
    for i in transaction_log: # iterate over tlog       
        if i[1] == 'outgoing': # if transaction is outgoing
            temp_best_dict[i[0]] = 0 # add {CIN:0} as key/value to temp_dict
            d_best_list.append(i) # add log to daily best list
    
    for i in d_best_list: # iterate over daily best list
        for key, value in temp_best_dict.items(): # iterate over key/value pairs of temp_dict with daily best outgoing CINs
           if i[0] == key: # if i[0](CIN) is equal to key(CIN) 
               value += i[2] # add the value of the outgoing transaction to the matched key in temp_dict
               temp_best_dict.update({key:value}) # update the {CIN:inv_sold} with the new value in dict
              
    sort_best_dict_keys = list(temp_best_dict.keys()) # list keys (CIN) of temp_dict
    sorted_best_dict = {sort_best_dict_keys[i]: sorted( # reverse dict
    temp_best_dict.values(), reverse=True) [i] for i in range(len(sort_best_dict_keys))}
    sort_best_dict_keys = list(sorted_best_dict.items()) # Overwrite with new Lexi order of bestsellers 
    
    if publication_type == None: # if None was passed in the 3rd param
        print("This is the length of daily best list:", len(sort_best_dict_keys))
        sorted_best_dict_keys = sort_best_dict_keys[:n] # slice df by size n from index 0 -> n
        print("This is the length of daily best list by n:", len(sorted_best_dict_keys))
        
        return ("Daily best list ",  sorted_best_dict_keys)  
    
    else:
        for i in sort_best_dict_keys: # iterate over sorted key,value pairs
            check_pub_type = str(i[0]) # int not iterable --> sim_inventory creation
            check_pub_type = check_pub_type[:2] # unpack
            if check_pub_type == str(publication_type): # match pub type with first two digits of CIN
                d_sp_list.append(i)      
        print("This is the length of daily best specific pub type list:", len(d_sp_list))
        d_sp_list = d_sp_list[:n] # slice df by size n from index 0 -> n
        print("This is the length of daily best specific list by n:", len(d_sp_list))   
        
        return ("Daily specific list ", d_sp_list)
 
best_seller_list = calculate_best_sellers(transaction_log_, 10, None)  # show top "n" best selling per "pub_type" from transaction log
print(f"The {best_seller_list[0]}: {best_seller_list[1]}") # intentionally left i[1] for i in d_spec_list 'outgoing/incoming' as param can also be transaction id 

##############  List of best sellers based on [LOG, N and PUB_TYPE] ##############                

""" Create a class, BestSeller, with three read-only properties"""

class Bestseller:
    
    def __init__(self, transaction_log):
        self.transaction_log = transaction_log
         
    @property
    def cin(self):
        d_best_list = []
        temp_best_dict = {}
        for i in self.transaction_log:
            if i[1] == 'outgoing':
                temp_best_dict[i[0]] = 0 # add {CIN:0} as key/value to temp_dict
                d_best_list.append(i) # add log to daily best list     
                
        for i in d_best_list: # iterate over daily best list
            for key, value in temp_best_dict.items(): # iterate over key/value pairs of temp_dict with daily best outgoing CINs
               if i[0] == key: # if i[0](CIN) is equal to key(CIN) 
                   value += i[2] # add the value of the outgoing transaction to the matched key in temp_dict
                   temp_best_dict.update({key:value}) # update the {CIN:inv_sold} with the new value in dict
                   
        sort_best_dict_keys = list(temp_best_dict.keys()) # list keys (CIN) of temp_dict
        sorted_best_dict = {sort_best_dict_keys[i]: sorted( # reverse dict
        temp_best_dict.values(), reverse=True) [i] for i in range(len(sort_best_dict_keys))}
        sort_best_dict_keys = list(sorted_best_dict.keys()) # Overwrite with new Lexi order of bestsellers      // GET KEYS
        
        best_seller_cin = sort_best_dict_keys[:1] # slice last to prevent data loss in further development
        return best_seller_cin
    
    @property
    def pub_type(self):
        d_best_list = []
        temp_best_dict = {}
        for i in self.transaction_log:
            if i[1] == 'outgoing':
                temp_best_dict[i[0]] = 0 # add {CIN:0} as key/value to temp_dict
                d_best_list.append(i) # add log to daily best list     
                
        for i in d_best_list: # iterate over daily best list
            for key, value in temp_best_dict.items(): # iterate over key/value pairs of temp_dict with daily best outgoing CINs
               if i[0] == key: # if i[0](CIN) is equal to key(CIN) 
                   value += i[2] # add the value of the outgoing transaction to the matched key in temp_dict
                   temp_best_dict.update({key:value}) # update the {CIN:inv_sold} with the new value in dict
                   
        sort_best_dict_keys = list(temp_best_dict.keys()) # list keys (CIN) of temp_dict
        sorted_best_dict = {sort_best_dict_keys[i]: sorted( # reverse dict
        temp_best_dict.values(), reverse=True) [i] for i in range(len(sort_best_dict_keys))}
        sort_best_dict_keys = list(sorted_best_dict.keys()) # Overwrite with new Lexi order of bestsellers      // GET KEYS         
        
        best_seller_cin = sort_best_dict_keys[:1] # slice last to prevent data loss in further development
        
        pub_type = str(best_seller_cin)
        pub_type = int(pub_type[1:3])
        return pub_type

    @property
    def qty_sold(self):
        d_best_list = []
        temp_best_dict = {}
        for i in self.transaction_log:
            if i[1] == 'outgoing':
                temp_best_dict[i[0]] = 0 # add {CIN:0} as key/value to temp_dict
                d_best_list.append(i) # add log to daily best list     
                
        for i in d_best_list: # iterate over daily best list
            for key, value in temp_best_dict.items(): # iterate over key/value pairs of temp_dict with daily best outgoing CINs
               if i[0] == key: # if i[0](CIN) is equal to key(CIN) 
                   value += i[2] # add the value of the outgoing transaction to the matched key in temp_dict
                   temp_best_dict.update({key:value}) # update the {CIN:inv_sold} with the new value in dict
                   
        sort_best_dict_keys = list(temp_best_dict.keys()) # list keys (CIN) of temp_dict
        sorted_best_dict = {sort_best_dict_keys[i]: sorted( # reverse dict
        temp_best_dict.values(), reverse=True) [i] for i in range(len(sort_best_dict_keys))}
        sort_best_dict_keys = list(sorted_best_dict.items()) # Overwrite with new Lexi order of bestsellers     // GET ITEMS       
        
        best_seller_qty = sort_best_dict_keys[:1] # slice last to prevent data loss in further development
        best_seller_qty = best_seller_qty[0][1] # List of tuples
        
        return best_seller_qty
    
        
best_cin = Bestseller(transaction_log_).cin    
best_pub_type = Bestseller(transaction_log_).pub_type
best_qty_sold = Bestseller(transaction_log_).qty_sold    

######################## 2.3 Daily Best Sellers #################################
