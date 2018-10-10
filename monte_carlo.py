
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
