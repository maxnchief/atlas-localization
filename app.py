from babel import ngettext

def _(message):
    """Translation function placeholder"""
    return message

greeting = _("Hello, World!")

num = 3
message = ngettext(
    "You have one message", 
    "You have %(num)d messages", 
    num
) % {"num": num}

print(greeting)
print(message)