import numpy as np
import matplotlib.pyplot as plt

def x_t(I,k1,t):
    return (I/k1)*(1-np.exp(-k1*t))

def y_t(I,k1,k2,t):
    term1=I/k2
    term2=I/(k2-k1)
    eq1=1-np.exp(-1*k2*t)
    eq2=np.exp(-1*k1*t)
    eq3=np.exp(-1*k2*t)
    return term1*eq1 - term2*(eq2-eq3)



def equal_case(I,k,t):
    return (I/k)*(1-(k*t+1)*np.exp(-k*t))

I=1
k1=0.6931
k2=0.0231
t=np.arange(0,10,0.001)

ans_x=x_t(I,k1,t)
ans_y=y_t(I,k1,k2,t)

plt.plot(t,ans_x,label='Drug in GI Tract ')
plt.title('Drug Course')
plt.legend()
plt.show()

plt.plot(t,ans_y,label='Drug in Blood ')
plt.title('Drug Course')
plt.legend()
plt.show()

k=0.6931
equal_k1=equal_case(I,k,t)
x_equal=x_t(I,k,t)
k=0.0231
equal_k2=equal_case(I,k,t)


plt.plot(t,x_equal,label='Drug in GI Tract (k=0.6931)',color='red')
plt.title('Drug Course (equal k)')
plt.xlabel('Time (hours)')
plt.ylabel('Drug Concentration')
plt.legend()
plt.show()


plt.plot(t,equal_k1,label='Drug in Blood (k=0.6931)',color='blue')
plt.title('Drug Course (equal k)')
plt.legend()
plt.show()


plt.plot(t,equal_k2,label='Drug in Blood (k=0.0231)',color='blue')
plt.title('Drug Course (equal k)')
plt.legend()
plt.show()

