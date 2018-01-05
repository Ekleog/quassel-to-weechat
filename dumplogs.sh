#!/bin/sh

mkdir logs

./networks.sh "$1" | while read net; do
    echo "Dumping logs for network '$net'"
    mkdir "logs/$net"
    ./chans.sh "$1" "$net" | while read chan; do
        echo "    Dumping logs for channel '$chan'"
        if [ -n "$chan" ]; then
            ./logs.sh "$1" "$net" "$chan" | ./logs.py "$chan" > "logs/$net/${chan}.weechatlog"
        else
            ./logs.sh "$1" "$net" "$chan" | ./logs.py "$chan" > "logs/${net}.weechatlog"
        fi
    done
done
