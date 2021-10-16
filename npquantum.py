import numpy as np

# Based of npquantum, a Quantum Computing at Davis (QCaD) educational library
# https://github.com/QC-at-Davis/npquantum/blob/master/npquantum.py

ket0 = np.array([[1],[0]])
bra0 = ket0.conjugate().T
ket1 = np.array([[0],[1]])
bra1 = ket1.conjugate().T
ketplus = 1/np.sqrt(2)*(ket0 + ket1)
ketminus = 1/np.sqrt(2)*(ket0 - ket1)


def Rx(theta):
    return np.array([[np.cos(theta/2), -1j*np.sin(theta/2)],
                      [-1j*np.sin(theta/2), np.cos(theta/2)]])


### Single Qubit Gates
X = ket0 * bra1 + ket1 * bra0
Y = (-1j * ket0 * bra1) + (1j * ket1 * bra0)
Z = ket0 * bra0 - ket1 * bra1
H = 1/np.sqrt(2) * np.array([[1,1], [1,-1]])
I = np.eye(2)

# |psi> = cos(theta/2)|0> + e^(i*phi)*sin(theta/2)|1>
# 0 <= theta <= pi
# 0 <= phi <= 2*pi
def ket_from_angles(theta, phi):
    ket0_coeff = np.cos(theta/2)
    ket1_coeff = (np.e**(1j*phi))*np.sin(theta/2)
    return  ket0_coeff * ket0 + ket1_coeff * ket1

def to_qiskit_plot(ket):
    return np.squeeze(np.asarray(ket))