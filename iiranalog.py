"""IIR butterworth and Chebyshev  filter """

from numpy import pi,linspace,cos,log10
from scipy.signal import butter,buttord,TransferFunction,lfilter,freqs
from scipy.signal import cheb1ord,cheby1
import matplotlib.pyplot as plt


fpa=int(input('PB freq:'))
fsa=int(input('S.B freq:'))
fs=int(input('sampling freq:'))                           #To switch between Butterworth and Chebyshev filter 
rp=int(input('passband attn:'))                         # uncomment/comment lines 25,27,29,31
rs=int(input('stopband attn:'))
                                                        #To change between lowpass and high pass
                                                        #Replace 'low' with 'high' or vice versa
n=linspace(0,79)
x1=cos(2*pi*200*n/fs)   

#x2=cos(2*pi*1500*n/fs)
#x3=cos(2*pi*4000*n/fs)

wpd=2*pi*fpa/fs
wsd=2*pi*fsa/fs


N,wn=buttord(wpd,wsd,rp,rs,True) #Calculate order of the given filter with given set of specifications

#N,wn=cheb1ord(wpd,wsd,rp,rs,True)


#b,a=cheby1(N,rp,wn,'high',True)

b,a=butter(N,wn,'high',True)  #Compute the given transfer function 



sys=TransferFunction(b,a)

w,h=freqs(b,a)

plt.plot(w,20*log10(abs(h)))
plt.grid()
plt.title('Frequency response')
plt.xlabel('Gain magnitude')
plt.ylabel('Amplitude')

plt.show()

y=lfilter(b,a,x1)

plt.plot(x1)
plt.title('input signal')
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.show()

plt.plot(y)
plt.title('Output response')
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.show()