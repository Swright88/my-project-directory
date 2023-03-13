def check_todo(string):
    if type(string) is str:
        if '#TODO' in string:
            return True
        else:
            return False
    else: 
        raise Exception("This is not a valid string")