
import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import math as math

t = np.linspace(0,3, 12 * 1024)
right_hand = np.array([329.62,440,493.86,512,440])
left_hand = np.array([0,0,0,0,0])
time = np.array([0,0.6,1.3,2,2.6])
Time = np.array([0.4,0.4,0.4,0.3,0.4])
i = 0
x = 0
while(i<5):
    Fi = right_hand[i]
    fi = left_hand[i]
    ti = time[i]
    Ti = Time[i]
    Func_Right = np.sin(2 * np.pi * Fi * t)
    Func_Left = np.sin(2 * np.pi * fi * t)
    x = x + (Func_Right +  Func_Left)*((t >= ti) & (t <= (Ti + ti))) 
    i += 1
plt.plot(t,x)


𝑁 = 3*1024
𝑓 = np. linspace(0 , 512 , int(𝑁/2))
x_f = fft(x)
x_f = 2/N * np.abs(x_f [0:np.int(N/2)])
𝑓𝑛1,𝑓𝑛2= np. random. randint(0, 512, 2)
noise= np.sin(2 * np.pi * fn1 * t)+ np.sin(2 * np.pi * fn2 * t)
xn=x+noise
xn_f = fft(xn)
xn_f = 2/N * np.abs(xn_f [0:np.int(N/2)])
z = np.where(xn_f>math.ceil(np.max(x_f))+0.5)
index1 = z[0][0]
index2 = z[0][1]
founder1 = int(f[index1])
founder2 = int(f[index2])
xFiltered = xn - (np.sin(2*np.pi*founder1*t)+np.sin(2*np.pi*founder2*t))
xFiltered_f = fft(xFiltered)
xFiltered_f = 2/N * np.abs(xFiltered_f [0:np.int(N/2)])
sd.play(xFiltered, 3*1024)
plt.figure()
plt.subplot(3,1,1)
plt.plot(t,x)
plt.subplot(3,1,2)
plt.plot(t,xn)
plt.subplot(3,1,3)
plt.plot(t,xFiltered)
plt.figure()
plt.subplot(3,1,1)
plt.plot(f,x_f)
plt.subplot(3,1,2)
plt.plot(f,xn_f)
plt.subplot(3,1,3)
plt.plot(f,xFiltered_f)
