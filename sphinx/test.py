from web3 import Web3, Account
from abi import riddle_abi
from starknet_py.net.gateway_client import GatewayClient
from starknet_py.net.networks import TESTNET, MAINNET

# Local network
from starknet_py.net.models import StarknetChainId

local_network_client = GatewayClient("http://localhost:5000", chain=StarknetChainId.TESTNET)

rpc = "xx"
private_key = "xx"
riddle_contract = "0x6bf20020ed923982030ae9dd99dd0b11dc92f6326fc20c5fcd21413e001c50"


def main():
    provider = Web3.HTTPProvider(rpc)
    print("status: ", provider.isConnected())
    w3 = Web3(provider)
    account = Account.from_key(private_key)
    nonce = w3.eth.get_transaction_count(account.address)

    riddle_con = w3.eth.contract(address=riddle_contract, abi=riddle_abi)

    random_con_addr = riddle_con.functions.random().call()
    # result = rand_con.functions.solve(4).transact()
    # 0x3c939a4f0e528526c472ae68c1416e95459e8da1549d3ebbddbe1a0875f4ef31


if __name__ == "__main__":
    main()
