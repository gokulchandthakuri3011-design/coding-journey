"""
### Medium
4. Write a function `create_profile(**kwargs)` that prints a person's profile details. Call it with different keyword arguments.
5. Create a function `calculate(a, b, /, operation="add")` that performs addition or subtraction. The first two params must be positional-only.
6. Write a function `format_text(*, text, uppercase=False)` where both params are keyword-only. If `uppercase` is True, return the text in uppercase.
7. Create a function `build_url(base, *paths, **params)` that joins base URL with path segments and appends query parameters from `**params`.

"""
# Function displaying person's profile
def create_profile(**kwargs): # Here **kwargs takes dict
    print("--- Personal Profile ---")
    for key, value in kwargs.items():
        print(f"{key} : {value}")

# Function to calculate
def calculate(a, b, /, operation = "add"):
    print(f"a + b : {a} + {b}")
    print(f"a - b : {a} - {b}")

# Function to format text
def format_text(*, text, uppercase = False):
    if uppercase == True:
        result = text.upper()
    else: 
        result = text
    return result

# Function to build url
def build_url(base, *paths, **params):
    url = base + "/".join(str(p) for p in paths) # Converting int to str to concaatenate them together
                                                 # .join() concatenates a list/iterable of strings(each seperately)
    if params:
        query = "&".join(f"{k}={v}" for k, v in params.items())
        url += "?" + query
    return url

# Calling each function with their each arguments
create_profile(name = "Arun", age = 22, is_student = True)
calculate(2,3)
print(format_text(text = "Hi Lalita!", uppercase = True))
print(build_url("httpsarunlalita", 1, 2, 3, type = "friends"))