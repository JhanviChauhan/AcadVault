# NAME : JHANVI CHAUHAN 
# ID : 201701445
# EMAIL : 201701445@daiict.ac.in

from utils import *
import math
from node import Node


def merkle_proof(tx, merkle_tree):
    """Given a tx and a Merkle tree object, retrieve its list of tx's and
    parse through it to arrive at the minimum amount of information required
    to arrive at the correct block header. This does not include the tx
    itself.

    Return this data as a list; remember that order matters!
    """
    #### YOUR CODE HERE
    transactions = merkle_tree.leaves
    find = tx
    found =[]
    
    while(len(transactions)>1):
        new_transactions=[]
        for i in range(0,len(transactions), 2):
            data1=transactions[i] + transactions[i+1]
            hashed_data1=hash_data(data1, 'sha256')
            if transactions[i] == find:
                found.insert(0,Node('r', transactions[i+1]))
                find = hashed_data1
            elif transactions[i+1] == find:
                found.insert(0,Node('l', transactions[i]))
                find = hashed_data1
            new_transactions.append(hashed_data1)
        transactions=new_transactions
    return found



def verify_proof(tx, merkle_proof):
    """Given a Merkle proof - constructed via `merkle_proof(...)` - verify
    that the correct block header can be retrieved by properly hashing the tx
    along with every other piece of data in the proof in the correct order
    """

    #### YOUR CODE HERE

    while(len(merkle_proof)>0):
        cur_node = merkle_proof.pop()
        if(cur_node.direction == 'l'):
            data = cur_node.tx + tx
        else:
            data = tx + cur_node.tx
        tx = hash_data(data, 'sha256')
    return tx
