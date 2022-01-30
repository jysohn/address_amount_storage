from scripts.helpful_scripts import get_account, get_contract
from brownie import Storage, network, config
from web3 import Web3

def print_state():
    account = get_account()
    active_network = network.show_active()
    print(f"\nActive account is {account} and active network is '{active_network}'\n")

def deploy_storage(new_deployment=False):
    account = get_account()
    # return latest contract
    if (new_deployment==False):
        if (Storage[-1]):
            print(f"Storage exists at {Storage[-1]}\n")
            return Storage[-1]
        # deploy new contract if none exists
        else:
            print("No previous Storage exists, deploying now...")
            storage = Storage.deploy(
                {"from": account},
                publish_source=config["networks"][network.show_active()]["verify"]
            )
            print("Storage deployed!\n")
            return storage
    
    # return latest contract
    else:
        print("Deploying new Storage contract...")
        storage = Storage.deploy(
                {"from": account},
                publish_source=config["networks"][network.show_active()]["verify"]
        )
        print("Storage deployed!\n")
        return storage

def check_funder():
    account = get_account()
    storage = Storage[-1]
    is_funder = storage.checkFunder({"from": account})
    is_funder.wait(1)

def check_amount_funded():
    account = get_account()
    storage = Storage[-1]
    amount_funded = storage.getAmountFunded({"from": account})
    amount_funded_in_eth = amount_funded / (10**18)
    print(f"amount funded is: {amount_funded_in_eth} ETH")
    return amount_funded

def fund_storage():
    account = get_account()
    storage = Storage[-1]
    value = Web3.toWei(0.1, "ether")
    fund_tx = storage.fund({"from": account, "value": value})
    fund_tx.wait(1)

def withdraw_all_storage():
    account = get_account()
    storage = Storage[-1]
    withdraw_tx = storage.withdrawAll({"from": account})
    withdraw_tx.wait(1)

def withdraw_some_storage(amount_eth_to_withdraw):
    account = get_account()
    storage = Storage[-1]
    withdraw_tx = storage.withdrawSome(amount_eth_to_withdraw, {"from": account})
    withdraw_tx.wait(1)

def main():
    print_state()
    deploy_storage(new_deployment=True)
    fund_storage()
    check_amount_funded()
    withdraw_some_storage(0.01)
    check_amount_funded()
    print("done")