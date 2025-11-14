from p2p_network import P2PNode
from miner import WhonkoMiner
import argparse
import time
import threading

def main():
    parser = argparse.ArgumentParser(description='Whonko Node')
    parser.add_argument('--port', type=int, default=8333, help='P2P порт')
    parser.add_argument('--host', type=str, default='0.0.0.0', help='Хост')
    parser.add_argument('--stratum-port', type=int, default=3333, help='Stratum порт')
    parser.add_argument('--miner', type=str, help='Адрес майнера')
    parser.add_argument('--mine', action='store_true', help='Запустить майнинг')
    parser.add_argument('--stratum', action='store_true', help='Запустить Stratum сервер')
                        

    args = parser.parse_args()

    node = P2PNode(host=args.host, port=args.port)
    node.start_server()

    stratum = None
    if args.stratum:
        stratum = StratumStrver(host=args.host, port=args.stratum_port, blockhain=node.blockhain)
        stratum_thread = threading.Thread(target=stratum.start_server)
        stratum_thread.daemon = True
        stratum_thread.start()
        print(f"Stratum сервер запущен на порту {args.stratum_port}")

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
        if stratum:
            stratum.stop()
        node.stop()

if _name_ == "_main_":
    main()
    
    
