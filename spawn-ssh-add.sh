#!/usr/bin/expect -f
spawn ssh-add ./tmp.key
expect "Enter passphrase for ./tmp.key:"
send "\n";
interact
