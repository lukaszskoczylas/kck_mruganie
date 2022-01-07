from pyOpenBCI import OpenBCIGanglion
import filterlib as flt
import datetime


mac_adress = 'eb:3a:66:e2:04:06'

def print_raw(sample):
	smp = sample.channels_data[0]
	smp_flted = frt.filterIIR(smp, 0)
	with open("moje_dane.txt", "a") as myfile:
		myfile.write(f'{str(smp_flted)},{datetime.datetime.now().time()}\n')

board = OpenBCIGanglion(mac=mac_adress)

if __name__ == '__main__':
	# filtering in real time object creation
	frt = flt.FltRealTime()
	board.start_stream(print_raw)
