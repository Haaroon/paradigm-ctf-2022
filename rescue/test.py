from web3 import Web3, Account
from abis import *

rpc = "x"
private_key = "x"
Setup_addr = "0x00f4cAbc9B832e6647D36015271dF12cDD739c5C"
MasterChefLike_addr = "0xc2EdaD668740f1aA35E4D8f227fB8E17dcA888Cd"
UniswapV2RouterLike_addr = "0xd9e1cE17f2641f24aE83637ab66a2cca9C378B9F"
# 20:47


def main():
    provider = Web3.HTTPProvider(rpc)
    print("status: ", provider.isConnected())
    w3 = Web3(provider)
    account = Account.from_key(private_key)
    nonce = w3.eth.get_transaction_count(account.address)

    setup_con = w3.eth.contract(address=Setup_addr, abi=setup_abi)
    MasterChefLike_con = w3.eth.contract(address=MasterChefLike_addr, abi=mastercheflike_abi)
    UniswapV2RouterLike_con = w3.eth.contract(address=UniswapV2RouterLike_addr, abi=uniswapv2routerike_abi)
    weth_addr = setup_con.functions.weth().call()
    Weth_con = w3.eth.contract(address=weth_addr, abi=weth9_abi)
    mchelper_addr = setup_con.functions.mcHelper().call()
    mshelper_con = w3.eth.contract(address=mchelper_addr, abi=masterchefhelpeer_abi)
    print(setup_con.functions.isSolved().call())
    # result = rand_con.functions.solve(4).transact()
    # 0x3c939a4f0e528526c472ae68c1416e95459e8da1549d3ebbddbe1a0875f4ef31


if __name__ == "__main__":
    main()
