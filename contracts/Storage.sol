// SPDX-License-Identifier: MIT

pragma solidity ^0.6.6;

contract Storage{
    mapping(address => uint256) public addressToAmountFunded;
    address[] public funders;
    event isFunderCheck(bool isFunder);
    
    function fund() public payable {
        payable(address(this)).call{value:msg.value}("");
        addressToAmountFunded[msg.sender] = msg.value;
        funders.push(msg.sender);
    }

    function withdrawAll() public payable {
        msg.sender.transfer(address(this).balance);
    }

    function getAmountFunded() public returns (uint256) {
        return addressToAmountFunded[msg.sender];
    }

    function checkFunder() public {
        bool isFunder = false;
        for (uint256 funderIndex=0; funderIndex<funders.length; funderIndex++) {
            address funder = funders[funderIndex];
            if (funder == msg.sender) {
                isFunder = true;
            }
        }
        emit isFunderCheck(isFunder);   
    }
}