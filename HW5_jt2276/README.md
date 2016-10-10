## HW5

For assignments 1 & 2 I worked with Chistian Rosado, Dana Karwas and Adrian Dahlin. I focused mainly on explaining the foundations of the statistical test to the group, while collectively we worked on actually implementing them.

For assignment 1, we picked the KS and AD test as our goodness of fit test and then loaded in both the January and June 2015 citibike data, and extracted the ages of all subscribers (customers did not have that data available). We then ran the KS test twice to compare the ages to both a normal and chi squared distribution with parameters estimated from the data. In both cases we were able to reject the null hypothesis that the ages came from those specific distributions. We then ran the AD test twice to see if the ages came from either a gaussian or exponential family for distributions, and in both cases we rejected the null and concluded that the ages did not follow either family of distributions.

For assignment 2, we worked through the skeleton notebook by storing the 2013 census pay data in two dictionaries by gender and by race, then exploring the data using a scatter matrix. We then attempted to fit a least squares regression line to total median pay data by gender to determine if there was evidence of pay inequality, which there was. We then added significantly more data to the mix and examined how the least squares line adjusted accordingly, and finally used the line to predict female income for a given male income.

For assignment 3, which is below, I worked alone.

1) The 'control group' will refer to participants who are asked to regularly perform medium to light exercise for 6 weeks, while the 'test group' will refer to participants who are asked to go on a low-carb diet for 6 weeks. Weights are measured before and after the 6 weeks.
Null hypothesis: The mean weight lost by the control group is greater than or equal to the mean weight lost by the test group.
    mu_control >= mu_test

2) Null hypothesis: The true proportion of the US population 'p' that would answer 'yes Bill Clinton does have the honesty and integrity you expect in a president' is less than or equal to 0.5.
    p <= 0.5

3) Null hypothesis: The proportion of smokers who successfully quit smoking using the nicotine patch is less than or equal to the proportion that quit using a placebo patch.
    p_nicotine <= p_control

4) Null hypothesis: The yearly increase in IQ averaged over ages 1-4 for children born to smokers is the same or higher than that of children born to non-smokers.
    mu_smoker >= mu_nonsmoker
