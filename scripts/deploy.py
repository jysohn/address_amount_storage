from scripts.helpful_scripts import get_account, get_contract
from brownie import Storage, network, config

def print_state():
    account = get_account()
    active_network = network.show_active()
    print(f"\nActive account is {account} and active network is '{active_network}'\n")

def deploy_storage():
    account = get_account()
    storage = Storage.deploy({"from": account})
    print("Storage deployed!\n")
    return storage

def main():
    print_state()
    deploy_storage()