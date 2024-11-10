from imports import *

R = 6.8e-2
n = 320
g = 2.0036

mu_b = constants.physical_constants["Bohr magneton"][0]

def campoHell(I=1, R=R, n=n):
    return constants.mu_0 * (4/5)**(3/2) * n / R * I

def constanteG(ang_cft=1):
    return constants.h * ang_cft / mu_b