<b>Ordina Coding Assesment</b>

For this coding assesment I simulated a database with transaction logs that I ran through some functions that outputs item attributes such as id(CIN) and value(copies). Those variables were used to calculate the best items sold given a parameter N and optionally a publication type.  

<i>CIN.py</i> has a unidimensional approach where the passed parameter consists of a list with integers to unpack that represent barcodes that holds a two digit publication type, a 10 digit item id and a two digit checksum, to check if the passed parameter is a valid CIN.

<i>taking_stock.py</i> simulates an inventory with items and item amounts, and a transaction log with the CIN, type of transaction and total value of transaction. The end day inventory is calculated and warnings are raised when the inventory amount for an item is negative, indicating either missing stock or incorrect logging of transactions. A list with updated inventory and a warning list with negative inventory is returned and is called by:
```Python
calculate_best_sellers(transaction_log_, 10, None)  # show top "n" best selling from transaction log
```
Or specify a 2 digit pub_type:
```Python
calculate_best_sellers(transaction_log_, 10, 82)  # show top "n" best selling per "pub_type" from transaction log
```

<i>DBS.py</i> differentiates in calculating a list of best sellers by again passing a transaction log as parameter, given n with an optional publication type parameter to specify daily best sellers in that category. Lastly, a class Bestseller that returns the best seller's CIN, publication type or quantity sold is callable by:
```Python
Bestseller(transaction_log_).cin
Bestseller(transaction_log_).pub_type
Bestseller(transaction_log_).qty_sold 
```

<b> Libraries used <b>
```Python
import random
import warning
```
