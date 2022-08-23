setup_abi = '''
[
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [],
		"name": "challenge",
		"outputs": [
			{
				"internalType": "contract Challenge",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "isSolved",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]
'''

deployer_abi = '''
[
	{
		"inputs": [
			{
				"internalType": "bytes",
				"name": "code",
				"type": "bytes"
			}
		],
		"stateMutability": "nonpayable",
		"type": "constructor"
	}
]
'''

challenge_abi = '''
[
	{
		"inputs": [
			{
				"internalType": "bytes",
				"name": "code",
				"type": "bytes"
			}
		],
		"name": "solve",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "solved",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]
'''