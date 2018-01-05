# Quassel-to-WeeChat

Takes logs out from the Quassel database towards the WeeChat log format.

Usage: `./dumplogs.sh USERNAME` will take all the logs of `USERNAME` and dump
them to the directory `logs`.

Please note these scripts were designed to help migrate from Quassel to WeeChat,
they are *NOT* designed with security in mind, and there are most likely
multiple ways to trick the exporter to generate wrong messages!
