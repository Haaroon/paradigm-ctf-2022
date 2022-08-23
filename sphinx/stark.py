from starknet_py.net.gateway_client import GatewayClient
from starknet_py.net import AccountClient, KeyPair
from starknet_py.net.models.chains import StarknetChainId
from starknet_py.net.gateway_client import GatewayClient
from starknet_py.net.models import StarknetChainId
from starknet_py.contract import Contract
from starkware.crypto.signature.signature import private_to_stark_key
from starkware.starknet.core.os.contract_address.contract_address import calculate_contract_address_from_hash
from starkware.python.utils import to_bytes


def main():
    client = GatewayClient("xx", chain=StarknetChainId.TESTNET)

    key_pair = KeyPair.from_private_key(xx)
    player_public_key = private_to_stark_key(xx)
    player_address = calculate_contract_address_from_hash(
        salt=20,
        class_hash=1803505466663265559571280894381905521939782500874858933595227108099796801620,
        constructor_calldata=[player_public_key],
        deployer_address=0,
    )

    riddle_contract = "0x5f3b3f33d7ef43f7c3bc1f57487d6fb42a13ad4a5ff8218ba5f4861376c653f"

    account_client_testnet = AccountClient(
        client=client,
        address=player_address,
        key_pair=key_pair,
        chain=StarknetChainId.TESTNET,
    )

    contract = Contract.from_address_sync(riddle_contract, account_client_testnet)

    contract.functions["solve"].invoke_sync(7168366, max_fee=int(1e16))
    contract.functions["solution"].call_sync()
    return contract


def brute_force_me_lazy():
    for i in range(0, 1_000_000_000):
        if to_bytes(i).lstrip(b"\x00") == b"man":
            print(i)
            print("got em")
            break


if __name__ == "__main__":
    main()
