##################################### loop & dict ################################################

countries = ["INDIA","UNITED STATES","AUSTRALIA","IRELAND","SRI LANKA","ICELAND","CUBA","IRAN","POLAND"]
counter = 0
output = []


for country in countries :
    if country.startswith('I'):
        counter = counter + 1
        output.append(country)

print(counter)
print()
print(output)

