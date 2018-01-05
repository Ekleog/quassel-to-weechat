#!/bin/sh

./sql.sh "select username from quasseluser" | egrep '^ ' | sed 's/ //' | egrep -v '^ '
