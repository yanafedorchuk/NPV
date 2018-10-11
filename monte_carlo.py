
price = np.array([6, 6.05, 6.1])
volume = np.array([802000, 967000, 1132000])
profit = price * volume
cost = 0.55 * profit
gross_profit = profit - cost 
oper_cost = 0.15 * gross_profit
net_profit = gross_profit - oper_cost 
tax = net_profit * 0.32
cash_flow = net_profit - tax


cash_flow = np.append(-3400000, cash_flow )

npv = np.npv(0.1,cash_flow)

irr = np.irr(cash_flow)

print(volume)  
print(cash_flow) 
print(npv)
print(irr)



import numpy.random as npr

price = npr.triangular([5.9,5.95,6], [6,6.05,6.1],  [6.1,6.15,6.2] , 3)
volume = npr.normal([802,967,1132], [25,30,25], 3)

cost_coef = npr.triangular(0.5, 0.55, 0.65) 
oper_coef = npr.normal(0.15, 0.02) 

cash_flow = ( 1 -  cost_coef ) * (1 - oper_coef ) * ( 1 - 0.32)    * price * volume   

cash_flow = np.append(-3400000, cash_flow )

npv = np.npv(0.1,cash_flow)

irr = np.irr(cash_flow)

print(volume)  
print(cash_flow) 
print(npv)
print(irr)
plt.hist(npv, bins=20,range=[-750000, 1000000], facecolor='NAVY', align='mid',histtype='bar') 
tick_val = [-750000, -500000, -250000,0, 250000, 500000, 750000,1000000] 
tick_lab = ['-750K', '-500k', '-250K','0K','250K','500K','750K', '1000K'] 
plt.title('NPV') 
plt.text(630000, 800, r'$\mu=100,\ \sigma=15$') 
plt.xticks(tick_val,tick_lab) 
plt.show()
