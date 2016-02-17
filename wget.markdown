`
wget -p -E -q https://twitter.com/snitzr/status/440017597535240193 --limit-rate=25k
wget -p -E -q https://twitter.com/snitzr/status/440017597535240193 -nd -H  # testing
wget -p -E -q https://twitter.com/snitzr/status/440017597535240193 -H --accept-regex https://pbs.twimg.com/  # testing
wget -p -E -q https://twitter.com/snitzr/status/440017597535240193 --limit-rate=25k -D https://twimg.com/
`

