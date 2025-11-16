# 💠Whonko
**Whonko** — This is a **first-generation proof-of-work blockchain** built on the **Scrypt** algorithm.
It is designed for **miners** who believe that true decentralization begins with **computation, fairness, and transparency.**

🌐 Website: -

#  🛠 Core Features
+ ⚒ **Proof-of-Work Scrypt-based** is a proven consensus that ensures security and availability.

+ 💎 **Fixed supply (100 million WNK)** — limited issuance for long-term deficit and predictable inflation.

+ 🧱 **Dev fee** — 1%

+ 💰  **4% Premine** — allocated for team development, listing on exchanges, infrastructure, and the ecosystem.
 

#  📊 Emission Schedule
   BLOCKS                      ——————————                  REWARD (WNK)

1 → 210.000                   — 20 WNK/BLOCK                    

210.001 → 420.000             — 10 WNK/BLOCK

420.001 → 630.000             — 5 WNK/BLOCK

630.001 → 840.000             — 2.5 WNK/BLOCK

840.001 → 1.050.000           — 1.25 WNK/BLOCK

1.050.001 → 1.260.000         — 0.625 WNK/BLOCK

1.260.001 → 1.470.000         — 0.3125 WNK/BLOCK

1.470.001 → 1.680.000         — 0.15625 WNK/BLOCK

1.680.001 → 912.000.000       — 0.078125 WNK/BLOCK

Total — 96,000,000 WNK

# ⛏ System requirements
**Recommended**

+ **OS** — windows 10/linux

+ **Version python** — 3.14.x

+ **CPU** — Quad-Core 3.0 GHz+

+ **RAM** — 8 GB or more

+ **Storage** — NWMe SSD  150 ГБ+

+ **Network** — Stable high-speed connection

**Minimal**

+ **OS** — windows 10/linux

+ **Version python** — 3.12.x

+ **CPU** — Dual-Core 2.0 GHz

+ **RAM** — 4 GB

+ **Storage** — 50 GB free space (SSD recommended)

+ **Network** — Broadband

# 🚀 Getting Started
**🔧 Requirements**

+ Python 3.12.x - 3.14.x
+ pip (Python Package Manager)

**🔧 installing dependencies**
```
cryptography>=3.4.8
scrypt>=0.8.20
requests>=2.25.1
base58>=2.1.1
```
**🔧 Build from Source**
```bash
git clone https://github.com/your-username/whonko-blockchain.git
cd whonko-blockchain
pip install -r requirements.txt
```
**🌐 Run a Node**
```
python main.ру --stratum --stratum-port 3333 --port 8333
```
 **🔧 Creating a wallet**
 ```
python wallet_cli.ру new 
```
**⛏️ Start Mining**
```
python main.ру --miner "YOUR_WNK_ADDRESS" --mine --port 8334
```
**Configuring the miner**
```bash
# An example for ccminer (NVIDIA)
ccminer -a scrypt -o stratum+tcp://your-node:3333 -u YOUR_WNK_ADDRESS.worker1 -p x

# An example for sgminer (AMD)
sgminer --algorithm scrypt -o stratum+tcp://your-node:3333 -u YOUR_WNK_ADDRESS.worker1 -p x
```
**Wallet Commands**
```
# Create wallet
python wallet_cli.ру new

# Show information
python wallet_cli.ру info

# Check your balance
python wallet_cli.ру balance

# Send a WNK
python wallet_cli.ру send WNKrecipientaddress123 10.5

# Show transaction history
python wallet_cli.ру transactions
```
# 🧩 Chain Configuration
**Parameter**
+ Algorithm — Scrypt
+ Block time — 30 seconds
+ Premine — 4% (4M WNK)
+ Max Supply — 100M WNK
+ block reward — 20 WNK 


# Community 🌍
+ 📢  [Telegram news](https://t.me/whonkonews)
+ 💭 [Telegram group](https://t.me/whonkonews1) 


	




