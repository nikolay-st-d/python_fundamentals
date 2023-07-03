countries = input().split(', ')
capitals = input().split(', ')
new_dict = {country: capital for country, capital in zip(countries, capitals)}
for key, value in new_dict.items():
    print(f'{key} -> {value}')