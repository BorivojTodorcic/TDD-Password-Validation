# Password Validation TDD Kata

This repository contains my implementation of the Password Validation Kata, which I completed as part of a TDD (Test-Driven Development) exercise during Codurance's weekly Coding Dojo sessions. The goal of this kata is to practice TDD principles by building a password validation feature incrementally, focusing on clean code and robust testing.


## Problem Statement - Iteration 1

Design and implement a software that validates a password applying TDD. The password will be introduced by the user (as an argument of the method) and should return if the password is valid or not.

A valid password should meet the following requirements:

- Have more than 8 characters
- Contains a capital letter
- Contains a lowercase
- Contains a number
- Contains an underscore
  

## How I approached the Kata

- Red: Start by writing a failing test for each rule.

- Green: Implement just enough code to make the test pass.

- Refactor: Clean up the code while ensuring all tests continue to pass.


## Technology Stack
- Language: [ Python ]
- Testing Framework: [ Unittest ]


## Running Tests

To run the tests and validate the password validator:

```bash
  python3 test_password.py
```


## Acknowledgements

 A huge thank you to Codurance for organising their weekly Software Crafters Manchester Meetups!
 
 - [Software Crafters Meetup](https://www.meetup.com/software-crafters-manchester/)
 - [Codurance Password Validation Kata](https://www.codurance.com/katas/password-validation)
