from main import WhonkoNode


if _name_ == "_main_":
    node = WhonkoNode(port=3555, mining=True)
    node.set_miner_address("WNKMINER00000000000000000000000000000")
    node.start()
