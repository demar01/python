# %% 
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
# %% 
def plot_functions_linearspace(functions, titles, space):
    """
    creates a grid plot with the gicen functions and the explore linear space 
    """
    plt.figure(figsize=(11,11))
    
    for index,function in enumerate(functions):
        plt.subplot(2, 2, index+1)
        plt.plot(space, function)
        plt.title(titles[index],fontsize=16)

linear_space = np.linspace(0,100,111)
fav_functions = [np.sin(linear_space), np.cos(linear_space), np.exp(linear_space), np.log(linear_space)]
titles = ['Sine function', 'Cosine function', 'Exponential function', 'Logarithmic function']

plot_functions_linearspace(fav_functions,titles,linear_space)
plt.savefig(os.path.join(os.path.dirname(__file__),'plot_functions_linearspace.pdf'))


def tidy_concatenation(dataframe1: 'PandasDataFrame', dataframe2:'PandasDataFrame' ) -> 'PandasDataFrame' :
    """
    takes two dataframes, adds a colum called year and merged the two data frames in a final tidy format
    """
    dataframe1['year'] = np.repeat(2020,dataframe1.shape[0])
    dataframe2['year'] = np.repeat(2021,dataframe1.shape[0])
    sales = pd.concat([dataframe1,dataframe2], ignore_index=True)
    return(sales)

sales_2020 = pd.DataFrame([['chair',20],['sofa',24],['table',15]],columns=['product','sales_units'])
sales_2021 = pd.DataFrame([['chair',20],['sofa',24],['table',15]],columns=['product','sales_units'])
print(tidy_concatenation(sales_2020,sales_2021))

#%% 
index = ['Firefox', 'Chrome', 'Safari', 'IE10', 'Konqueror']
df = pd.DataFrame({'http_status': [np.nan,'-',404,404,301], 'response_time': [0.04, 0.02, 0.07, 0.08, 1.0]}, index=index)
new_index= ['Safari', 'Iceweasel', 'Comodo Dragon', 'IE10', 'Chrome']
df.reindex(new_index)
print(df)
print(df.isnull().sum())
df.dropna(inplace=True)
print(df)
#%% 
def myargmax(Qtable, axis):
    """
    Returns the indices of the maximum values along an axis.
    """
    policy = np.argmax(Q_table.values, axis=axis)
    return(policy)

Q_table = pd.DataFrame({'a0':[10,4,3],'a1':[1,2,8],'a2':[4,5,1]},index=['s0','s1','s2'])
print(myargmax(Q_table,0))
print(myargmax(Q_table,1))

#%% 
def histogram_plot(bin):
    rng = np.random.RandomState(bin)
    a = np.hstack((rng.normal(size=1000),rng.normal(loc=5, scale=2, size=1000)))
    _ = plt.hist(a, bins='auto') 
    fig=plt.figure(figsize=(11,11))
    plt.plot()
    return fig
    
histogram_plot(10) 
plt.savefig(os.path.join(os.path.dirname(__file__),'histogram_plot_10.pdf'))

#%% 
def squeeze_find(array):
    """
    squeeze the array and return a new array with 'pass'/'nonpass' depending on condition.
    """
    np.squeeze(array).shape
    newarray = np.where(array>1, 'pass','nonpass')
    return newarray

scores = np.array([[ 30,   1,  10,  80]])
print(squeeze_find(scores))


#%% 
def balance_table(freq=12,rate=.0675, nper=30 ,pv=200000) -> np.ndarray:
    """
    To calculate FV we need to calculate PMT first. NumPy comes preloaded with a handful of financial functions.
    """
    def future_value:
        periods = np.arange(1, nper + 1, dtype=int)
        principal = np.ppmt(rate, periods, nper, pv)
        interest = np.ipmt(rate, periods, nper, pv)
        pmt = principal + interest
        d = (1 + rate) ** nper  # Discount factor
        fv = pv * d - pmt * (d - 1) / rate
        return periods,principal, interest, 
    
    cols = ['beg_bal', 'prin', 'interest', 'end_bal']
    data = [future_value(pv, rate, periods - 1, -pmt),
    principal, interest,  balance(pv, rate, periods, -pmt)]
    table = pd.DataFrame(data, columns=periods, index=cols).T
    table.index.name =  'month'
    with pd.option_context('display.max_rows', 6):
        print(table.round(2))
    final_month = periods[-1]
    print(np.allclose(table.loc[final_month, 'end_bal'], 0))
    
  