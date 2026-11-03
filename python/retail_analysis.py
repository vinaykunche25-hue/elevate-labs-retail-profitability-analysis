import pandas as pd\nimport matplotlib.pyplot as plt\nimport seaborn as sns\ndf = pd.read_csv('../data/cleaned/retail_transactions_cleaned.csv', parse_dates=['order_date'])\ndf.head()

print(df.shape)\ndf.info()\ndisplay(df.describe(include='all').T)\nprint('Missing values:', df.isna().sum().sum())\nprint('Duplicate rows:', df.duplicated().sum())

kpis = {'Sales':df.sales.sum(),'Profit':df.profit.sum(),'Profit margin %':df.profit.sum()/df.sales.sum()*100,'Orders':df.order_id.nunique(),'Customers':df.customer_id.nunique()}\npd.Series(kpis).round(2)

category = df.groupby('category').agg(sales=('sales','sum'),profit=('profit','sum'))\ncategory['margin_pct']=category.profit/category.sales*100\ndisplay(category.round(2))\nsubcategory = df.groupby('sub_category').agg(sales=('sales','sum'),profit=('profit','sum')).sort_values('profit')\ndisplay(subcategory.round(2))\ncategory.profit.plot(kind='bar',title='Profit by Category'); plt.tight_layout(); plt.show()

region = df.groupby('region').agg(sales=('sales','sum'),profit=('profit','sum')).sort_values('sales',ascending=False)\ndisplay(region.round(2))\nmonthly=df.assign(month=df.order_date.dt.to_period('M').astype(str)).groupby('month').sales.sum()\nmonthly.plot(figsize=(11,4),marker='o',title='Monthly Sales Trend'); plt.xticks(rotation=60); plt.tight_layout(); plt.show()

df['discount_band']=pd.cut(df.discount_pct,[-.001,.1,.2,.3,1],labels=['0-9%','10-19%','20-29%','30%+'])\ndisplay(df.groupby('discount_band',observed=False).agg(line_items=('order_id','size'),avg_profit=('profit','mean'),total_profit=('profit','sum')).round(2))\nsns.scatterplot(data=df,x='discount_pct',y='profit',alpha=.4); plt.title('Discount vs Profit'); plt.show()\ndisplay(df.groupby('product_name').agg(avg_inventory_days=('inventory_days','mean'),total_profit=('profit','sum')).query('avg_inventory_days>=60').sort_values('avg_inventory_days',ascending=False).head(15))

numeric=df[['discount_pct','inventory_days','quantity','sales','profit']]\ndisplay(numeric.corr().round(2))\nsns.heatmap(numeric.corr(),annot=True,cmap='coolwarm',center=0); plt.tight_layout(); plt.show()