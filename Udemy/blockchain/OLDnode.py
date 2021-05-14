from blockchain import Blockchain
from uuid import uuid4
from utility.verification import Verification
import random
from wallet import Wallet

class Node:

    def __init__(self):
        #self.wallet.public_key = str(uuid4())
        self.wallet = Wallet()
        self.wallet.create_keys()
        self.blockchain = Blockchain(self.wallet.public_key)

    def get_transaction_value(self):
        """ Returns the transaction inputs of the users """
        tx_recipient = input('Enter the recipient of the transaction : ')
        tx_amount = float(input('Input your transaction amount : '))
        return tx_recipient,tx_amount

    def get_user_choice(self):
        return input("Enter your option : ")


    def print_blockchain_elements(self):
        for block in self.blockchain.get_chain():
            print("Outputing blocks !")
            print(block)


    def listen_for_input(self):
    
        waiting_for_input = True

        while waiting_for_input:
            print("Select your option")
            print("1: Add user transaction amount")
            print("2: Mine Block")
            print("3: Output Blockchain")
            print("4: Check transaction validity")
            print("5: Create Keys")
            print("6: Load Keys")
            print("7: Save keys")
            print("q: Quit")
            user_choice = self.get_user_choice()
            if user_choice == "1":
                tx_data = self.get_transaction_value()
                recipient , amount =tx_data
                #Add new transaction to blockchain
                signature = self.wallet.sign_transaction(self.wallet.public_key,recipient,amount)
                if self.blockchain.add_transaction(recipient,self.wallet.public_key, signature ,amount=amount):
                    print("Added transaction!")
                else:
                    print("Transaction failed")
            elif user_choice == "2":
                if not self.blockchain.mine_block():
                    print("Mining Failed. Got no wallet?")
            elif user_choice == "3":
                self.print_blockchain_elements()
            elif user_choice == '4':
                if Verification.verify_transactions(self.blockchain.get_open_transactions(),self.blockchain.get_balance):
                    print("All transactions are valid")
                else:
                    print("There are invalid transactions")
            elif user_choice == '5':
                self.wallet.create_keys()
                self.blockchain = Blockchain(self.wallet.public_key)
            elif user_choice == '6':
                self.wallet.load_keys()
                self.blockchain = Blockchain(self.wallet.public_key)
            elif user_choice == "7":
                self.wallet.save_keys()
            elif user_choice == "q":
                waiting_for_input = False
            else:
                print("Pleasse enter the provided options")
            if not Verification.verify_chain(self.blockchain.get_chain()):
                self.print_blockchain_elements()
                print("Invalid Blockchain elements!")
                break
            print("Balance of {} : {:5.2f}".format(self.wallet.public_key ,self.blockchain.get_balance()))
        else:
            print("User Left!")

        print("Done!")

node = Node()
node.listen_for_input()