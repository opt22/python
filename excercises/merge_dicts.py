
#dict 123 abc
#dict 456 def

first_thing = {
        1:"a",
        2:"b",
        3:"c"
}

second_thing = {
        4:"d",
        5:"e",
        6:"f"
}
print(first_thing)
print(second_thing)


third_thing = {**first_thing, **second_thing}
print(third_thing)

fourth_thing = first_thing | second_thing
print(fourth_thing)

def merge(first_thing,second_thing):
    fifth_thing= ""
