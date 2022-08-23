from web3 import Web3, Account
from abis import *
rpc = "xx"
private_key = "xx"
Setup_addr = "0x2dFBD5cb07c163d7397806300B70077f17710652"
# 22:52

def main():
    provider = Web3.HTTPProvider(rpc)
    print("status: ", provider.isConnected())
    w3 = Web3(provider)
    account = Account.from_key(private_key)
    nonce = w3.eth.get_transaction_count(account.address)  
,
    setup_con = w3.eth.contract(address=Setup_addr, abi=setup_abi)
    chall_addr = setup_con.functions.challenge().call()
    chal_con = w3.eth.contract(address=chall_addr, abi=challenge_abi)

    result = setup_con.functions.solve(4).transact()
    

if __name__ == '__main__':
    main()