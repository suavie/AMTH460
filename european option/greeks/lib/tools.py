import numpy as np
from scipy.stats import norm

#if T is in day-lengths, divide by 252 before passing the value to the function

def binomial_tree_option_price(S, K, T, r, sigma, n, option_type='call'):
    T=T/252
    delta_t = T / n
    u = np.exp(sigma * np.sqrt(delta_t))
    d = 1 / u
    p = (np.exp(r * delta_t) - d) / (u - d)

    stock_prices = np.zeros((n+1, n+1))
    option_values = np.zeros((n+1, n+1))

    for i in range(n+1):
        for j in range(i+1):
            stock_prices[j, i] = S * (u ** (i - j)) * (d ** j)

    if option_type == 'call':
        option_values[:, -1] = np.maximum(0, stock_prices[:, -1] - K)
    elif option_type == 'put':
        option_values[:, -1] = np.maximum(0, K - stock_prices[:, -1])

    for i in range(n-1, -1, -1):
        for j in range(i+1):
            option_values[j, i] = np.exp(-r * delta_t) * (p * option_values[j, i+1] + (1 - p) * option_values[j+1, i+1])

    option_price = option_values[0, 0]
    return option_price

def trinomial_tree_option_price(S, K, T, r, sigma, n, option_type='call'):
    T=T/252
    delta_t = T / n
    u = np.exp(sigma * np.sqrt(2 * delta_t))
    p_u = ((np.exp(r * delta_t/2) - np.exp(-sigma * np.sqrt(delta_t/2))) /
           (np.exp(sigma * np.sqrt(delta_t/2)) - np.exp(-sigma * np.sqrt(delta_t/2))))**2
    p_d = ((np.exp(sigma * np.sqrt(delta_t/2)) - np.exp(r * delta_t/2)) /
           (np.exp(sigma * np.sqrt(delta_t/2)) - np.exp(-sigma * np.sqrt(delta_t/2))))**2
    p_m = 1 - p_u - p_d
    stock_prices = np.zeros((2*n+1, n+1))
    option_values = np.zeros((2*n+1, n+1))
    stock_prices[n,0] = S
    for j in range(1,n+1):
        stock_prices[n-j,j] = S*u**j
        for i in range(n-j+1,n+j+1):
            stock_prices[i,j] = stock_prices[i-1,j]/u
    if option_type == 'call':
        option_values[:, -1] = np.maximum(0, stock_prices[:, -1] - K)
    elif option_type == 'put':
        option_values[:, -1] = np.maximum(0, K - stock_prices[:, -1])
    for j in range(n-1, -1, -1):
        for i in range(-j, j+1):
            option_values[i+n, j] = np.exp(-r * delta_t) * (p_u * option_values[i+n-1, j+1] +
                                                            p_d * option_values[i+n+1, j+1] +
                                                            p_m * option_values[i+n, j+1])
    option_price = option_values[n, 0]
    return option_price

def monte_carlo_option_price(S, K, T, r, sigma,tree_steps,option_type='call', num_simulations=10000):  
    num_steps = tree_steps*1000
    T=T/252
    dt=T/num_steps
    S_T = np.zeros(num_simulations)

    for i in range(num_simulations):
        rand = np.random.normal(0, 1, num_steps)
       
        stock_path = S * np.exp(np.cumsum((r - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * rand))
        S_T[i] = stock_path[-1]

    if option_type == 'call':
        payoff = np.maximum(0, S_T - K)
    elif option_type == 'put':
        payoff = np.maximum(0, K - S_T)
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")

    option_price = np.exp(-r * T) * np.mean(payoff)
    return option_price
''' stock_path = S * np.exp((r - 0.5 * sigma ** 2) * T + sigma * np.sqrt(T) * rand) '''


def black_scholes_merton_delta(S, K, T, r, sigma, option_type='call'):
    T=T/252
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == 'call':
        option_price = norm.cdf(d1)
    elif option_type == 'put':
        option_price = norm.cdf(d1)-1
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")

    return option_price

def black_scholes_merton_gamma(S, K, T, r, sigma, option_type='call'):
    T=T/252
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == 'call':
        option_price = norm.pdf(d1)/(S*sigma* np.sqrt(T))
    elif option_type == 'put':
        option_price = norm.pdf(d1)/(S*sigma* np.sqrt(T))
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")

    return option_price


def black_scholes_merton_theta(S, K, T, r, sigma, option_type='call'):
    T=T/252
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == 'call':
        option_price = -sigma*S*norm.pdf(d1)/(2*np.sqrt(T))-r*K* np.exp(-r*T) * norm.cdf(d2)
    elif option_type == 'put':
        option_price = -sigma*S*norm.pdf(d1)/(2*np.sqrt(T))+r*K* np.exp(-r*T) * norm.cdf(-d2)
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")

    return option_price

def black_scholes_merton_vega(S, K, T, r, sigma, option_type='call'):
    T=T/252
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == 'call':
        option_price = S*norm.pdf(d1)*np.sqrt(T)
    elif option_type == 'put':
        option_price = S*norm.pdf(d1)*np.sqrt(T)
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")

    return option_price

def black_scholes_merton_rho(S, K, T, r, sigma, option_type='call'):
    T=T/252
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == 'call':
        option_price = K*norm.cdf(d2)*T* np.exp(-r*T)
    elif option_type == 'put':
        option_price = -K*norm.cdf(-d2)*T* np.exp(-r*T)
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")

    return option_price
