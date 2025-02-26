import scipy.stats as stats
table=[[60,54,46,41],
      [40,44,53,57]]
chi2,p_value,_,_=stats.chi2_contingency(table)
print("The chi_square value is -",chi2)
print("The p-value is",p_value)
if p_value <0.05:
    print("gender and education are dependent")
else:
    print("Are not Dependent")
