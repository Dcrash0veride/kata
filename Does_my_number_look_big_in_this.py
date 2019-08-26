def narcissistic( value ):
    total = 0
    breaks = str(value)
    power = len(breaks)
    for i in breaks:
         total += int(i) ** int(power)
    if total == value:
        return True
    else:
        return False