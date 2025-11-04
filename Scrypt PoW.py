import hashlib
import time

class Scryptcoin:
    def _init_(self):
        self.chain = []
        self.difficulty = 8
    def mine_block(self, data):
        """
        майнинг блока с данными 'data' с использованием Scrypt.
        """
        nonce = 0
        prefix = '0' * self.difficulty

        while True:

            input_data = f"{data}{nonce}".encode()

            hash_result = hashlib.scrypt(
                input_data,
                salt=b'',
                n=4096,
                r=8,
                p=4,
                dklen=32
            ).hex()


            if hash_result.startswith(prefix):
                print(f"Найден nonce: {nonce}, хеш: {hash_result}")
                return nonce, hash_result

            nonce += 1
    def add_block(self, data):
        """
        добавляем новый блок в блокчейн.
        """
        start_time = time.time()
        nonce, block_hash = self.mine_block(data)
        mining_time = time.time() - start_time

        block = {
            'data': data,
            'nonce': nonce,
            'mining_time': mining_time
        }
        self.chain.append(block)
        print(f"Блок добавлен: {block}")
        

if '_name_' == "_main_":
    coin = ScryptCoin()
    coin.add_block("Транзакция 1: Андрей -> Боб (10 SCRYPT)")
    coin.add_block("Транзакция 2: Боб -> Кэрол (9 SCRYPT)")
