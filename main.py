import pandas as pd

data = pd.read_csv(r'C:\Users\Kim\PycharmProjects\falltech_2021_profit_margin_pricer\Faltech edited price sheet.csv')

df = pd.DataFrame(data)
print(df.head())

# df[' NEW PRICE '] = df[' NEW PRICE '].str.replace('$', '').str.replace(',', '')


# print(df[' NEW PRICE '])
#calculates our cost from list price

df['equipdirectcost1'] = df['2021 List Price1'].astype(float) - 0.37 * df['2021 List Price1'].astype(float)
df['equipdirectcost2'] = df['2021 List Price2'].astype(float) - 0.37 * df['2021 List Price2'].astype(float)
df['equipdirectcost3'] = df['2021 List Price3'].astype(float) - 0.37 * df['2021 List Price3'].astype(float)

# increases by a 25% profit margin from our cost

df['25 Percent Profit Margin1'] = (df['equipdirectcost1'].astype(float)/(1 - 0.25))
df['25 Percent Profit Margin2'] = (df['equipdirectcost2'].astype(float)/(1 - 0.25))
df['25 Percent Profit Margin3'] = (df['equipdirectcost3'].astype(float)/(1 - 0.25))

df['25 Percent Profit Margin1'] = df['25 Percent Profit Margin1'].round(2)
df['25 Percent Profit Margin2'] = df['25 Percent Profit Margin2'].round(2)
df['25 Percent Profit Margin3'] = df['25 Percent Profit Margin3'].round(2)

print(df['25 Percent Profit Margin1'])
print(df['25 Percent Profit Margin2'])
print(df['25 Percent Profit Margin3'])
df.to_csv(r'C:\Users\Kim\PycharmProjects\falltech_2021_profit_margin_pricer/'
          r'falltech_2021_prices_with_25_percent_profit_margin_from_equip_direct_cost.csv')
