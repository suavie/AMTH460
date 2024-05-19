from lib.tools import *
import pandas as pd

S = 930.5
K_l = [785, 800, 700, 900, 750, 1000]
q_l= [ 0.008,0.001,0.003,0.004,0.006,0.002]
T_l = [100, 200, 300,400,50 ,500]
r_l = [0.01, 0.02, 0.03, 0.05, 0.1,0.15]
vol_l = [0.23, 0.3, 0.35, 0.2,0.15,0.4]
tree_steps_l = [5, 10, 100,1000,2000,5000]

#K = K_l[0]
T = T_l[0]
r = r_l[0]
q = q_l[0]
vol = vol_l[0]
tree_steps = tree_steps_l[0]

ck = []
for K in K_l:
    ck1 = binomial_tree_option_price(S,K,T,r,vol,q,tree_steps)
    ck2 = trinomial_tree_option_price(S,K,T,r,vol,q,tree_steps)
    ck3 = monte_carlo_option_price(S,K,T,r,vol,q,tree_steps)
    ck4 = black_scholes_merton(S,K,T,r,vol,q)
    ck.append([ck1,ck2,ck3,ck4])

K = K_l[0]
#T = T_l[0]
r = r_l[0]
q = q_l[0]
vol = vol_l[0]
tree_steps = tree_steps_l[0]

ct = []

for T in T_l:
    ct1 = binomial_tree_option_price(S,K,T,r,vol,q,tree_steps)
    ct2 = trinomial_tree_option_price(S,K,T,r,vol,q,tree_steps)
    ct3 = monte_carlo_option_price(S,K,T,r,vol,q,tree_steps)
    ct4 = black_scholes_merton(S,K,T,r,vol,q)
    ct.append([ct1,ct2,ct3,ct4])

K = K_l[0]
T = T_l[0]
q = q_l[0]
#r = r_l[0]
vol = vol_l[0]
tree_steps = tree_steps_l[0]

cr = []

for r in r_l:
    cr1 = binomial_tree_option_price(S,K,T,r,vol,q,tree_steps)
    cr2 = trinomial_tree_option_price(S,K,T,r,vol,q,tree_steps)
    cr3 = monte_carlo_option_price(S,K,T,r,vol,q,tree_steps)
    cr4 = black_scholes_merton(S,K,T,r,vol,q)
    cr.append([cr1,cr2,cr3,cr4])

K = K_l[0]
T = T_l[0]
r = r_l[0]
q = q_l[0]
#vol = vol_l[0]
tree_steps = tree_steps_l[0]

cv = []

for vol in vol_l:
    cv1 = binomial_tree_option_price(S,K,T,r,vol,q,tree_steps)
    cv2 = trinomial_tree_option_price(S,K,T,r,vol,q,tree_steps)
    cv3 = monte_carlo_option_price(S,K,T,r,vol,q,tree_steps)
    cv4 = black_scholes_merton(S,K,T,r,vol,q)
    cv.append([cv1,cv2,cv3,cv4])

K = K_l[0]
T = T_l[0]
r = r_l[0]
vol = vol_l[0]
q = q_l[0]
#tree_steps = tree_steps_l[0]

cts = []

for tree_steps in tree_steps_l:
    cts1 = binomial_tree_option_price(S,K,T,r,vol,q,tree_steps)
    cts2 = trinomial_tree_option_price(S,K,T,r,vol,q,tree_steps)
    cts3 = monte_carlo_option_price(S,K,T,r,vol,q,tree_steps)
    cts4 = black_scholes_merton(S,K,T,r,vol,q)
    cts.append([cts1,cts2,cts3,cts4])

K = K_l[0]
T = T_l[0]
r = r_l[0]
vol = vol_l[0]
#q = q_l[0]
tree_steps = tree_steps_l[0]

cqs = []

for q in q_l:
    cqs1 = binomial_tree_option_price(S,K,T,r,vol,q,tree_steps)
    cqs2 = trinomial_tree_option_price(S,K,T,r,vol,q,tree_steps)
    cqs3 = monte_carlo_option_price(S,K,T,r,vol,q,tree_steps)
    cqs4 = black_scholes_merton(S,K,T,r,vol,q)
    cqs.append([cqs1,cqs2,cqs3,cqs4])


print("Base case: S0 = "+str(S)+", K = "+str(K)+", r = "+str(r)+", vol = "+str(vol)+", steps = "+str(tree_steps))
print("With K ="+str(K_l)+"\n")
data = {"K" : K_l,
        "BM" : [item[0] for item in ck],
        "TM" : [item[1] for item in ck],
        "MC" : [item[2] for item in ck],
        "BS" : [item[3] for item in ck]}
df = pd.DataFrame(data)
df.to_csv('K_variable.csv', index=False)
print("With T ="+str(T_l)+"\n")
data = {"T" : T_l,
        "BM" : [item[0] for item in ct],
        "TM" : [item[1] for item in ct],
        "MC" : [item[2] for item in ct],
        "BS" : [item[3] for item in ct]}
df = pd.DataFrame(data)
df.to_csv('T_variable.csv', index=False)
print("With vol ="+str(vol_l)+"\n")
data = {"vol" : vol_l,
        "BM" : [item[0] for item in cv],
        "TM" : [item[1] for item in cv],
        "MC" : [item[2] for item in cv],
        "BS" : [item[3] for item in cv]}
df = pd.DataFrame(data)
df.to_csv('vol_variable.csv', index=False)
print("With r ="+str(r_l)+"\n")
data = {"r" : r_l,
        "BM" : [item[0] for item in cr],
        "TM" : [item[1] for item in cr],
        "MC" : [item[2] for item in cr],
        "BS" : [item[3] for item in cr]}
df = pd.DataFrame(data)
df.to_csv('r_variable.csv', index=False)
print("With TreeSteps ="+str(tree_steps_l)+"\n")
data = {"TreeSteps" : tree_steps_l,
        "BM" : [item[0] for item in cts],
        "TM" : [item[1] for item in cts],
        "MC" : [item[2] for item in cts],
        "BS" : [item[3] for item in cts]}
df = pd.DataFrame(data)
df.to_csv('TreeSteps_variable.csv', index=False)

print("With Dividends ="+str(q_l)+"\n")
data = {"TreeSteps" : q_l,
        "BM" : [item[0] for item in cqs],
        "TM" : [item[1] for item in cqs],
        "MC" : [item[2] for item in cqs],
        "BS" : [item[3] for item in cqs]}
df = pd.DataFrame(data)
df.to_csv('Dividends_variable.csv', index=False)


print("All data printed")


