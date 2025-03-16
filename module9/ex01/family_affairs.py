#!/usr/bin/env python3

def find_the_redheads(family):
    redheads = filter(lambda name: family[name] == "red", family.keys())
    return list(redheads)

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "friend": "red"
}
print(find_the_redheads(dupont_family))