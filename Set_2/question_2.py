import numpy as np
import matplotlib.pyplot as plt

def x_t(x0,k1,t):
    return x0*np.exp(-k1*t)

def y_t(k1,k2,x0,t):
    return ((k1*x0)/(k2-k1))* ( np.exp(-k1*t) - np.exp(-k2*t))

def equal_case(k,x0,t):
    return k*x0*t*np.exp(-k*t)

t=np.arange(0,100,0.0001)
x0=1
k1=0.6931
k2 = 0.0231
ans=x_t(x0,k1,t)
ans_y=y_t(k1,k2,x0,t)
tt=np.log(k1/k2)*(1/k1-k2)

plt.plot(t,ans,label='Drug in GI Tract')
plt.title('Single Dose')
plt.legend()
plt.plot(t,ans_y,label='Drug in Blood')
plt.title('Single Dose')
plt.legend()
plt.show()

print("Max. value of y_t",y_t(k1,k2,x0,tt))

k=0.6931
equal_case_k1=equal_case(k,x0,t)
ans_k1=x_t(x0,k,t)
k=0.0231
tt=np.arange(0,210,0.0001)
ans_k2=x_t(x0,k,tt)
equal_case_k2=equal_case(k,x0,tt)

plt.plot(t,equal_case_k1,label='Drug in Blood (k=0.6931)')
plt.plot(t,ans_k1,label='Drug in GI Tract')
plt.title('Single Dose (Equal k)')
plt.legend()
plt.show()

plt.plot(tt,equal_case_k2,label='Drug in Drug in Blood (k=0.0231)')
plt.plot(tt,ans_k2,label='Drug in GI Tract')
plt.title('Single Dose (Equal k)')
plt.legend()
plt.show()

