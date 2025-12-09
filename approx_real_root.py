def approx_real_root(coeffs, interval):
    a, b = interval

    def g(x):
        return coeffs[0] + coeffs[1]*x + coeffs[2]*x**2 + coeffs[3]*x**3

    if g(a) * g(b) >= 0:
        raise ValueError("Function must change its sign on the interval [a, b]")
    
    tol = 1e-9
    maxit = 100 #max iteration

    for i in range(maxit):
        x = (a + b)/2.0
        
        if abs(g(x)) <= tol or b-a <= tol:
            break

        if g(a) * g(x) <0:
            b = x
        else:
            a = x
    return x
  
    pass