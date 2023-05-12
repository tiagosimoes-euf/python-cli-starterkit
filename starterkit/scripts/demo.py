
from starterkit import fancyprint as fp


def main(*args):
    print()
    print('**************')
    print('* FancyPrint *')
    print('**************')
    print()

    print(fp.format('Style', prefix=True))

    print(fp.format('0 Neutral'))
    print(fp.format('1 Bold', style='1'))
    print(fp.format('2 Muted', style='2'))
    print(fp.format('3 Italic', style='3'))
    print(fp.format('4 Underline', style='4'))

    input('\nPress Enter to continue...')

    print()

    print(fp.format('Foreground color', prefix=True))

    print(fp.format('31 Red', fg='31'))
    print(fp.format('32 Green', fg='32'))
    print(fp.format('33 Yellow', fg='33'))
    print(fp.format('34 Blue', fg='34'))
    print(fp.format('35 Purple', fg='35'))
    print(fp.format('36 Cyan', fg='36'))
    print(fp.format('37 Light grey', fg='37'))

    input('\nPress Enter to continue...')

    print()

    print(fp.format('Background color', prefix=True))

    print(fp.format('41 Red', bg='41'))
    print(fp.format('42 Green', bg='42'))
    print(fp.format('43 Yellow', bg='43'))
    print(fp.format('44 Blue', bg='44'))
    print(fp.format('45 Purple', bg='45'))
    print(fp.format('46 Cyan', bg='46'))
    print(fp.format('47 Light grey', bg='47'))

    input('\nPress Enter to continue...')

    print()

    print(fp.format('Indent', prefix=True))

    fp.output('No indent')
    fp.output('1 space', indent=1)
    fp.output('2 spaces', indent=2)
    fp.output('3 spaces', indent=3)
    fp.output('4 spaces', indent=4)

    input('\nPress Enter to continue...')

    print()

    print(fp.format('Utilities', prefix=True))

    fp.success('Display a success message.')
    fp.notice('Display a notice.')
    fp.warning('Display a warning.')
    fp.error('Display an error.')
    fp.info('Display information.')

    print()
