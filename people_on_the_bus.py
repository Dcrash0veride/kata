def number(bus_stops):
    got_on = [x[0] for x in bus_stops]
    got_off = [x[1] for x in bus_stops]
    return sum(got_on) - sum(got_off)