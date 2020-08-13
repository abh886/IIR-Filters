"""IIR butterworth and Chebyshev  filter """

from numpy import pi,tan,linspace,cos,log10
from scipy.signal import butter,buttord,TransferFunction,freqz,bilinear,lfilter
from scipy.signal import cheb1ord,cheby1
import matplotlib.pyplot as plt


fpa=int(input('PB freq:'))
fsa=int(input('S.B freq:'))
fs=int(input('sampling freq:'))
rp=int(input('passband attn:'))
rs=int(input('stopband attn:'))

n=linspace(0,79)
x1=cos(2*pi*100*n/fs)
x2=cos(2*pi*1500*n/fs)
x3=cos(2*pi*4000*n/fs)

wpd=2*pi*fpa/fs
wsd=2*pi*fsa/fs

pwpa=2*tan(wpd/2)
pwsa=2*tan(wsd/2)

N,wn=buttord(pwpa,pwsa,rp,rs,True)

#N,wn=cheb1ord(pwpa,pwsa,rp,rs,True)

#b,a=cheby1(N,rp,wn,'low',True)

b,a=butter(N,wn,'low',True)
Fs=1
num,den=bilinear(b,a,Fs)

sys=TransferFunction(b,a,dt=1)

w,h=freqz(num,den,128)

plt.plot((w*fs/(2*pi)),20*log10(abs(h)))
plt.grid()
plt.title('Frequency response')
plt.xlabel('Gain magnitude')
plt.ylabel('Amplitude')

plt.show()

y=lfilter(num,den,x1)


plt.stem(y)
plt.title('Output response')
plt.xlabel('n')
plt.ylabel('y(n)')

plt.show()

plt.stem(x1)
plt.title('input')
plt.xlabel('n')
plt.ylabel('x(n)')

plt.show()
