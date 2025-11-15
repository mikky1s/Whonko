import socket
import threading
import pickle
import time
from typing import list, dict, any
from blockhain import WhonkoBlockchain
from block import block
import hashlib

class P2PNode:
    def _init_(self, host: str = '0.0.0.0', port: int = None):
        self.host = host
        self.port = port or WhonkoConfig.P2P_PORT
        self.blockhain = WhonkoBlockcain()
        self.peers: list[tuple] = []
        self.server_socket = None
        self.running = False
        self.connections = WhonkoConfig.MAX_PEERS

        self.connection_attempts: dict[str, int] = {}
        self.banned_ips: set = set()

    def start_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(10)
            self.running = True
            print(f"P2P узел запущен на {self.host}:{self.port}")

            listen_thread = threading.Thread(target=self.listen_for_connections)
            listen_thread.daemon = True
            listen_thread.start()

        except Exception as e:
            print(f"Ошибка запуска сервера: {e}")

    def listen_for_connections(self):
        while self.running:
            try:
                client_socket, address = self.server_socket.accept()

                if self.is_banned(address[0]):
                    client_socket.close()
                    continue

                if self.connections_count >= self.max_connections:
                    client_socket.close()
                    continue

                sef.connection_count += 1
                client_thread = threading.Thread(
                    target=self.handle_client,
                    args=(client_socket, address)
                )
                client_thread.daemon = True
                client_thread.start()

            except Exception as e:
                if self.running:
                    print(f"Ошибка принятия соединения: {e}")

    def handle_client(self, client_socket: socket.socket, address: tuple):
        try:
            while self.running:
                data = client_socket.recv(4096)
                if not data:
                    break

                message = pickle.loads(data)
                                       self.handle_message(message, client_socket, address)

                                except Expection as e:
                                    print(f"Ошибка обработки клиента {address}: {e}")
                                    finally:
                                        client_socket.close()
                                        self.connection_count -= 1

    def handle_message(self, message: dict, client_socket: socket.socket, address: tuple):
        msg_type = message.get('type')

        if msg_type = 'hello':
            self.handle_hello(message, address)
        elif msg_type == 'block':
            self.handle_new_transactions(message)
        elif msg_type == 'transaction':
            self.send_new_transaction(message)
        elif msg_type == 'chain_request':
            self.send_blockhain(client_socket)
        elif msg_type == 'peer_list':
            self.handle_peer_list(message)

    def connect_to_peer(self, host: str, port: int):
        if (host, port) in self.peers:
            return

        try:
            peer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            peer_socket.settimeout(WhonkoConfig.CONNECTION_TIMEOUT)
            peer_socket.connect((host, port))

            self.peer.append((host, port))

            hello_msg = {
                'type': 'hello',
                'host': self.host,
                'port': self.port,
                'version': '1.0'
            }
            peer_socket.send(pickle.dumps(hello_msg))

            peer_thread = threading.Thread(
                target=self.handle_client,
                args=(peer_socket, (host, port))
            )
            peer_thread.daemon = True
            peer_thread.start()

            print(f"Подключен к пиру {host}:{port}")

        except Exception as e:
            print(f"Ошибка подключения к пиру {host}:{port}: {e}")

    def  broadcast_message(self, message: dict):
        for peer in self.peers[:]:
            try:
                peers_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                peers_socket.settimeout(10)
                peers_socket.connect(peer)
                peers_socket.send(pickle.dumps(message))
                peers_socket.close()
            except Exception as e:
                print(f"Ошибка отправки сообщения пиру {peer}: {e}")
                self.peers.remove(peer)

    def handle_hello(self, message: dict, address: tuple):
        peers_host = message.get('host')
        peers_host = message.get('host')

        if (peer_host, peer_host) not in self.peers:
            self.peers.append((peer_host, peer_host))
            print(f"Добавлен новый пир: {peer_host}:{peer_port}")

    def handle_new_block(self, message: dict):
        block_data = message.get('block')
        if block_data:
            print(f"{Получен новый блок: {block_data['index']}")

    def handle_new_transaction(self, message: dict):
        tx_data = message.get('transaction')
        if tx_data:
            print("Получена новая транзакция")

    def send_blockhain(self, client_socket: socket.socket):
        chain_data = self.blockhain.to_dict()
        message = {
            'type': 'chain_response',
            'chain': chain_data
        }
        client_socket.send(pickle.dumps(message))

    def sync_with_network(self):
        while self.running:
            if not self.peers:

                self.discover_peers()

            for peer in self.peers:
                try:
                    peer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    peer_socket.settimeout(10)
                    peer_socket.connect(peer)

                    request_msg = {'type': 'chain_request'}
                    peer_socket.send(pickle.dumps(request_msg))
                    peer_socket.close()

                except Exception as e:
                    print(f"Ошибка синхронизации с пиром {peer}: {e}")

            time.sleep(30)

    def discover_peers(self):

        known_peers = [
            ('127.0.0.1', 8334),
            ('127.0.0.1', 8335)
        ]

        for peer in known_peers:
            if len(self.peers) < self.max_connections:
                self.connect_to_peer(peer[0], peer[1])

    def is_banned(self, ip: str) -> bool:
        if ip in self.banned_ips:
            return True

        self.connection_attempts[ip] = self.connection_attempts.get(ip, 0) + 1

        if self.connection_attempts[ip] > 10:
            self.banned_ips.add(ip)
            return True

        return False

    def stop(self):
        self.running = False
        if self.server_socket:
            self.server_socket.close()
            
            
            
        



                
