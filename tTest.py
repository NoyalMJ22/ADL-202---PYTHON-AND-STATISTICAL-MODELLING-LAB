import scipy.stats as stats

n=16
SD=3
mean=22
prevmean=20
t_stat=(mean-prevmean)/(SD/(n**0.5))
p_value=2*(1-stats.t.cdf(abs(t_stat),df=n-1))
print("the p-value is-",p_value)
print("THe t-stat value is-",t_stat)
if p_value < 0.05:
    print("Reject Null hypothesis,new truck diff MPG")
else:
    print("No Diff in MPG")
