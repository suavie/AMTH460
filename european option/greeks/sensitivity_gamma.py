from lib.tools import *
import pandas as pd

S_l=[930.5, 700, 800, 900, 1000, 1100]
K_l = [785, 800, 700, 900, 750, 1000]
T_l = [100, 200, 300,400,50 ,500]
r_l = [0.01, 0.02, 0.03, 0.05, 0.1,0.15]
vol_l = [0.23, 0.3, 0.35, 0.2,0.15,0.4]
tree_steps_l = [100, 5, 10, 1000,2000,5000]

#S = S_l[0]
K = K_l[0]
T = T_l[0]
r = r_l[0]
vol = vol_l[0]
tree_steps = tree_steps_l[0]
ds=30

ck = []
for S in S_l:
    ck1 = (binomial_tree_option_price(S+ds,K,T,r,vol,tree_steps)-2*binomial_tree_option_price(S,K,T,r,vol,tree_steps)+binomial_tree_option_price(S-ds,K,T,r,vol,tree_steps))/(ds**2)
    ck2 = (trinomial_tree_option_price(S+ds,K,T,r,vol,tree_steps)-2*trinomial_tree_option_price(S,K,T,r,vol,tree_steps)+trinomial_tree_option_price(S-ds,K,T,r,vol,tree_steps))/(ds**2)
    ck3 = (monte_carlo_option_price(S+ds,K,T,r,vol,tree_steps)-2*monte_carlo_option_price(S,K,T,r,vol,tree_steps)+monte_carlo_option_price(S-ds,K,T,r,vol,tree_steps))/(ds**2)
    ck4 = black_scholes_merton_gamma(S,K,T,r,vol)
    ck.append([ck1,ck2,ck3,ck4])

print("With S ="+str(S_l)+"\n")
data = {"S" : S_l,
        "BM" : [item[0] for item in ck],
        "TM" : [item[1] for item in ck],
        "MC" : [item[2] for item in ck],
        "BS" : [item[3] for item in ck]}
df = pd.DataFrame(data)
df.to_csv('S_variable_gamma.csv', index=False)

print("All data printed") 