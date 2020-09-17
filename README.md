# Subnetter
It gives subnet mask, wildcard, networkid, broadcast, total host information for given an IP &amp; subnet.

## Download & Usage
`git clone github.com/Toxifera/subnetter`

### Example 
`python2.7 : from subnetter import Subnetter`
`print(Subnetter('192.168.1.1/24').address)`    *gives address of this network*
`print(Subnetter('192.168.1.1/24').subnet)`     *gives subnet of this network*
`print(Subnetter('192.168.1.1/24').subnetmask)` *gives subnetmask of this network*
`print(Subnetter('192.168.1.1/24').wildcard)`   *gives wildcard of this network*
`print(Subnetter('192.168.1.1/24').networkid)`  *gives network id of this network*
`print(Subnetter('192.168.1.1/24').broadcast)`  *gives broadcast id of this network*
`print(Subnetter('192.168.1.1/24').totalhost)`  *gives total host count of this network*
