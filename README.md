# Network Tools (configuration)

A library to help with easy configuration of Network connections.
It is basically a wrapper of shell functions used for configuring 
Network device settings on debian distros.

| Functions |
|-----------|
|Change eth0 to use a static address|
|Change wlan0 to use a static address|
|Check comms protocol of devices on the network|
|Disable DHCPD if NetworkManager is functional
|get available network addresses|


## Tools

-[Auth_SSID](#installation)
- [NetworkWizard](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#GPL)


###Auth_SSID.py
Tool is used to verify that a given wireless ssid is currently accessible
it exits with:
    VALID_SSID = 120,
    INVALID_SSID = -120,
    PROCESS_ERROR = -10,
    FEW_ARGS = -121,
it is meant to be used as a subprocess.

