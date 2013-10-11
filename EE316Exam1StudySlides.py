import webbrowser

#the hint was 2^38...2 to the 38th power...
site = 'bit.ly/ee316ch#'

#newsite = site.replace('0', string)
for i in xrange(1,9):
    if i != 6:
        newsite = site.replace('#', str(i))
        print newsite
        webbrowser.open(newsite)
    else: 
        print 'fuck you'