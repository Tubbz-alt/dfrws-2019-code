# EM Side-Channel Attacks on AES Encryption
## OSU CSE 5429 - Hardware Security Project

This repository is forked from a repository by Asanka Sayakkara.
Tyler Harris, Michael Hayworth, Griffin Thompson, and I (Kyle Westhaus) modified the code to attempt to perform AES key extraction via electromagnetic side-channel attacks on a Raspberry Pi Zero.
We modified the scripts which perform the AES encryption on the device under test as well as the GNU Radio Companion (GRC) flowcharts to record the radio frequency (RF) signals.
In addition, we added some of our own RF recordings as well as GRC flowcharts which process these recordings.

To learn more about our project and what we accomplished (as well as what we didn't), please read [our final report.](https://docs.google.com/document/d/1N5pLWlWuhqlhWMYbWTlVVzHKo8fPh0ePCxnTA4jez-o/edit?usp=sharing)
If you wish to use this code, check out the Setup section specifically, which provides details on how to prepare both the hardware and software to reproduce and build upon our results.
