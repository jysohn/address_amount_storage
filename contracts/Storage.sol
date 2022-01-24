// SPDX-License-Identifier: MIT

pragma solidity ^0.6.6;
import "@openzeppelin/contracts/access/Ownable.sol";

contract Storage{
    mapping(address => uint256) public addressToAmountFunded;
    address[] public funders;
    address public owner;
    
    function fund() public payable {
        payable(address(this)).call{value:msg.value}("");
        addressToAmountFunded[msg.sender] = msg.value;
        funders.push(msg.sender);
    }

    function getAmountFunded() public returns (uint256) {
        return addressToAmountFunded[msg.sender];
    }

    function checkFunder() public returns (bool) {
        bool isFunder = false;
        for (uint256 funderIndex=0; funderIndex<funders.length; funderIndex++) {
            address funder = funders[funderIndex];
            if (funder == msg.sender) {
                isFunder = true;
            }
        }
        return isFunder;
    }
}