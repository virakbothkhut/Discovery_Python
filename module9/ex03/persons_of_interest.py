#!/usr/bin/env python3

def famous_births(women_scientists):
    data_list = sorted(women_scientists.items(), key=lambda a:a[1]['date_of_birth'])
    for x in data_list:
        print(f" {x[1]['name']} is great scientist born in {x[1]['date_of_birth']}")

women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)


