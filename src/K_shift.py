import numpy as np 
import math

from numba import njit, prange
from scipy.fft import rfft, irfft
from tools import doublefactorial

@njit(parallel = True)
def simulate_X_shift_naive(M, n, T, H, eps, Z) : 
    X = np.zeros((M, n+1))
    t_grid = np.linspace(0, T, n+1) 
    sqrt_dt = math.sqrt(T/n) 

    for m in prange(M) : 
        for i in range(1, n+1) : 
            for j in range(0, i) : 
                X[m,i] += (t_grid[i] - t_grid[j] + eps)**(H-1/2) * sqrt_dt * Z[m,j]
    
    return X 

def simulate_X_shift_FFT(M, n, T, H, eps, Z):
    X = np.zeros((M, n+1))
    t_grid = np.linspace(0, T, n+1)
    sqrt_dt = math.sqrt(T/n)
    
    kernel = np.zeros(n)
    for k in range(n):
        kernel[k] = (t_grid[k+1] + eps)**(H - 0.5)
    
    for m in range(M):
        z_padded = np.zeros(2*n)
        z_padded[:n] = Z[m, :n] * sqrt_dt
        
        kernel_padded = np.zeros(2*n)
        kernel_padded[:n] = kernel
        
        Z_fft = rfft(z_padded)
        K_fft = rfft(kernel_padded)
        conv_fft = Z_fft * K_fft
        conv_result = irfft(conv_fft)
        
        X[m, 1:] = conv_result[:n]
    
    return X

def compute_g_shift(u_grid, m, alphas, H, eps = 1/52) : 
    constant = 1/(2*H)
    N_quad = len(u_grid)
    g = np.zeros(N_quad)
    cauchy = np.convolve(alphas, alphas)

    for r in range(N_quad) : 
        if u_grid[r] == 0:
            g[r] = cauchy[0] 
            continue
        variance = constant * ((u_grid[r]+eps)**(2*H) - eps**(2*H))
        sigma = np.sqrt(variance)
        for k in range(2*m+1) : 
            if k%2 != 0: continue
            g[r] += sigma**k * doublefactorial(k-1) * cauchy[k]
    return g 

def compute_G_shift(t, u_grid, m, H, eps = 1/52): 
    constant = 1/(2*H)
    N_quad = len(u_grid)
    G = np.zeros((2*m+1, N_quad))

    for k in range(2*m+1) : 
        if k % 2 != 0 : continue 
        for r in range(N_quad) : 
            variance = constant * ((u_grid[r] - t + eps)**(2*H) - eps**(2*H))
            sigma = np.sqrt(variance)
            G[k,r] = sigma**k * doublefactorial(k-1)
    return G 



