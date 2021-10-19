'''def format_duration(seconds):
    d = {}

    if seconds < 1:
        return print('now')

    d['year' if (seconds // (60 * 60 * 24 * 365)) == 1 else 'years'] = seconds // (60 * 60 * 24 * 365)
    d['day' if ((seconds % (60*60*24*365)) // (60*60*24)) == 1 else 'days'] = (seconds % (60*60*24*365)) // (60*60*24)
    d['hour' if ((seconds % (60*60*24)) // (60*60)) == 1 else 'hours'] = (seconds % (60*60*24)) // (60*60)
    d['minute' if ((seconds % (60*60)) // 60) == 1 else 'minutes'] = (seconds % (60*60)) // 60
    d['second' if ((seconds - 60*60) % 60) == 1 else 'seconds'] = (seconds - 60*60) % 60

    li = [' '.join(tups) for tups in list((str(val) , key) for key, val in d.items() if val != 0)]
    if len(li) <= 2:
        print(' and '.join(li))
    elif len(li) > 2:
        li = ', '.join(li[i] for i in range(len(li)-2)), ' and '.join(li[i] for i in [-2, -1])
        print(', '.join(li))'''

def format_duration(seconds):
    if seconds == 0: return "now"
    units = ( (31536000, "year"  ),
              (   86400, "day"   ),
              (    3600, "hour"  ),
              (      60, "minute"),
              (       1, "second") )
    ts, t = [], seconds
    for unit in units:
        u, t = divmod(t, unit[0])
        ts += ["{} {}{}".format(u, unit[1], "s" if u>1 else "")] if u != 0 else []
    return ", ".join([str(d)for d in ts[:-1]]) + (" and " if len(ts)>1 else "") + ts[-1]

format_duration(-1)
# format_duration(60)
# format_duration(115)
# format_duration(3590)
# format_duration(3599)
# format_duration(3600)
# format_duration(86399)
# format_duration(86400)
# format_duration(31536000)
# format_duration(31837000)