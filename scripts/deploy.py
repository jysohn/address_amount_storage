from scripts.helpful_scripts import get_account, get_contract
from brownie import Storage, network, config

def print_state():
    account = get_account()
    active_network = network.show_active()
    print(f"\nActive account is {account} and active network is '{active_network}'\n")

def deploy_storage():
    account = get_account()
    #if (Storage[-1]):
    #    print(f"Storage exists at {Storage[-1]}\n")
    #    return Storage[-1]
    storage = Storage.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"]
    )
    print("Storage deployed!\n")
    return storage

def check_storage():
    account = get_account()
    storage = Storage[-1]
    check_funder = False
    for a in storage.funders:
        if a == account:
            check_funder = True
    return (check_funder, storage.addressToAmountFund[account])

def main():
    print_state()
    deploy_storage()
    check_storage()