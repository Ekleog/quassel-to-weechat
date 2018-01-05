#!/bin/sh

./sql.sh "select type, flags, time, sender, message from backlog
join buffer on buffer.bufferid = backlog.bufferid
join network on network.networkid = buffer.networkid
join quasseluser on quasseluser.userid = network.userid
join sender on sender.senderid = backlog.senderid
where buffer.buffername = '$3'
and network.networkname = '$2'
and quasseluser.username = '$1'" | head -n -2 | tail -n +3
