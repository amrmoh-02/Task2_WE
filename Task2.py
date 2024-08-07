import pandas as pd

# file_path = 'insurance-data.csv'
insurance_data = pd.read_csv('insurance-data.csv')

# 1. Calculate the percentage of female smokers
#total_females = insurance_data[insurance_data['sex'] == 'female'].shape[0]
#female_smokers = insurance_data[(insurance_data['sex'] == 'female') & (insurance_data['smoker'] == 'yes')].shape[0]
#percentage_female_smokers = (female_smokers / total_females) * 100

# 1.1 Calculate the percentage of female smokers from the entire dataset
total_people = insurance_data.shape[0]
female_smokers = insurance_data[(insurance_data['sex'] == 'female') & (insurance_data['smoker'] == 'yes')].shape[0]
percentage_female_smokers = (female_smokers / total_people) * 100

# 2. Find the region with the maximum insurance charges
max_insurance_region = insurance_data.groupby('region')['charges'].max().idxmax()

# 3. Find the gender with the maximum insurance charges
#max_insurance_gender = insurance_data.groupby('sex')['charges'].sum().idxmax()
max_insurance_gender = insurance_data.groupby('sex')['charges'].max().idxmax()

# 4. Calculate the average age of female smokers
average_age_female_smokers = insurance_data[(insurance_data['sex'] == 'female') & (insurance_data['smoker'] == 'yes')]['age'].mean()

# 5. Calculate the percentage of males with children
total_males = insurance_data[insurance_data['sex'] == 'male'].shape[0]
males_with_children = insurance_data[(insurance_data['sex'] == 'male') & (insurance_data['children'] > 0)].shape[0]
percentage_males_with_children = (males_with_children / total_males) * 100

# 6. Calculate the percentage of females with children
total_females = insurance_data[insurance_data['sex'] == 'female'].shape[0]
females_with_children = insurance_data[(insurance_data['sex'] == 'female') & (insurance_data['children'] > 0)].shape[0]
percentage_females_with_children = (females_with_children / total_females) * 100

# 7. Find the maximum number of children associated with male parents
max_children_male = insurance_data[insurance_data['sex'] == 'male']['children'].max()

# 8. Find the maximum number of children associated with female parents
max_children_female = insurance_data[insurance_data['sex'] == 'female']['children'].max()

# 9. Find the region with the maximum total insurance charges for females
female_total_charges_by_region = insurance_data[insurance_data['sex'] == 'female'].groupby('region')['charges'].sum()
max_female_insurance_region = female_total_charges_by_region.idxmax()

# Print the results
print("Percentage of female smokers: ", percentage_female_smokers)
print("City with the maximum insurance rate: ", max_insurance_region)
print("Gender with the maximum insurance rate: ", max_insurance_gender)
print("Average age of female smokers: ",average_age_female_smokers)
print("Percentage of males with children insurance: ", percentage_males_with_children)
print("Percentage of females with children insurance: ", percentage_females_with_children)
print("Maximum number of children associated with male parents: ", max_children_male)
print("Maximum number of children associated with female parents: ", max_children_female)
print("City with the maximum total insurance charge for females: ", max_female_insurance_region)
