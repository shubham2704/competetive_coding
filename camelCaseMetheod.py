def camel_case(string):
    return "".join(x for x in string.title() if not x.isspace())
print(camel_case("hello case"))