import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"

	headers = {
		"Content-Type": "application/json",
		"pinata_api_key": "acb2ac4b035afad96c56",
		"pinata_secret_api_key": "8f89a3524c94e9bf1c38e09a61cf62f634d8a040cb36b963338c9bbd3e5310e3"
	}

	payload = {
		"pinataContent": data,
		"pinataMetadata": {
			"name": "blockchain_assignment_data"
		}
	}
	try:
		response = requests.post(url, json=payload, headers=headers)
		response.raise_for_status()
		result = response.json()
		cid = result["IpfsHash"]
		return cid
	except requests.exceptions.RequestException as e:
		print(f"Error pinning to IPFS: {e}")
		if hasattr(e, 'response') and e.response is not None:
			print(f"Response: {e.response.text}")
		return None

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE
	if not cid:
		print("Error: CID is empty or None")
		return {}
	url = f"https://gateway.pinata.cloud/ipfs/{cid}"

	try:
		response = requests.get(url)
		response.raise_for_status()
		data = response.json()
		assert isinstance(data, dict), f"get_from_ipfs should return a dict"
		return data

	except requests.exceptions.RequestException as e:
		print(f"Error retrieving from IPFS: {e}")
		return {}

	except json.JSONDecodeError as e:
		print(f"Error parsing JSON from IPFS: {e}")
		return {}