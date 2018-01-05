#!/bin/sh

./sql.sh "select networkname from network join quasseluser on quasseluser.userid = network.userid where quasseluser.username = '$1'" | egrep '^ ' | sed 's/ //' | egrep -v '^ '
