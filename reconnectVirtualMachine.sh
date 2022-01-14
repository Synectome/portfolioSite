#!/bin/bash
ip link set ens33 up
dhclient ens33 -v