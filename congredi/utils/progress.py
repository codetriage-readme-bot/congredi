#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
from progressbar import AnimatedMarker, Bar, Counter, ETA, \
    Percentage, Widget, ProgressBar, Timer
class Speed(Widget):
    FORMAT = '%6.2f %s/s'
    PREFIXES = 'okMGTPEZY'

    def update(self, pbar):
        """Updates the widget with the current SI prefixed speed."""

        if pbar.seconds_elapsed < 2e-6 or pbar.currval < 2e-6: # =~ 0
            scaled = power = 0
        else:
            speed = pbar.currval / pbar.seconds_elapsed
            power = int(math.log(speed, 1000))
            scaled = speed / 1000.**power

        return self.FORMAT % (scaled, self.PREFIXES[power])
#http://www.artima.com/weblogs/viewpost.jsp?thread=240845
class example(object):
    # def wrapped(*args):
    #     f(args)
    # return wrapped
    def __init__(self, f):
        self.f = f
    def __call__(self, *args):
        """
        The __call__ method is not called until the
        decorated function is called.
        """
        print "Inside __call__()"
        self.f(*args)
@example
def together(interval=10000):
    things=[AnimatedMarker(), " ", Counter(), "/{} ".format(interval), Percentage(), ' ', Speed(), ' ', Bar(), ' ', Timer(), ' ', ETA()]
    pbar = ProgressBar(widgets=things, maxval=interval).start()
    for i in range(interval):
        pbar.update(i+1)
    pbar.finish()
together(100000000)