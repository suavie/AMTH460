clc;clear all;
%volatility 23% , we consider the
%initial stock price $930.5, risk free interest rate 1%
%and 100 days maturity times, we consider the 252
%trading days and zero dividend yield here. 
strike = [785, 800, 700, 900, 750, 1000];
rate=[0.01, 0.02, 0.03, 0.05, 0.1,0.15];
volatility=[0.23, 0.3, 0.35, 0.2,0.15,0.4];
steppy= [5, 10, 100,1000,2000,5000];
matur=[100, 200, 300,400,50 ,500]/252;

S0=930.5;T=100/252;r=0.01;
sigma=.23;
K=785;
tree_steps = 1000;
simulations=1000;
for i=1:6
variableK(i)=AsianCall(S0,strike(i),r,T,sigma,tree_steps,simulations);
variableT(i)=AsianCall(S0,K,r,matur(i),sigma,tree_steps,simulations);
variableV(i)=AsianCall(S0,K,r,T,volatility(i),tree_steps,simulations);
variableSTEP(i)=AsianCall(S0,K,r,T,sigma,steppy(i),simulations);
variableR(i)=AsianCall(S0,K,rate(i),T,sigma,tree_steps,simulations);
end
variableK=variableK';
variableT=variableT';
variableV=variableV';
variableSTEP=variableSTEP';
variableR=variableR';
tt=table(strike',variableK,matur'.*252,variableT,volatility',variableV,steppy',variableSTEP,rate',variableR);
writetable(tt,'asiantable.csv')







