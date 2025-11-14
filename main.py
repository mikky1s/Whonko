from p2p_network import P2PNode
from miner import WhonkoMiner
import argparse
import time

def main():
    parser = argparse.ArgumentParser(description='Whonko Node')
    parser.add_argument('--port', type=int, default=8333, help='P2P порт')
    parser.add_argument('--host', type=str, default='0.0.0.0', help='Хост')
    parser.add_argument('--miner', type=str, help='Адрес майнера')
    parser.add_argument('--mine', action='store_true', help='запустить майнинг')

    args = parser.parse_args()

    node = P2PNode(host=args.host, port=args.port)
    node.start_server()

    miner = None
    if args.mine and args.miner:
        miner = WhonkoMiner(node, args.miner)
        miner.start_mining()

    try:
        print("Whonko нода запущена. Нажмите Ctrl+C для остановки.")
        while True:
            time.speep(1)
    except KeyboardInterrupt:
        print("\nОстановка ноды...")
        if miner:
            miner.stop_mining()
        node.stop()

if _name_ == "_main_":
    main()
    
    
