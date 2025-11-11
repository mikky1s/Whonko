from block import Block, Transaction
from config import Whonkoconfig
import time
import json
import threading

class WhonkoBlockchain
    def _init_(self):
        self.chain: List[Block] = []
        self.pending_transactions: List[Transaction] = []
        self.difficulty = Whonkoconfig.TARGET_BITS
        self.mining_reward = WhonkoConfig.BLOCK_REWARD
        self.chain_lock = threading.Lock()
        self.create_genesis_block()

    def create_genesis_block(self):
        premine_tx = Transaction(
            sender="0"
            recipient=WhonkoConfig.DEV_ADDRESS,
            amount=WhonkoConfig.PREMINE

        )
        genesis_block.mine_block()

        with self.chain_lock:
            self.chain.append(genesis_block)

    def get_latest_block(self) -> Block:
        return self.chain[-1]

    def get_current_reward(self) -> float:
        current_height = len(self.chain)
        halvings = current_height // WhonkoConfig.HALVING_BLOCKS

        if current_height >= 1680000:
            if current_height <= 912000000:
                return 0.078125
            else:
                return 0

        reward = WhonkoConfig.BLOCK_REWARD
        for _ in range(halvings):
            reward /= 2

        return

    def calculate_miner_reward(self, block_reward: float) -> tuple:
        dev_fee = block_reward * WhonkoConfig.DEV_FEE_PERCENT
        return miner_reward, dev_fee

    def add_transaction(self, transaction: Transaction) -> bool:

        if transaction.amount <= 0:
            return False

        with self.chain_lock:
            self.pending_transactions.append(transaction)
        return True

    def mine_pending_transactions(self, miner_address: str) -> Block:
        block_reward = self.get_current_reward()
        miner_reward, dev_fee = self.calculate_miner_reward(block_reward)

        miner_tx = Transactions(
            sender="0",
            recipient=miner_address,
            amount=miner_reward
        )

        if dev_fee > 0:
            dev_tx = Transaction(
                sender="0"
                recipient=WhonkoConfig.DEV_ADRESS,
                amount=dev_fee
            )
            self.pending_transactions.append(dev_tx)

        self.pending_transactions.append(miner_tx)

        latest_block = self.get_latest_block()
        new_block = Block(
            index=len(self.chain),
            previous_hash=latest_block.hash,
            timestamp=time.time(),
            transactions=self.pending_transactions.copy(),
            difficulty=self.difficulty
        )

        print(f"Майнинг блока {new_block.index}...")
        new_block.mine_block()
        print(f"Блок найден! Хеш: {new_block.hash}")

        with self.chain_lock:
            if self.add_block(new_block):
                self.pending_transactions = []
                self.adjust_difficulty()
                return new_block
            else:
                return None

        def add_block(self, new_block: Block) -> bool:
            latest_block = self.get_latest_block()

            if new_block.previous_hash != latest_block.hash:
                return False

            if new_block.index != latest_block.index + 1:
                return False

            if not new_block.is_valid():
                return False

            if len(self.chain) >= 6:
                pass

            with self.chain_lock:
                self.chain.append(new_block)

            return True

        def adjust_difficulty(self):
            if len(self.chain) % WhonkoConfig.DIFFICULTY_ADJUST_BLOCKS == 0:
                adjustment_block = self.chain[-WhonkoConfig.DIFFICULTY_ADJUSTMENT_BLOCKS]
                time_taken = self.get_latest_block().timestamp - adjustment_block.timestamp
                expected_time = WhonkoConfig.BLOCK_TIME * WhonkoConfig.DIFFICULTY_ADJUSTMENT_BLOCKS

                if time_taken < expected_time / 2:
                    self.difficulty += 1
                elif time_taken > expected_time * 2:
                    self.difficulty = max(1, self.difficulty - 1)

                print(f"Сложность скорректирована: {self.difficulty}")

        def is_chain_valid(self) -> bool:
            for i in range(1, len(self.chain)):
                current_block = self.chain[i]
                previous_block = self.chain[i - 1]

                if current_block.previous_hash != previous_block.hash:
                    return False

                if not current_block.is_valid():
                    return False

                return True

        def get_balance(self, address: str) -> float:
            balance = 0.0

            for block in self.chain:
                for tx in block.transactions:
                    if tx.recipient == address:
                        balance += tx.amount
                    if tx.sender == address:
                        balance -= tx.amount

            for tx in self.pending_transactions:
                if tx.sender == address:
                    balance -= tx.amount

            return balance

        def to_dict(self) -> dict:
            return {
                'chain': [block.to_dict() for block in self.chain],
                'pending_transactions': [tx.to_dict() for tx in self.pending_transactions],
                'difficulty': self.difficulty,
                'total_supply': self.get_total_supply()
            }

        def get_total_supply(self) -> float:
            total = WhonkoConfig.PREMINE
            for block in self.chain:
                for tx in block.transactions:
                    if tx.sender == "0":
                        total += tx.amount
            return min(total, WhonkoConfig.SUPPLY_CAP)
        
                             
                
                
            
            

        
        
