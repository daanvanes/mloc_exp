import sys

from SASession import *
# from SPSession import *

try:
    import appnope
    appnope.nope()
except:
    print 'APPNOPE NOT ACTIVE!'


def main():
    initials = raw_input('Your initials: (2 letters)')
    run_nr = int(raw_input('Run number: (1 int)'))
    scanner = raw_input('Are you in the scanner (y/n)?: ')
    track_eyes = raw_input('Are you recording gaze (y/n)?: ')

    which_exp = raw_input('which exp do you want to run: (fix/sa/sp)?')

    if track_eyes == 'y':
        tracker_on = True
    elif track_eyes == 'n':
        tracker_on = False

    if which_exp == 'sa':
        session = SASession( initials, run_nr, scanner, tracker_on,fix_sp='n' )
    elif which_exp == 'sp':
        session = SPSession( initials, run_nr, scanner, tracker_on)
    elif which_exp == 'fix':
        session = SASession( initials, run_nr, scanner, tracker_on,fix_sp='y')

    session.run()

if __name__ == '__main__':
    main()
