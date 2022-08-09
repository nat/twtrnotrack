#!/usr/bin/env python3
#
# A script to strip the tracking cookies from Twitter links in your clipboard.
#

import pasteboard
import time

pb = pasteboard.Pasteboard()

while True:
    str = pb.get_contents()
    if str is not None and str.startswith('https://twitter.com/') and str.find('t=') != -1:
        str = str.split('?')[0]
        pb.set_contents(str)

    time.sleep (0.5)
