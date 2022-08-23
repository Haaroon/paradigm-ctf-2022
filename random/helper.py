from web3 import Web3, Account
from abi import *

rpc = "xx"
private_key = "xx"
setup_contract = "0xDB92Efa0B0eeC9d65290aC8A98154b685131dcD0"


def main():
    provider = Web3.HTTPProvider(rpc)
    print("status: ", provider.isConnected())
    w3 = Web3(provider)
    account = Account.from_key(private_key)
    nonce = w3.eth.get_transaction_count(account.address)

    setup_con = w3.eth.contract(address=setup_contract, abi=setup_abi)
    random_con_addr = setup_con.functions.random().call()
    rand_con = w3.eth.contract(address=random_con_addr, abi=random_abi)
    result = rand_con.functions.solve(4).transact()
    # 0x3c939a4f0e528526c472ae68c1416e95459e8da1549d3ebbddbe1a0875f4ef31
    setup_con.functions.isSolved().call()


if __name__ == "__main__":
    main()
