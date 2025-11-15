import hashlib
import time
import json
from typing import list, dict, any
import theading
import socket
import pockle
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from  cryptography.hazmat.primitives import serialization
import scrypt

class WhonkoConfig:
    NAME = "Whonko"
    SYMBOL = "WNK"
    BLOCK_REWARD = 20.0
    BLOCK_TIME = 30
    DIFFICULTY_ADJUSTNENT_BLOCKS = 2016
    HALVING_BLOCKS = 210000 
    SUPPLY_CAP = 100000000
    PREMINE = 4000000
    MINEABLE = 96000000
    DEV_FEE_PERCENT = 0.01
    MINER_REWARD_PERCENT = 0.99

    DEV_ADDRESS = "вставить адрес разработчика"

    SCRYPT_N = 4096
    SCRYPT_R = 8
    SCRYPT_P = 4
    TARGET_BITS = 32

    P2P_PORT = 8333
    MAX_PEERS = 50
    CONNECTION_TIMEOUT = 30
    
