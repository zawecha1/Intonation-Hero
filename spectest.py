#spec test
from __future__ import print_function, division

import thinkdsp
import thinkplot

import numpy

from matplotlib import pyplot

garbage = thinkdsp.read_wave('Sent_garbage.wav')
spectrogram = garbage.make_spectrogram(seg_length=1024)
pyplot.show(spectrogram.plot(high=5000))
