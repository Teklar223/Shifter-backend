'''
A basic utility file for our django base_app.
'''

def prints_args_kwargs(*args, **kwargs):
    # Print the values of *args
    print("*args values:")
    for arg in args:
        print(arg)

    # Print the values of **kwargs
    print("**kwargs values:")
    for key, value in kwargs.items():
        print(f"{key} = {value}")


# TODO: move somewhre else (not sure where to yet)
class slugs():
    company_id = "company_id"
    role_id = "role_id"
    team_id = "team_id"
    employee_id = "employee_id"
    requisite_id = "requisite_id"
    superior_id = "superior_id"


