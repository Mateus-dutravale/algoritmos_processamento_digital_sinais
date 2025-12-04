import sympy as sp 


def resFrequencia(h, w):
    z = sp.symbols('z')
    
    hz = h.subs(z, sp.exp(-sp.I*w))
    
    hz = sp.expand_complex(hz) 
    hz = sp.simplify(hz)
    
    h_modulo = sp.sqrt(sp.re(hz)**2 + sp.im(hz)**2)
    h_modulo = sp.simplify(h_modulo)  
    
    h_fase = -sp.atan2(sp.im(hz), sp.re(hz)) #fase em rad/s
    h_fase = sp.simplify(h_fase)      
    
    return h_modulo.evalf(), h_fase.evalf()


# # teste do material de apoio 
# z = sp.symbols('z')
# h = 1/(1 - 0.8*z**-1)
# w = sp.pi/6

# H, fase = resFrequencia(h, w)


# print("Modulo:", H)
# print("\nFase:", fase)


__all__ = ['resFrequencia']