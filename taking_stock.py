# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 20:08:47 2022

@author: NVDL

Adjust Line 43 for inventory size

Exercise 2.
Write a function, calculate_inventory, that calculates the new inventory at the end of the day based on the day’s transaction log. 
The function takes two arguments:
 - start_inventory: a mapping of CINs to their quantity at the start of the day
 - transaction_log: the transaction log (a single, potentially multiline, str)
 
The function returns a new dictionary that maps CIN to their updated inventory count.

Additional requirements
 - The start_inventory mapping should not be changed.
 - Items that have their inventory count drop to 0 are still included in the returned inventory.
 - Assume that CINs not present in the start_inventory have a starting count of 0.
 - It is okay for an item’s inventory count to (temporarily) drop below zero while processing a transaction log, 
   as employees may enter transactions out of order. However, if there are still items with a negative inventory count 
   after processing the entire transaction log, raise an appropriate exception with an informative message, as having 
   a negative quantity in stock at the end of the day should not be possible.
"""
######################## 2.2 Taking Stock #################################
# Import Libs
import random 
import warnings

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
archive = start_inventory(500)
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

"""Update inventory"""
############## Update Inventory ##############
def calculate_inventory(start_inventory, transaction_log):
    end_inventory = start_inventory.copy() # copy the start_inventory 
    
    for key, value in end_inventory.items(): # iterate over the start_inventory {CIN:inventory amount} pairs
        for i in transaction_log: # for every transaction log instance
            if i[0] == key: # if the object at index 0 (CIN) is equal to the key of the start_inventory pairs
                if i[1] == 'incoming': # and if the object at index 1 states 'incoming' (assuming incoming = number of copy's sold)
                    print(f"Initial value of (CIN:{key}) was ",value)
                    value += i[2] # then, add the value of the object at index 2 (quantity)
                    print(f"The updated value of (CIN:{key}) is ",value)
                    end_inventory[key] = value # update the value(new inventory amount) given the key (CIN)
                elif i[1] == 'outgoing':
                    print(f"Initial value of CIN:{key}) was ",value)
                    value-= i[2]
                    print(f"The updated value of CIN:{key}) is ",value)
                    end_inventory[key] = value
                    if value < 0: # Raise warning if the resulting value is < 0
                        warnings.warn(f" WARNING: Item with CIN number: {key} returns a non-positive value of {value}. Please, check inventory! -- Adding to warning list")
                else:
                    print('Check type')
                        
            elif i[0] not in end_inventory.keys(): # if CIN is in transaction log but not archived add i (list) to the end_inventory list
                print(f"Updating inventory with new item with CIN{i[0]}")
                temp_dict = {i[0]:i[2]} # add {CIN:inventory} keypair, assuming 0, but can be any number
                end_inventory.update(temp_dict)
                
    
    CIN_warning_dict = {} # create empty dict              
    for key_end_inv, val in end_inventory.items(): # iterate over {CIN:updated inventory amount}
        if val < 0: # if the inv_amount < 0
            CIN_warning_dict[key_end_inv] = val # add key, pair to dict
            
    return end_inventory, CIN_warning_dict # return updated inventory and warning_list

# Run 3
new_data = calculate_inventory(archive, transaction_log_) # Run transaction log on start_inventory with calculate_inventory function and save in new variable
new_inv = new_data[0] # Unpack tuple new inventory list
warning_list = new_data[1] # Unpack tuple warning list
############## Update Inventory ##############

######################## 2.2 Taking Stock #################################