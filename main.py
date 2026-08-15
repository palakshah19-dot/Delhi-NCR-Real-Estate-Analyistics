import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data.csv')
# print(df.info())

# data cleaning
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
print(df.columns.tolist())
df= df.drop_duplicates()  

# numerical columns cleaning
df["price"] = df["price"].astype(str).str.replace(",", "").astype(float)
df["area"] = df["area"].astype(str).str.replace(",", "").astype(int)
# print(df[["area", "price"]])
df["rate_per_sqft"] = df["rate_per_sqft"].astype(str).str.replace(",", "").astype(int)
# print(df["rate_per_sqft"])

# print(df.info())

# categorical columns cleaning
df["status"] = df["status"].str.strip().str.lower()
df["rera_approval"] = df["rera_approval"].str.strip().str.lower().map({'approved by rera': True, 'not approved by rera': False})
df["flat_type"] = df["flat_type"].str.strip().str.lower()
# print(df["rera_approval"])

df = df.drop_duplicates()

# print(df)
# print(df.info())

# 1.Which is the costliest flat in the dataset?
costliest_flat = df.loc[df['price'].idxmax()]
print(f"The costliest flat is a {costliest_flat['bhk_count']} BHK apartment located in {costliest_flat['locality']}, priced at {costliest_flat['price']/10000000} crores in {costliest_flat['society']} society.")

# 2.Which locality has the highest average price?
locality_avg_price = df.groupby('locality')['price'].mean().sort_values(ascending=False).head(1)
print(f"The locality with the highest average price is {locality_avg_price.index[0]} with an average price of {locality_avg_price.values[0]/10000000} crores.")


# 3. Which locality has the highest rate per square foot?
locality_avg_rate = df.groupby('locality')['rate_per_sqft'].mean().sort_values(ascending=False).head(1)
print(f"The locality with the highest average rate per square foot is {locality_avg_rate.index[0]} with an average rate of {locality_avg_rate.values[0]} per square foot.")

# 4.Do ready-to-move properties cost more than under-construction properties?
ready_to_move_avg_price = df[df['status'] == 'ready to move']['price'].mean()
under_construction_avg_price = df[df['status'] == 'under construction']['price'].mean()
print(f"Ready-to-move: {ready_to_move_avg_price/10000000} crores | Under-construction: {under_construction_avg_price/10000000} crores")

# 5. Do RERA-approved properties command a price premium?
rera_approved_avg_price = df[df['rera_approval'] == True]['price'].mean()
rera_not_approved_avg_price = df[df['rera_approval'] == False]['price'].mean()
print(f"RERA-approved properties have an average price of {rera_approved_avg_price/10000000} crores, while non-RERA-approved properties have an average price of {rera_not_approved_avg_price/10000000} crores.")

# 6. How does area (sqft) impact property price?
sns.scatterplot(data=df, x='area', y='price')
plt.title('Area vs Price')
plt.xlabel('Area (sqft)')
plt.ylabel('Price (in crores)')
plt.show()

# 7.Which BHK configuration is the most expensive based pn per square foot rate?
bhk_avg_rate = df.groupby('bhk_count')['rate_per_sqft'].mean().sort_values(ascending=False).head(1)
print(f"The {bhk_avg_rate.index[0]} BHK configuration is the most expensive on average with a rate of {bhk_avg_rate.values[0]} per square foot.")

# # 8. Which property type (Apartment, Floor, Plot) is the costliest?
property_type_avg_rate = df.groupby('flat_type')['rate_per_sqft'].mean().sort_values(ascending=False).head(1)
print(f"The {property_type_avg_rate.index[0]} property type is the costliest with an average rate of {property_type_avg_rate.values[0]} per square foot.")

# 9. Do certain builders price higher?
print("that top 5 builders which price higher are:")
builder_avg_rate = df.groupby('company_name')['rate_per_sqft'].mean().sort_values(ascending=False).head(5)
for i, (builder, rate) in enumerate(builder_avg_rate.items(), start=1):
    print(f"{i}. {builder}: {rate}")


# 10. Are larger homes always more expensive per square foot?
sns.scatterplot(data=df, x='area', y='rate_per_sqft')
plt.title('Area vs Rate per Square Foot') 
plt.xlabel('Area (sqft)')
plt.ylabel('Rate per Square Foot')
plt.show()


