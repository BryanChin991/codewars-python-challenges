'''def make_readable(seconds):
    d = {}

    d['hrs'] = seconds // (60*60)
    d['min'] = (seconds % (60*60)) // 60
    d['sec'] = (seconds - 60*60) % 60
    return '{:02}:{:02}:{:02}'.format(d['hrs'], d['min'], d['sec'])'''

def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)

make_readable(60)
make_readable(115)
make_readable(3590)
make_readable(3599)
make_readable(3600)
make_readable(86399)
make_readable(359999)