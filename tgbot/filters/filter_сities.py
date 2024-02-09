def filter_cities_service(letter_town: str) -> str | None:
    all_city = ["одеса", "харків", "київ", "івано-франківськ", "odessa", "odesa", "xarkiv", "kuiv", "ivano-frankivsk", "одесса", "харьков", "киев", "ивано-франковск"]

    for word in all_city:
        found = True
        for letter in letter_town.lower():
            if letter not in word:
                found = False
                break
        if found:
            return word
    return None

# out = filter_cities_service("od")
# print(out)
# if not out:
#     print(None)
# else:
#     print(True)
