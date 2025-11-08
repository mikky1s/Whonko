import json
import hashlib
from config import BlockhainUtils, BLOCKHAIN_CONFIG

class Transaction:
    def _init_(self, sender, recipient, amount, fee=0.0, timestamp=None):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.fee = fee
        self.timestamp = timestamp or time.time()
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """Вычисляем хеш траназкции"""
        transaction_data = {
             'sender': self.sender,
             'recipient': self.recipient,
             'amount': self.amount,
             'fee': self.fee,
             'timestamp': self.timestamp
        }
        return BlockhainUtils.calculate_hash(json.dumps(transaction.data, sort_keys=True))

    def to_dict(self):
        return {
            'hash': self.hash,
            'sender':self.sender,
            'recipient': self.recipient,
            'amount': self.amount,
            'fee': self.fee,
            'timestamp': self.timestamp
        }
    def is_coinbase(self):
        """Проверяетб является ли транзаккция coinbase (наградой за блок)"""
        return self.sender == 'coinbase'

    def is_def_fee(self):
        """Проверяетб является ли транзакция комиссией разработчикам"""
        return self.recipient == BLOCKHAIN_CONFIG['dev_address']

class TransactionPool:
    def _init_(self):
        self.transactions = []

    def add_transaction(self, transaction):
        """Добавляем транзакцию в пул"""
        if self.validate_transaction(transaction):
            self.transaction.append(transaction)
            return True
        return False

    def validate_transaction(self, transaction):
        """Валидирует транзакцию"""

        if not (BlockhainUtils.validate_address(transaction.recipient) and
                (transaction.sender == 'coinbase' or
                 BlockhainUtils.validate_address(transaction.sender))):
            return False

        if transaction.hash != transaction.calculate_hash():
            return False

        return True

    def get_transactions_for_block(self):
        """Возвращает транзакции для включения в блок"""
        sorted_tx = sorted(self.transactions, key= lambda x: x.fee, reverse=True)
        return sorted_tx[:100]

    def remove_transactions(self, transactions):
        """Удаляет транзакции из пула после включения в блок"""
        tx_hashes = [tx.hash for tx in transactions]
        self.transactions = [tx for tx in self.transactions if tx.hash not in tx_hashes]
             
            
            
