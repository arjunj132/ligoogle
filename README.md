# LiGoogle Docs

This package allows you to open google on the Linux terminal.

## Installation

You can install it via pip using:

```
pip3 install ligoogle
```

## Usage

You open ligoogle by typing:

```
python3 -m ligoogle.google
```

Then the ligoogle cli pops up. Then type your search term and it should take some time till the JSON results appear.

## Changing API keys

You also may need to change the API keys to get a higher quota (regular is public and may limit you search quota). First go to [RapidAPI](https://rapidapi.com/) and get a API key. Then, at the `search@google` type this:

```
api-change
```

Then, enter your API key and then boom!

---

Copyright (c) Arjun J
