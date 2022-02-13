legacy_customers = ['Alice', 'Bob']
new_customers = ['Tiff', 'steve']

db = [legacy_customers, new_customers]

print(db)

for legacy_customer in legacy_customers:
    new_customers.append(legacy_customer) 

print(new_customers)


test = {*legacy_customers, *new_customers}
print (test)


