from blockhain import WhonkoBlockhain
from p2p_network import P2PNode
import threading
import time

class WhonkoMiner
    def _init_(self, node: P2PNode, miner_address: str):
        self.node = node
        self.miner_address = miner_address
        self.mining = False
        self.mining_thread = None

    def start_mining(self):
        if self.mining:
            return

        self.mining = True
        self.mining_thread = threading.Thread(target=self.mine_loop)
        self.mining_thread.daemon = True
        self.mining_thread.start()
        print(f"Майнинг запущен для адреса: {self.miner_address}")

    def stop_mining(self):
        self.mining = False
        if self.mining_thread:
            self.mining_thread.join()
        print("Майнинг остановлен")

    def mine_loop(self):
        while self.mining:
            try:

                new_block = self.node.blockhain.mine_pending_transactions(self.miner_address)

                if new_block:

                    message = {
                        'type': 'block',
                        'block': new_block.to_dict()
                    }
                    self.node.broadcast_message(message)
                    print(f"Ошибка при майнинге: {e}")
                    time.sleep(5)
