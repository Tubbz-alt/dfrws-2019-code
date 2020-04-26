#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Rpi Data Acquisition
# GNU Radio version: 3.8.0.0

from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import osmosdr
import time

class rpi_data_acquisition(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Rpi Data Acquisition")

        ##################################################
        # Variables
        ##################################################
        self.trigger = trigger = -1
        self.samp_rate = samp_rate = 3200000
        self.capture_freq = capture_freq = 1.0001e9

        ##################################################
        # Blocks
        ##################################################
        self.rtlsdr_source_0 = osmosdr.source(
            args="numchan=" + str(1) + " " + "rtl=0"
        )
        self.rtlsdr_source_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(capture_freq, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_gain(40, 0)
        self.rtlsdr_source_0.set_if_gain(20, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna('', 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)
        self.blocks_tagged_file_sink_0 = blocks.tagged_file_sink(gr.sizeof_gr_complex*1, samp_rate)
        self.blocks_burst_tagger_0 = blocks.burst_tagger(gr.sizeof_gr_complex)
        self.blocks_burst_tagger_0.set_true_tag('burst',True)
        self.blocks_burst_tagger_0.set_false_tag('burst',False)
        self.analog_const_source_x_0 = analog.sig_source_s(0, analog.GR_CONST_WAVE, 0, 0, trigger)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_burst_tagger_0, 1))
        self.connect((self.blocks_burst_tagger_0, 0), (self.blocks_tagged_file_sink_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.blocks_burst_tagger_0, 0))

    def get_trigger(self):
        return self.trigger

    def set_trigger(self, trigger):
        self.trigger = trigger
        self.analog_const_source_x_0.set_offset(self.trigger)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)

    def get_capture_freq(self):
        return self.capture_freq

    def set_capture_freq(self, capture_freq):
        self.capture_freq = capture_freq
        self.rtlsdr_source_0.set_center_freq(self.capture_freq, 0)



def main(top_block_cls=rpi_data_acquisition, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()
        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()
    try:
        input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
