#!/usr/bin/env python3

def array_of_names(persons):
    return [f"{first.capitalize()} {last.capitalize()}" for first, last in persons.items()]

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}
print(array_of_names(persons))
