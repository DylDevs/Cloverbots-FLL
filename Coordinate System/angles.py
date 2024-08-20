distances = {}
# This will give an unpopulated dictionary that goes from 0-180 and -179 back to -1
if distances == {}:
    for i in range(181): # Repeat 181 times to get a range of 0-180
        distances[i] = 0.0
        if i != 180: # We dont want 180 and -180
            distances[-i] = 0.0