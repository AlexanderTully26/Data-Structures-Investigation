import hashlib
import time

class Block:
    def __init__(self, index, data, previous_block=None):
        self.index = index  # Unique ID for the block
        self.timestamp = time.time()
        self.data = data
        self.previous_block = previous_block  # Reference to the previous block
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        """Creates hash for the blOCK Data"""
        hash_input = f'{self.index}{self.timestamp}{self.data}{self.previous_block.hash if self.previous_block else None}'
        return hashlib.sha256(hash_input.encode()).hexdigest()
    
    def __repr__(self):
        return f'Block(index={self.index}, data={self.data}, hash={self.hash[:10]})'

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()
    
    def create_genesis_block(self):
        """Creates first block in the blockchane"""
        genesis_block = Block(0, "Genesis Block", None)
        self.chain.append(genesis_block)
    
    def add_block(self, data):
        """Adds new block to the blockchain"""
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), data, previous_block)
        self.chain.append(new_block)
    
    def is_valid(self):
        """Verifies the integrity of the blockchain."""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            # Validate hash consistency
            if current_block.hash != current_block.calculate_hash():
                return False
            
            # Ensure proper linking between blocks
            if current_block.previous_block.hash != previous_block.hash:
                return False
        return True
    
    def display_chain(self):
        """Prints the blockchain."""
        for block in self.chain:
            print(block)

# Example usage
if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.add_block("Block 1")
    blockchain.add_block("Block 2")
    blockchain.add_block("Block 3")
    
    blockchain.display_chain()
    print("Is blockchain valid?", blockchain.is_valid())



'''Used: https://www.geeksforgeeks.org/python-linked-list/'''

'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Reference to the next node
# LinkedList class manages the nodes and operations of the linked list
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize an empty linked list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")
# Example usage:
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.print_list()
'''