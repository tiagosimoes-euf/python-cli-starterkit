

def format(arg, style='0', fg='39', bg='49', prefix=False):
    style = f'{style};' if style and (fg or bg) else ''
    fg = f'{fg};' if fg and bg else ''

    if prefix:
        arg = f'[{arg}]'

    return f'\033[{style}{fg}{bg}m{arg}\033[0m'


def error(msg):
    prefix = format('error', style='1', bg='41', prefix=True)
    output(str(msg), prefix, 3)


def success(msg):
    prefix = format('success', style='1', bg='42', prefix=True)
    output(str(msg), prefix, 1)


def warning(msg):
    prefix = format('warning', style='1', bg='43', prefix=True)
    output(str(msg), prefix, 1)


def info(msg):
    prefix = format('info', style='1', bg='44', prefix=True)
    output(str(msg), prefix, 4)


def notice(msg):
    prefix = format('notice', style='1', bg='46', prefix=True)
    output(str(msg), prefix, 2)


def output(content, prefix='', indent=0):
    space = ''

    if int(indent) > 0:
        for i in range(indent):
            space = f' {space}'

    prefix = f'{prefix} ' if prefix else ''

    print(f'{space}{prefix}{content}')
