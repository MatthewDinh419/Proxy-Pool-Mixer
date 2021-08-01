# Proxy Pool Mixer

A script that combines the pools of a proxy provider to obtain a combined in order pool

## Description

Proxy providers often recommend using multiple pools for certain websites and bots often use in order assignment of proxies to tasks. This creates a problem where a user will have to create multiple proxy lists to get the correct usage of each pool. This script aims to combine the pools required so that the user will only have to create one proxy list for their bot.

## Example
```
proxies1.txt
43.95.27.179
244.159.15.136
17.182.185.95
```
```
proxies2.txt
100.190.253.167
144.142.253.62
128.152.137.167
```
```
combined.txt
43.95.27.179
100.190.253.167
244.159.15.136
144.142.253.62
17.182.185.95
128.152.137.167
```
As we can see, the proxies in each text file are weaved together to form combined.txt. This allows you to utilize all the pools that are needed so that you can use combined.txt as one proxy list.
## Getting Started
Start by putting a pool of proxies in proxies1.txt and another pool of proxies in proxies2.txt. Then run the randomize.py script and the combined proxies will be written into randomize.py
### Dependencies

* Python3

### Executing program

```
python3 randomize.py
```
