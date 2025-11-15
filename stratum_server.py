import socket
import thrading
import json
import time
import hashlib
import scrypt
from typing import dict, list, any
from blockhain import WhonkoBlockhain
from config import WhonkoConfig

class StratumServer:
    def _init_(self, host: = '0.0.0.0.', port: int = 3333, blockhain: WhonkoBlockhain = None):
        self.host = host
        self.port = port
        self.blockhain = blockhain or WhonkoBlockhain()
        self.miners: dict[str, dict] = {}
        self.jobs: dict[str, dict] = {}
        self.current_job_id = 0
        self.server_socket = None
        self.running = False

        self.shares_submitted = 0
        self.valid_shares = 0

    def start_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(100)
            self.running = True

            print(f"Stratum сервер запущен на {self.host}:{self.port}")

            job_thrad = threading.Thread(target=self.job_updater)
            job_thread.daemon = True
            job_thread.start()

            while self.running:
                client_socket, address = self.server_socket.accept()
                client_thread = threading.Thread(
                    target-self.handle_miner_connection,
                    args=(client_socket, address)
                )
                client_thread.daemon = True
                client_thread.start()

        except Exceptin as e:
            print(f"Ошибка запуска Stratum сервера:{e}")

    def handle_miner_connection(self, client_socket: socket.socket, address: tuple):
        miner_id = f"{address[0]}:{address[1]}"
        print(f"Майнер подключен: {miner_id}")

        try:

            welcome_msg = {
                "id": 1,
                "result": {
                    "difficulty": self.blockhain.difficulty,
                    "version": "1.0.0",
                    "motd": f"Welcome to Whonko Pool - {WhonkoConfig.NAME}"
                },
                "error": None
            }
            self.senf_message(client_socket, welcome_msg)

            buffer = ""
            while self.running:
                data = client_socket.recv(4096).decode('utf-8')
                if not data:
                    break

                buffer += data
                lines = buffer.split('\n')

                for line in lines[:-1]:
                    if line.strip():
                        self.process_miner_message(client_socket, miner_id, line.strip())

                    buffer = lines[-1]

                except Exception as e:
                    print(f"Ошибка соединения с майнером {miner_id}: {e}")
                finally:
                    client_socket.close()
                    if miner_id in self.miners:
                        del self.miners[miner_id]
                    print(f"Майнер отключен {miner_id}")

    def process_miner_message(self, client_socket: socket.socket, miner_id: str, message: str):
        try:
            data = json.loads(message)
            method = data.get('method')
            params = data.get('params', [])
            msg_id = data.get('id')

            if method == 'mining.subscribe':
                self.handle_subscribe(client_socket, miner_id, msg_id)
            elif method == 'mining.authorize':
                self.handle_authorize(client_socket, miner_id, params, msg_id)
            elif method == 'mining.submit':
                self.handle_submit(client_socket, miner_id, params, msg_id)
            elif method == 'mining.get_job':
                self.handle_get_job(client_socket, miner_id, msg_id)
                
        except json.JSONDecodeError:
            print(f"Неверный JSON от майнера {miner_id}")
    
    def handle_subscribe(self, client_socket: socket.socket, miner_id: str, msg_id: int):
        
        extranonce = hashlib.sha256(miner_id.encode()).hexdigest()[:8]
        
        self.miners[miner_id] = {
            'socket': client_socket,
            'extranonce': extranonce,
            'authorized': False,
            'worker': None,
            'difficulty': self.blockchain.difficulty,
            'shares': 0
        }
        
        response = {
            "id": msg_id,
            "result": [
                [
                    ["mining.set_difficulty", "00000001"],
                    ["mining.notify", "00000002"]
                ],
                extranonce,
                4
            ],
            "error": None
        }
        
        self.send_message(client_socket, response)
        
        self.send_new_job(miner_id)
    
    def handle_authorize(self, client_socket: socket.socket, miner_id: str, params: List, msg_id: int):
        if len(params) >= 2:
            worker_name = params[0]
            password = params[1]
            
            self.miners[miner_id]['authorized'] = True
            self.miners[miner_id]['worker'] = worker_name
            
            response = {
                "id": msg_id,
                "result": True,
                "error": None
            }
            
            print(f"Майнер авторизован: {worker_name} ({miner_id})")
        else:
            response = {
                "id": msg_id,
                "result": False,
                "error": "Invalid parameters"
            }
        
        self.send_message(client_socket, response)
    
    def handle_submit(self, client_socket: socket.socket, miner_id: str, params: List, msg_id: int):
        if miner_id not in self.miners or not self.miners[miner_id]['authorized']:
            return
        
        self.shares_submitted += 1
        
        try:
            worker_name = params[0]
            job_id = params[1]
            extranonce2 = params[2]
            ntime = params[3]
            nonce = params[4]
            
            if self.verify_share(miner_id, job_id, extranonce2, ntime, nonce):
                self.valid_shares += 1
                self.miners[miner_id]['shares'] += 1
                
                response = {
                    "id": msg_id,
                    "result": True,
                    "error": None
                }
                
                print(f"Валидная доля от {worker_name}. Всего долей: {self.valid_shares}")
            else:
                response = {
                    "id": msg_id,
                    "result": False,
                    "error": "Invalid share"
                }
                
        except Exception as e:
            response = {
                "id": msg_id,
                "result": False,
                "error": str(e)
            }
        
        self.send_message(client_socket, response)
    
    def verify_share(self, miner_id: str, job_id: str, extranonce2: str, ntime: str, nonce: str) -> bool:
        if job_id not in self.jobs:
            return False
        
        job = self.jobs[job_id]
        miner = self.miners[miner_id]
        
        header = (
            job['previous_hash'] +
            job['merkle_root'] +
            ntime +
            job['bits'] +
            nonce +
            miner['extranonce'] +
            extranonce2
        )
        
        hash_result = scrypt.hash(
            header.encode(),
            salt=b'whonko',
            N=WhonkoConfig.SCRYPT_N,
            r=WhonkoConfig.SCRYPT_R,
            p=WhonkoConfig.SCRYPT_P
        )
        
        hash_hex = hash_result.hex()
        
        share_target = 2 ** (256 - miner['difficulty'])
        return int(hash_hex, 16) < share_target
    
    def handle_get_job(self, client_socket: socket.socket, miner_id: str, msg_id: int):
        self.send_new_job(miner_id)
    
    def send_new_job(self, miner_id: str):
        if miner_id not in self.miners:
            return
        
        latest_block = self.blockchain.get_latest_block()
        self.current_job_id += 1
        job_id = str(self.current_job_id)
        
        job = {
            'job_id': job_id,
            'previous_hash': latest_block.hash,
            'merkle_root': '0' * 64,
            'version': '00000002',
            'bits': f"{self.blockchain.difficulty:08x}",
            'timestamp': int(time.time()),
            'clean_jobs': True
        }
        
        self.jobs[job_id] = job
        
        notify_msg = {
            "id": None,
            "method": "mining.notify",
            "params": [
                job_id,
                job['previous_hash'],
                job['merkle_root'],
                job['version'],
                job['bits'],
                job['timestamp'],
                job['clean_jobs']
            ]
        }
        
        self.send_message(self.miners[miner_id]['socket'], notify_msg)
    
    def job_updater(self):
        while self.running:
            time.sleep(10)
            
            for miner_id in list(self.miners.keys()):
                try:
                    self.send_new_job(miner_id)
                except Exception as e:
                    print(f"Ошибка отправки задания майнеру {miner_id}: {e}")
    
    def send_message(self, client_socket: socket.socket, message: dict):
        try:
            client_socket.send((json.dumps(message) + '\n').encode('utf-8'))
        except Exception as e:
            print(f"Ошибка отправки сообщения майнеру: {e}")
    
    def stop(self):
        self.running = False
        if self.server_socket:
            self.server_socket.close()
            
            
