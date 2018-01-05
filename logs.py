#!/usr/bin/python3

import sys

chan = sys.argv[1]

def outmessage(time, sender, message):
    print("%s\t%s\t%s" % (time, sender[0], message))

def outnotice(time, sender, message):
    print("%s\t--\tNotice(%s): %s" % (time, sender[0], message))

def outaction(time, sender, message):
    print("%s\t*\t%s %s" % (time, sender[0], message))

def outnick(time, sender, message):
    print("%s\t--\t%s is now known as %s" % (time, sender[0], message))

def outmode(time, sender, message):
    print("%s\t--\tMode %s [%s] by %s" % (time, chan, " ".join(message.split(' ')[1:]), sender[0]))

def outjoin(time, sender, message):
    print("%s\t-->\t%s (%s) has joined %s" % (time, sender[0], sender[1], chan))

def outpart(time, sender, message):
    print("%s\t<--\t%s (%s) has left %s (\"%s\")" % (time, sender[0], sender[1], chan, message))

def outquit(time, sender, message):
    print("%s\t<--\t%s (%s) has quit %s (%s)" % (time, sender[0], sender[1], chan, message))

def outkick(time, sender, message):
    print("%s\t<--\t%s has kicked %s (%s)" % (time, sender[0], message.split(' ')[0], ' '.join(message.split(' ')[1:])))

def outserver(time, sender, message):
    print("%s\t--\t%s *** %s" % (time, sender[0], message))

def outinfo(time, sender, message):
    print("%s\t--\t%s *** %s" % (time, sender[0], message))

def outerror(time, sender, message):
    print("%s\t=!=\t%s *** %s" % (time, sender[0], message))

def outothers(time, sender, message):
    print("%s\t--\t%s" % (time, message))

def outlog(type, time, sender, message):
    if type == 1:
        return outmessage(time, sender, message)
    elif type == 2:
        return outnotice(time, sender, message)
    elif type == 4:
        return outaction(time, sender, message)
    elif type == 8:
        return outnick(time, sender, message)
    elif type == 16:
        return outmode(time, sender, message)
    elif type == 32:
        return outjoin(time, sender, message)
    elif type == 64:
        return outpart(time, sender, message)
    elif type == 128:
        return outquit(time, sender, message)
    elif type == 256:
        return outkick(time, sender, message)
    elif type == 1024:
        return outserver(time, sender, message)
    elif type == 2048:
        return outinfo(time, sender, message)
    elif type == 4096:
        return outerror(time, sender, message)
    elif type == 8192:
        return outothers(time, sender, message)
    else:
        return outothers(time, sender, message)

for row in sys.stdin:
    try:
        row = row.split(" | ")
        type = int(row[0])
        time = row[2].strip().split('.')[0]
        sender = row[3].strip().split('!')
        message = " | ".join(row[4:]).strip()
        outlog(type, time, sender, message)
    except:
        print("0000-00-00 00:00:00\t=!=\tUnable to parse this message from Quassel database to WeeChat format!")
