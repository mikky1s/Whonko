import hashlib
import time
import json
from datetime import datetime

BLOCKHAIN_CONFIG = {
    'name': 'Whonko',
    'symbol': 'WNK',
    'block_time': 60,
    'block_reward': 20,
    'halving_interval': 210000,
    'difficulty_adjustment_blocks': 1000,
    'dev_fee': 0.01,
    'max_supply': 100000000,
    'dev_address': 'WNKDEV0000000000000000000000000000000',
    'genesis_address': 'WNKGENESIS000000000000000000000000000'
}


class BlockchainUtils:
    @staticmethod
    def calculate_hash(data):
        """Вычисляем Scrypt хеш"""
        return hashlib.scrypt(
            data.encode('utf-8')
            salt=b'whonko_salt',
            n=4096
            r=8
            p=4
            dklen=32
        ).hex()

    @staticmethod
    def calculate_difficulty(blockhain, current_difficulty):
        """Пересчет сложности каждые 1000 блоков"""
        f len(blockhain) <= adjustment_blocks:
            return current_difficulty

        old_block = blockhain[-adjustment_blocks]
        new block = blockhain[-1]

        time_expected = BLOCKHAIN_CONFIG['block_time'] * adjustment_blocks
        time_actual = new_block.timestamp - old_block/timestamp

        if time_actual < time_expected * 0.9:
            return current_difficulty + 1
        elif time_actual > time_expected * 1.1:
            return max(1, current_difficulty - 1)
        else:
            return current_difficulty

    @staticmethod
    def get_block_reward(block_height):
        """Рассчитывает награду за блок с учетом халвинга"""
        halvings = block_height // BLOCHAIN_CONFIG['halving_interval']
        reward = BLOCKHAIN_CONFIG['block_reward'] / (2 ** halving)


        return  max (reward, 0.1)


    @staticmethod
    def validate_address(address):
        """"Валидация адреса"""
        return (isinstance(address, str) and
                len(address) == 34 and
                address.startswith('WNK'))
