def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    fx = 0
    for i in range(steps): 
        x0 = x0 - lr * (2 * x0 * a + b)

    return x0