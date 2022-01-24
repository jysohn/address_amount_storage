from scripts.helpful_scripts import get_account, get_contract
from brownie import Storage, network, config

def print_state():
    account = get_account()
    active_network = network.show_active()
    print(f"\nActive account is {account} and active network is '{active_network}'\n")

def deploy_storage(new_deployment=False):
    account = get_account()
    if (new_deployment==False):
        if (Storage[-1]):
            print(f"Storage exists at {Storage[-1]}\n")
            return Storage[-1]
        else:
            print("No previous Storage exists, deploying now...")
            storage = Storage.deploy(
                {"from": account},
                publish_source=config["networks"][network.show_active()]["verify"]
            )
            print("Storage deployed!\n")
            return storage
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
    return is_funder

def check_amount_funded():
    pass

def main():
    print_state()
    deploy_storage(new_deployment=True)
    should_be_false = check_funder()
    print(f"should be false = {should_be_false}")