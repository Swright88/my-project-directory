def minutes_to_read_text(num):
    if type(num) is not int:
        raise Exception("You have not entered a number in the correct format")
    else:
        if num > 0:
            answer = num / 200
            return f"It will take {int(answer)} minutes to read {num} words!"
        else:
            raise Exception("You can not have a negative number of words!")