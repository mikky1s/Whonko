from config import WhonkoConfig
import hashlib
import time
import json

class Transaction:
    def _inint_(self, sender: str, recipient: str, amount: float, fee: float = 0.0):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.fee = fee
        self.timestamp = time.time()
        self.signature = None
        self.tx_hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        data = f"{self.sender}{self.recipient}{self.amount}{self.fee}{self.timestamp}"
        return hash.sha256(data.encode()).hexdigest()

    def to_dict(self) -> dict:
        return {
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount,
            'fee': self.fee,
            'timestamp': self.timestamp,
            'tx_hash': self.tx_hash,
            'signature': self.signature
        }
class Block:
    def _init_(self, index: int, previous_hash: str, timestamp: float,
               transactions: list[transaction], nonce: int = 0,
               difficulty: int = WhonkoConfig.TARGET_BITS):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.nonce = nonce
        self.difficulty = difficulty
        self.merkle_root = self.calculate_merkle_root()
        self.hash = self.calculate_hash()

    def calculate_merkle_root(self) -> str:
        if not self.tansactions:
            return hashlib.sha256(b"").hexdigest()

        tx_hashes = [tx.tx_hash for tx  in self.transactions]

        while len(tx_hashes) > 1:
            new_hashes = []
            for i in range(0, len(tx_hashes), 2):
                if i + 1 < len(tx_hashes):
                    combined = tx_hashes[i] + tx_hashes[i + 1]
                else:
                    combined = tx_hashes[i] + tx_hashes[i]
                new_hashes.append(hashlib.sha256(combined.encode()).hexdigest())
            tx_hashes = new_hashes

        return tx_hashes[0]

    def caalculate_hash(self) -> str:
        block_data = {
            'index': self.index,
            'previous_hash': self.previous_hash,
            'timestamp': self.timestamp,
            'merkle_root': self.mercke_root,
            'nonce': self.nonce,
            'difficulty': self.difficulty
        }
        block_string = json.dumps(block_data, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self):
        target = 2 ** (256 - self.difficulty)
        while int(self.hash, 16) >= target:
            self.nonce += 1

            block_data = f"{self.index}{self.previous_hash}{self.timestamp}{self.merkle_root}{self.nonce}"
            self.hash = scrypt.hash(block_data.encode(),
                                    salt=b'whonko'
                                    N=WhonkoConfig.SCRYPT_N,
                                    r=WhonkoConfig.SCRYPT_R,
                                    P=WhonkoConfig.SCRYPT_P)
            self.hash = self.hash.hex()

    def to_dict(self) -> Dict:
        return {
            'index': self.index,
            'previous_hash': self.previous_hash,
            'timestamp': self.timestamp,
            'transactions': [tx.to_dict() for tx in self.transactions],
            'nonce': self.nonce,
            'difficulty': self.difficulty,
            'merkle_root': self.merkle_root,
            'hash': self.hash
        }

    def is_valid(self) -> bool:
        if self.hash != self.calculate_hash():
            return False
        target = 2 ** (256 - self.difficulty)
        if int(self.hash, 16) >= target:
            return False

        return True
        
            
            
                                    
        
        
    
                
        
        
