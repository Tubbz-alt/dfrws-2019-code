#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Am Demod Chop
# GNU Radio version: 3.8.0.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import blocks
import pmt
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import qtgui

class am_demod_chop(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Am Demod Chop")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Am Demod Chop")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "am_demod_chop")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.cpu_offset = cpu_offset = -72e3
        self.capture_freq = capture_freq = 1.0001e9
        self.sideband_offset = sideband_offset = 257e3
        self.samp_rate = samp_rate = 32e5
        self.cpu_freq = cpu_freq = capture_freq + cpu_offset
        self.up_sideband_freq = up_sideband_freq = cpu_freq + sideband_offset
        self.low_sideband_freq = low_sideband_freq = cpu_freq - sideband_offset
        self.firdes_tap_low_reader = firdes_tap_low_reader = firdes.low_pass(1, samp_rate, 300000, 10000, firdes.WIN_HAMMING, 6.76)

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            20000, #size
            samp_rate, #samp_rate
            "", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.01)
        self.qtgui_time_sink_x_0.set_y_axis(-1.2, 1.2)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 3.5, 0.0010, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            cpu_freq, #fc
            samp_rate, #bw
            "", #name
            1
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.01)
        self.qtgui_freq_sink_x_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(False)
        self.qtgui_freq_sink_x_1.set_fft_average(0.2)
        self.qtgui_freq_sink_x_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1.enable_control_panel(True)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_1_win)
        self.freq_xlating_fir_filter_xxx_1 = filter.freq_xlating_fir_filter_ccc(1, firdes_tap_low_reader, cpu_offset, samp_rate)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(100)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, '../data/1block/2/0-chopped.dat', False, 10000, 20000)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_complex_to_mag_1 = blocks.complex_to_mag(1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_mag_1, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fir_filter_xxx_1, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_1, 0), (self.blocks_complex_to_mag_1, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_1, 0), (self.qtgui_freq_sink_x_1, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "am_demod_chop")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_cpu_offset(self):
        return self.cpu_offset

    def set_cpu_offset(self, cpu_offset):
        self.cpu_offset = cpu_offset
        self.set_cpu_freq(self.capture_freq + self.cpu_offset)
        self.freq_xlating_fir_filter_xxx_1.set_center_freq(self.cpu_offset)

    def get_capture_freq(self):
        return self.capture_freq

    def set_capture_freq(self, capture_freq):
        self.capture_freq = capture_freq
        self.set_cpu_freq(self.capture_freq + self.cpu_offset)

    def get_sideband_offset(self):
        return self.sideband_offset

    def set_sideband_offset(self, sideband_offset):
        self.sideband_offset = sideband_offset
        self.set_low_sideband_freq(self.cpu_freq - self.sideband_offset)
        self.set_up_sideband_freq(self.cpu_freq + self.sideband_offset)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_firdes_tap_low_reader(firdes.low_pass(1, self.samp_rate, 300000, 10000, firdes.WIN_HAMMING, 6.76))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_1.set_frequency_range(self.cpu_freq, self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)

    def get_cpu_freq(self):
        return self.cpu_freq

    def set_cpu_freq(self, cpu_freq):
        self.cpu_freq = cpu_freq
        self.set_low_sideband_freq(self.cpu_freq - self.sideband_offset)
        self.set_up_sideband_freq(self.cpu_freq + self.sideband_offset)
        self.qtgui_freq_sink_x_1.set_frequency_range(self.cpu_freq, self.samp_rate)

    def get_up_sideband_freq(self):
        return self.up_sideband_freq

    def set_up_sideband_freq(self, up_sideband_freq):
        self.up_sideband_freq = up_sideband_freq

    def get_low_sideband_freq(self):
        return self.low_sideband_freq

    def set_low_sideband_freq(self, low_sideband_freq):
        self.low_sideband_freq = low_sideband_freq

    def get_firdes_tap_low_reader(self):
        return self.firdes_tap_low_reader

    def set_firdes_tap_low_reader(self, firdes_tap_low_reader):
        self.firdes_tap_low_reader = firdes_tap_low_reader
        self.freq_xlating_fir_filter_xxx_1.set_taps(self.firdes_tap_low_reader)



def main(top_block_cls=am_demod_chop, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
