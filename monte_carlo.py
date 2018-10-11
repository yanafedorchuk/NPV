
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


np.random.seed(0)
nSimulatation = 10000

#для price треугольное распределение
price1 = np.random.triangular(5.9, 6, 6.1, size=nSimulatation)
price2 = np.random.triangular(5.95, 6.05, 6.15, size=nSimulatation)
price3 = np.random.triangular(6, 6.1, 6.2, size=nSimulatation)

#для объема продаж нормальное распределение
volume1 = np.random.normal(loc=802000 , scale=25000 , size =nSimulatation)
volume2 = np.random.normal(loc=967000 , scale=30000 , size =nSimulatation)
volume3 = np.random.normal(loc=1132000 , scale=25000 , size =nSimulatation)

#для себестоимости треугольное распределение
cost_per = np.random.triangular(0.5, 0.55, 0.65, size=nSimulatation)

#для операционных издержек нормальное распределение
oper_cost_per = np.random.normal(loc=0.15, scale=0.02 , size =nSimulatation)

#вычисляем
npv =[]
irr =[]

#можно попробовать переделать, чтоб убрать цикл
for i in np.arange(nSimulatation):
    profit1 = price1[i]*volume1[i]
    profit2 = price2[i]*volume2[i]
    profit3 = price3[i]*volume3[i]
    profit = np.array([profit1, profit2, profit3])
    cost = cost_per[i] * profit
    gross_profit = profit - cost
    oper_cost = oper_cost_per[i] * gross_profit
    net_profit = gross_profit - oper_cost 
    tax = net_profit * 0.32
    cash_flow = net_profit - tax
    cash_flow = np.append(-3400000, cash_flow )   
    npvv = np.npv(0.1, cash_flow)
    irrr = np.irr(cash_flow)
    npv.append(npvv)
    irr.append(irrr)
    
#итог
print(max(npv))

#без цикла
npv1 = []
npv1 = {np.npv(0.1, np.append(-340000, 0.68*(1 - oper_cost_per[i])*(1 - cost_per[i])*np.array([price1[i]*volume1[i], price2[i]*volume2[i], price3[i]*volume3[i]]))) for i in np.arange(10000)}     



print(max(npv1))

#графики
plt.hist(npv)
