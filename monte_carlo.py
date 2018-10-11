
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

plt.violinplot(npv, positions=None, vert=True, widths=0.5, showmeans=False, showextrema=True, showmedians=False, points=100)
plt.boxplot(npv, whis=[1, 99], notch=True, widths=0.3)

plt.show()




numb_iter = 10000
   
npv_all = []
irr_all = [] 
price1 = np.random.triangular(5.9, 6, 6.1, numb_iter)
price2 = np.random.triangular(5.95, 6.05, 6.15, numb_iter)
price3 = np.random.triangular(6, 6.1, 6.2, numb_iter) 
volume1 = np.random.normal(802, 25, numb_iter) * 100
volume2 = np.random.normal(967, 30, numb_iter) * 100
volume3 = np.random.normal(1132, 25, numb_iter) * 100
cost_coef = npr.triangular(0.5, 0.55, 0.65,numb_iter) 
oper_coef = npr.normal(0.15, 0.02,numb_iter) 
npv_all = { np.npv(0.1, np.append(-340000, ( 1 - 0.32)*(1 - oper_coef[i])*(1 - cost_coef[i])*np.array([price1[i]*volume1[i], price2[i]*volume2[i], price3[i]*volume3[i]])))  for i in np.arange(numb_iter)}  
irr_all = { np.irr(np.append(-340000, ( 1 - 0.32)*(1 - oper_coef[i])*(1 - cost_coef[i])*np.array([price1[i]*volume1[i], price2[i]*volume2[i], price3[i]*volume3[i]])))  for i in np.arange(numb_iter)}  
    

print(np.mean(npv_all))
print(np.mean(irr_all))

