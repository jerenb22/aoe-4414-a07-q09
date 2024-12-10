# max_bitrate.py
#
# Usage: python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz
# This script calculates the maximum achievable bitrate for a communication link using the Shannon-Hartley theorem.
#
# Parameters:
# tx_w: Transmitter power in Watts
# tx_gain_db: Transmitter gain in dB
# freq_hz: Frequency in Hz
# dist_km: Distance between transmitter and receiver in kilometers
# rx_gain_db: Receiver gain in dB
# n0_j: Noise spectral density in Watts/Hz
# bw_hz: Bandwidth in Hz
#
# Output:
# The maximum achievable bitrate in bits per second, rounded down to the nearest whole number.
#
# Written by Jeren Browder
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math # math module
import sys # argv

# Constants
c=2.99792458*(10**8) #m/s
L_l= 10**(-1/10) #0.79dB
L_a = 10**(0/10) #0.79dB #dB

# initialize script arguments
tx_w= float('nan')
tx_gain_db= float('nan')
freq_hz= float('nan')
dist_km= float('nan')
rx_gain_db= float('nan')
n0_j= float('nan')
bw_hz= float('nan')

# parse script arguments
if len(sys.argv)==8:
    tx_w= float(sys.argv[1])
    tx_gain_db= float(sys.argv[2])
    freq_hz= float(sys.argv[3])
    dist_km= float(sys.argv[4])
    rx_gain_db= float(sys.argv[5])
    n0_j= float(sys.argv[6])
    bw_hz= float(sys.argv[7])
else:
   print(\
    'Usage: '\
    'python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz'\
   )
   exit()

# write script below this line
lamda = c/freq_hz #m
S= dist_km * 1000 #m

C = tx_w * L_l * tx_gain_db * (lamda/(4*math.pi*S))**2  * L_a * rx_gain_db
N=n0_j*bw_hz #W
inp = 1+C/N
r_max= bw_hz * math.log(inp,2)


print(math.floor(r_max))
