# modbus-pypoll
Non-sophisticated Modbus Poll written in Python

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Usage](#usage)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
- How does this script work? It simply performs data receiving for 100 times using the IP address, port, and device number specified in the command line.


## Technologies Used
- Python 3.10 + os and sys modules from the Python Standart Library

## Usage

First, I recommend making an alias for this script in your Linux system:

`alias modbus='python3 /path/to/modbus.py'`, or whatever.

This allows you to use it as a command in the Terminal.

Example of usage:

```
modbus 172.16.30.51 502 10 1175 1

modbus <IP address> <port> <device number> <data address> <data lengh>

```

The script performs 100 poll iterations by default. You can interrupt it by pressing 'Ctrl+C'.

## Contact
Created by dyedfox - feel free to contact me via GitHub!