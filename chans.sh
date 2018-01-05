#!/bin/sh

./sql.sh "select buffername from buffer join quasseluser on quasseluser.userid = buffer.userid join network on network.networkid = buffer.networkid where quasseluser.username = '$1' and network.networkname = '$2'" | egrep '^ ' | sed 's/ //' | egrep -v '^ '
