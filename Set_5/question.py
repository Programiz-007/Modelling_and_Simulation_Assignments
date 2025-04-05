import numpy as np
import matplotlib.pyplot as plt

etch_in=np.loadtxt('in_etch.dat')
etch_out=np.loadtxt('out_etch.dat')
lenny_in=np.loadtxt('in_lenny.dat')
lenny_out=np.loadtxt('out_lenny.dat')
squeeze_in=np.loadtxt('in_squeeze.dat')
squeeze_out=np.loadtxt('out_squeeze.dat')


def phi(x, eta, lambd, c, mu, alpha):
    return eta + (c/(x+lambd))**2

def line(x,c,alpha):
    return (x/c)**alpha

# etch incoming
alpha=-2
eta=-8
lambd=1.5
mu=-1
c=190

x_val=np.arange(1,100,0.01)
etch_in_val=phi(x_val, eta, lambd, c, mu, alpha)

plt.plot(x_val, etch_in_val, label='Etch Incoming', color='blue')
plt.plot(x_val, line(x_val,c,alpha), label='Power Law', color='green',linestyle='dashed')
plt.scatter(etch_in[:,0], etch_in[:,1], label='Etch Incoming Data', color='red',marker='+',s=35)
plt.xlabel('x')
plt.ylabel('phi')
plt.title('Etch Incoming')
plt.legend()
plt.ylim(10**-1,1e4)
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plt.show()

# etch outgoing
alpha=-2
eta=1
lambd=0.25
mu=-1
c=80

x_val=np.arange(1,10000,0.01)
etch_out_val=phi(x_val, eta, lambd, c, mu, alpha)

plt.plot(x_val, etch_out_val, label='Etch Outgoing', color='blue')
plt.scatter(etch_out[:,0], etch_out[:,1], label='Etch Outgoing Data', color='red',marker='+',s=35)
plt.xlabel('x')
plt.ylabel('phi')
plt.title('Etch Outgoing')
plt.legend()
plt.ylim(10**-1,1e4)
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plt.show()

# lenny incoming
alpha=-2    
eta=-15 
lambd=1.6
mu=-1
c=210

x_val=np.arange(1,100,0.01)
lenny_in_val=phi(x_val, eta, lambd, c, mu, alpha)

plt.plot(x_val, lenny_in_val, label='Lenny Incoming', color='blue')
plt.scatter(lenny_in[:,0], lenny_in[:,1], label='Lenny Incoming Data', color='red',marker='+')
plt.xlabel('x')
plt.ylabel('phi')
plt.title('Lenny Incoming')
plt.legend()
plt.ylim(10**-1,1e4)
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plt.show()

# lenny outgoing
alpha=-2
eta=1
lambd=0.35
mu=-1
c=90

x_val=np.arange(1,10000,0.01)
lenny_out_val=phi(x_val, eta, lambd, c, mu, alpha)

plt.plot(x_val, lenny_out_val, label='Lenny Outgoing', color='blue')
plt.scatter(lenny_out[:,0], lenny_out[:,1], label='Lenny Outgoing Data', color='red',marker='+')
plt.xlabel('x')
plt.ylabel('phi')
plt.title('Lenny Outgoing')
plt.legend()
plt.ylim(10**-1,1e4)
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plt.show()


# squeeze incoming
alpha=-2
eta=-28
lambd=2.2
mu=-1
c=265

x_val=np.arange(1,100,0.01)
squeeze_in_val=phi(x_val, eta, lambd, c, mu, alpha)

plt.plot(x_val, squeeze_in_val, label='Squeeze Incoming', color='blue')
plt.scatter(squeeze_in[:,0], squeeze_in[:,1], label='Squeeze Incoming Data', color='red',marker='D')
plt.xlabel('x')
plt.ylabel('phi')
plt.title('Squeeze Incoming')
plt.legend()
plt.ylim(10**-1,1e4)
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plt.show()

# squeeze outgoing
alpha=-2
eta=1
lambd=0.45
mu=-1
c=110

x_val=np.arange(1,10000,0.01)
squeeze_out_val=phi(x_val, eta, lambd, c, mu, alpha)

plt.plot(x_val, squeeze_out_val, label='Squeeze Outgoing', color='blue')
plt.scatter(squeeze_out[:,0], squeeze_out[:,1], label='Squeeze Outgoing Data', color='red',marker='x')
plt.xlabel('x')
plt.ylabel('phi')
plt.title('Squeeze Outgoing')
plt.legend()
plt.ylim(10**-1,1e4)
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plt.show()