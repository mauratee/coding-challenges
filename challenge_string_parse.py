import unittest

def parseTransactionRecord(transaction, property):
    """Parse transaction and return value for relevant property

    >>> parseTransactionRecord("", "")
    ''

    >>> parseTransactionRecord("e7d36ba58a02021-09-10RAKUTEN PYMNT HEALTH  JEWELRY           D0000078885", "transaction_id")
    'e7d36ba58a'
    >>> parseTransactionRecord("e7d36ba58a02021-09-10RAKUTEN PYMNT HEALTH  JEWELRY           D0000078885", "is_posted")
    'false'
    >>> parseTransactionRecord("e7d36ba58a02021-09-10RAKUTEN PYMNT HEALTH  JEWELRY           D0000078885", "as_of_date")
    '2021-09-10'
    >>> parseTransactionRecord("e7d36ba58a02021-09-10RAKUTEN PYMNT HEALTH  JEWELRY           D0000078885", "description")
    'RAKUTEN PYMNT HEALTH  JEWELRY'
    >>> parseTransactionRecord("e7d36ba58a02021-09-10RAKUTEN PYMNT HEALTH  JEWELRY           D0000078885", "direction")
    'debit'
    >>> parseTransactionRecord("e7d36ba58a02021-09-10RAKUTEN PYMNT HEALTH  JEWELRY           D0000078885", "amount")
    '78885'

    >>> parseTransactionRecord("e7d36ba58a2021-09-10RAKUTEN PYMNT HEALTH  JEWELRY           D0000078885", "is_posted")
    ''
    >>> parseTransactionRecord("e7d36ba58a2021-09-10RAKUTEN PYMNT HEALTH  JEWELRY           D0000078885", "as_of_date")
    '2021-09-10'

    """
    # input: transaction record, property name
    # output: property value
    
    
    # print(transaction)
    # print(len(transaction))

    # if transaction is empty string, return empty string
    if not transaction:
        return ""
    
    if len(transaction) == 72:
    
        transaction_dict = {}
        
        transaction_dict["transaction_id"] = transaction[:10]
        #print(transaction_id)
        is_posted = transaction[10]
        if is_posted == "0":
            is_posted = "false"
        else:
            is_posted = "true"
        # print(is_posted)
        transaction_dict["is_posted"] = is_posted
        transaction_dict["as_of_date"] = transaction[11:21]
        #print(as_of_date)
        description = transaction[21:61].rstrip()
        transaction_dict["description"] = description
        #print(description)
        direction = transaction[61]
        if direction == "D":
            direction = "debit"
        else:
            direction = "credit"
        #print(direction)
        transaction_dict["direction"] = direction
        transaction_dict["amount"] = transaction[62:].lstrip("0")
        #print(amount)
        
        #print(transaction_dict)
        
        return transaction_dict[property]
        
    else:
        print(transaction.vformat())
        return transaction
        # need to figure out how to find missing properties and return empty strings for missing


# class Test(unittest.TestCase):

#     # def regular_transaction(self):
#     #     result = 
#     #     expect = 
#     #     self.assertEqual(result, expect)

#     def transaction_empty(self):
#         result = parseTransactionRecord("", "direction")
#         expect = ""
#         self.assertEqual(result, expect)

# unittest.main(verbosity=2)


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n✨✨ All tests passed! ✨✨\n")