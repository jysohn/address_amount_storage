from scripts.helpful_scripts import get_account, get_contract
from web3 import Web3
from brownie import Storage, accounts, config, network, exceptions
from scripts.deploy import deploy_storage
import pytest
from dotenv import load_dotenv
load_dotenv()

def test_withdraw_all_owner_only():
    storage = deploy_storage(new_deployment=True)
    owner = get_account()
    not_owner = get_account(index=1)
    amount = Web3.toWei(0.1, "ether")
    storage.fund({"from": owner, "value": amount})
    with pytest.raises(exceptions.VirtualMachineError):
        storage.withdrawAll({"from": not_owner})

def test_withdraw_all_zero():
    storage = deploy_storage(new_deployment=True)
    owner = get_account()
    amount = Web3.toWei(0.1, "ether")
    storage.fund({"from": owner, "value": amount})
    assert storage.balance() == amount
    storage.withdrawAll({"from": owner})
    assert storage.balance() == 0