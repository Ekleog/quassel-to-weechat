#!/bin/sh

exec psql -h 127.0.0.1 -p 5432 quassel root -c "$1"
