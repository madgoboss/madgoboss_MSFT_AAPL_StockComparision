#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


# In[24]:


# Assuming you have a list or array of close prices
close_prices_msft = np.array([48.9375,44.6875,53.125,34.875,31.28125,40,34.90625,34.90625,30.15625,34.4375,28.6875,21.6875,30.53125,29.5,27.3437,33.875,34.59,36.5,33.095001,28.5,25.584999,29.07500,32.105,33.125,31.855,29.1,30.155001,26.12999,25.45,27.3,23.99,24.54000,21.870001,26.7350,28.84,25.85,23.73,23.700001,24.209999,25.57,24.610001,25.639999,26.41,26.52,27.799999,26.139999,25.70999,27.370001,27.65,26.530001,24.93,26.129999,26.23,28.559999,28.49,27.299999,27.65,27.969999,26.809999,26.719999,26.280001,25.16,24.1,25.299999,25.799999,24.8,25.61000,27.379,25.73,25.70000,27.6,26.15,28.15,26.870001,27.209999,24.15,22.6,23.299999,24.059999,25.700001,27.3,28.709999,29.360001,29.860001,30.860001,28.17,27.870001,29.94000,30.690001,29.469999,28.99,28.73,29.459999,36.81000,33.599998,35.599998,32.59999,27.20000,28.379999,28.52,28.32,27.5,25.719999,27.290001,26.690,22.33,20.219999,19.440001,17.1,16.15,18.370001,20.26,20.88999,23.77,23.52,24.65,25.719999,27.73,29.41,30.48,28.1,28.67,29.290001,30.540001,25.799999,23.01,25.809999,23.469999,24.49,26.67,25.26,27.91,27.73,26.58,25.389999,25.92,25.01,2,27.4,26.,24.889999,26.629999,25.58,25.959999,29.530001,31.7,32.259998,32.02,29.190001,30.59,29.469999,30.82,29.76,28.540001,26.620001,26.709999,27.45000,27.799999,28.610001,33.099998,34.900002,34.5400,31.84,33.400002,33.27999,35.41,38.130001,37.,37.84,38.310001,40.990002,40.400002,40.939999,41.700001,43.16,45.4,46.360001,46.950001,47.810001,46.450001,40.400002,43.849998,40.66,48.639999,46.86000,44.150002,46.70000,43.52,44.259998,52.639999,54.349998,55.,55.09,50.880001,55.23,49.869999,53,51.169998,56.68,57.459999,57.599998,59.919998,60.259998,62.139999,64.650002,63.98,65.86000,68.459999,69.839996,68.93,72.69999,74.769997,74.489998,83.1,84.169998,85.540001,95.010002,93.769997,91.269997,93.51999,98.839996,98.610001,106.080002,112.330002,114.370003,106.809998,110.889999,101.57,104.43,112.029999,117.940002,130.600006,123.68,133.960007,136.270004,137.860001,139.0299,143.369995,151.380005,157.699997])

# Calculating daily returns
daily_returns_msft = (close_prices_msft[1:] - close_prices_msft[:-1]) / close_prices_msft[:-1] * 100

# Calculating Average daily returns
average_daily_return_msft = np.mean(daily_returns_msft)

# Calculating culmulative returns
cumulative_returns_msft = (close_prices_msft[-1] - close_prices_msft[0]) / close_prices_msft[0] * 100

print("Daily Returns:", daily_returns_msft)
print("Average Daily Return:", average_daily_return_msft)
print("Cumulative Returns:", cumulative_returns_msft)

x =np.array([200001,200002,200003,200004,200005,200006,200007,200008,200009,200010,200011,200012,
             200101,200102,200103,200104,200105,200106,200107,200108,200109,200110,200111,200112,
             200201,200202,200203,200204,200205,200206,200207,200208,200209,200210,200211,200212,
             200301,200302,200303,200304,200305,200306,200307,200308,200309,200310,200311,200312,
             200401,200402,200403,200404,200405,200406,200407,200408,200409,200410,200411,200412,
             200501,200502,200503,200504,200505,200506,200507,200508,200509,200510,200511,200512,
             200601,200602,200603,200604,200605,200606,200607,200608,200609,200610,200611,200612,
             200701,200702,200703,200704,200705,200706,200707,200708,200709,200710,200711,200712,
             200801,200802,200803,200804,200805,200806,200807,200808,200809,200810,200811,200812,
             200901,200902,200903,200904,200905,200906,200907,200908,200909,200910,200911,200112,
             201001,201002,201003,201004,201005,201006,201007,201008,201009,201010,201011,201012,
             201101,201102,201103,200104,201105,201106,201107,201108,201109,201110,201111,201112,
             201201,201202,201203,201204,201205,201206,201207,201208,201209,201210,201211,201212,
             201301,201302,201303,201304,201305,201306,201307,201308,201309,201310,201311,201312,
             201401,201402,201403,201404,201405,201406,201407,201408,201409,201410,201411,201412,
             201501,201502,201503,201504,201505,201506,201507,201508,201509,201510,201511,201512,
             201601,201602,201603,201604,201605,201606,201607,201608,201609,201610,201611,201612,
             201701,201702,201703,201704,201705,201706,201707,201708,201709,201710,201711,201712,
             201801,201802,201803,201804,201805,201806,201807,201808,201809,201810,201811,201812,
             201901,201902,201903,201904,201905,201906,201907,201908,201909,201910,201911,201912])
             
             
plt.scatter(x,close_prices_msft,linestyle='dotted', marker = '.')
plt.xlabel("Year/Month - YYYYMM")
plt.ylabel("USD")
plt.grid(True, linewidth=0.5)
plt.title("Microsoft Close Prices 2000-2019")
plt.show


# In[25]:


# AAPL STOCK PRICES OVER THE YEARS
close_prices_aapl = np.array([3.705357, 4.09375, 4.850446, 4.430804, 3, 3.741071, 3.629464, 4.352679, 1.839286, 1.397321, 1.178571, 1.0625, 1.544643, 1.303571, 1.576429, 1.820714, 1.425, 1.660714, 1.342143, 1.325, 1.107857, 1.254286, 1.521429, 1.564286, 1.765714, 1.55, 1.690714, 1.733571, 1.664286, 1.265714, 1.09, 1.053571, 1.035714, 1.147857, 1.107143, 1.023571, 1.025714, 1.072143, 1.01, 1.015714, 1.282143, 1.361429, 1.505714, 1.615, 1.48, 1.635, 1.493571, 1.526429, 1.611429, 1.708571, 1.931429, 1.841429, 2.004286, 2.324286, 2.31, 2.463571, 2.767857, 3.742857, 4.789286, 4.6, 5.492857, 6.408571, 5.952857, 5.151429, 5.68, 5.258572, 6.092857, 6.698571, 7.658571, 8.227143, 9.688571, 10.27, 10.787143, 9.784286, 8.96, 10.055715, 8.538571, 8.181429, 9.708571, 9.692857, 10.997143, 11.582857, 13.094286, 12.12, 12.247143, 12.087143, 13.272857, 14.257143, 17.312857, 17.434286, 18.822857, 19.782858, 21.924286, 27.135714, 26.031429, 28.297142, 19.337143, 17.860001, 20.5, 24.85, 26.964285, 23.92, 22.707144, 24.218571, 16.237143, 15.37, 13.238571, 12.192857, 12.875714, 12.758572, 15.017143, 17.975714, 19.401428, 20.347143, 23.341429, 24.030001, 26.478571, 26.928572, 28.558571, 30.104286, 27.437143, 29.231428, 33.57143, 37.298573, 36.697144, 35.932858,36.75,34.728573,40.535713,42.997143,44.450001,46.080002,48.474285,50.458572,49.787144,50.01857,49.689999,47.952858,55.782856,54.975716,54.474285,57.825714,54.599998,57.857143,65.211426,77.491432,85.650002,83.425713,82.53286,83.428574,87.251427,95.034286,95.300003,85.045715,83.611427,76.024284,65.07,63.057144,63.237144,63.254284,64.247147,56.647144,64.647141,69.602859,68.10714,74.671425,79.438568,80.145714,71.514282,75.177139,76.677139,84.298569,90.428574,92.93,95.599998,102.5,100.75,108,118.93,110.379997,117.160004,128.460007,124.43,125.150002,130.279999,125.43,121.300003,112.919998,110.300003,119.5,118.300003,105.260002,97.339996,96.690002,108.989998,93.739998,99.860001,95.599998,104.209999,106.099998,113.050003,113.540001,110.519997,115.82,121.349998,136.990005,143.660004,143.649994,152.759995,144.020004,148.729996,164,154.119995,169.039993,171.850006,169.229996,167.429993,178.119995,167.779999,165.259995,186.869995,185.110001,190.289993,227.630005,225.740005,218.860001,178.580002,157.740005,166.440002,173.149994,189.949997,200.669998,175.070007,197.919998,213.039993,208.740005,223.970001,248.759995,267.25,293.649994])
close_prices_msft = np.array([48.9375,44.6875,53.125,34.875,31.28125,40,34.90625,34.90625,30.15625,34.4375,28.6875,21.6875,30.53125,29.5,27.3437,33.875,34.59,36.5,33.095001,28.5,25.584999,29.07500,32.105,33.125,31.855,29.1,30.155001,26.12999,25.45,27.3,23.99,24.54000,21.870001,26.7350,28.84,25.85,23.73,23.700001,24.209999,25.57,24.610001,25.639999,26.41,26.52,27.799999,26.139999,25.70999,27.370001,27.65,26.530001,24.93,26.129999,26.23,28.559999,28.49,27.299999,27.65,27.969999,26.809999,26.719999,26.280001,25.16,24.1,25.299999,25.799999,24.8,25.61000,27.379,25.73,25.70000,27.6,26.15,28.15,26.870001,27.209999,24.15,22.6,23.299999,24.059999,25.700001,27.3,28.709999,29.360001,29.860001,30.860001,28.17,27.870001,29.94000,30.690001,29.469999,28.99,28.73,29.459999,36.81000,33.599998,35.599998,32.59999,27.20000,28.379999,28.52,28.32,27.5,25.719999,27.290001,26.690,22.33,20.219999,19.440001,17.1,16.15,18.370001,20.26,20.88999,23.77,23.52,24.65,25.719999,27.73,29.41,30.48,28.1,28.67,29.290001,30.540001,25.799999,23.01,25.809999,23.469999,24.49,26.67,25.26,27.91,27.73,26.58,25.389999,25.92,25.01,2,27.4,26.,24.889999,26.629999,25.58,25.959999,29.530001,31.7,32.259998,32.02,29.190001,30.59,29.469999,30.82,29.76,28.540001,26.620001,26.709999,27.45000,27.799999,28.610001,33.099998,34.900002,34.5400,31.84,33.400002,33.27999,35.41,38.130001,37.,37.84,38.310001,40.990002,40.400002,40.939999,41.700001,43.16,45.4,46.360001,46.950001,47.810001,46.450001,40.400002,43.849998,40.66,48.639999,46.86000,44.150002,46.70000,43.52,44.259998,52.639999,54.349998,55.,55.09,50.880001,55.23,49.869999,53,51.169998,56.68,57.459999,57.599998,59.919998,60.259998,62.139999,64.650002,63.98,65.86000,68.459999,69.839996,68.93,72.69999,74.769997,74.489998,83.1,84.169998,85.540001,95.010002,93.769997,91.269997,93.51999,98.839996,98.610001,106.080002,112.330002,114.370003,106.809998,110.889999,101.57,104.43,112.029999,117.940002,130.600006,123.68,133.960007,136.270004,137.860001,139.0299,143.369995,151.380005,157.699997])

# Calculating daily returns
daily_returns_aapl = (close_prices_aapl[1:] - close_prices_aapl[:-1]) / close_prices_aapl[:-1] * 100

# Calculating average daily return
average_daily_return_aapl = np.mean(daily_returns_aapl)

# Calculating cumulative returns
cumulative_returns_aapl = (close_prices_aapl[-1] - close_prices_aapl[0]) / close_prices_aapl[0] * 100

print("Daily Returns:", daily_returns_aapl)
print("Average Daily Return:", average_daily_return_aapl)
print("Cumulative Returns:", cumulative_returns_aapl)

x =np.array([200001,200002,200003,200004,200005,200006,200007,200008,200009,200010,200011,200012,
             200101,200102,200103,200104,200105,200106,200107,200108,200109,200110,200111,200112,
             200201,200202,200203,200204,200205,200206,200207,200208,200209,200210,200211,200212,
             200301,200302,200303,200304,200305,200306,200307,200308,200309,200310,200311,200312,
             200401,200402,200403,200404,200405,200406,200407,200408,200409,200410,200411,200412,
             200501,200502,200503,200504,200505,200506,200507,200508,200509,200510,200511,200512,
             200601,200602,200603,200604,200605,200606,200607,200608,200609,200610,200611,200612,
             200701,200702,200703,200704,200705,200706,200707,200708,200709,200710,200711,200712,
             200801,200802,200803,200804,200805,200806,200807,200808,200809,200810,200811,200812,
             200901,200902,200903,200904,200905,200906,200907,200908,200909,200910,200911,200112,
             201001,201002,201003,201004,201005,201006,201007,201008,201009,201010,201011,201012,
             201101,201102,201103,200104,201105,201106,201107,201108,201109,201110,201111,201112,
             201201,201202,201203,201204,201205,201206,201207,201208,201209,201210,201211,201212,
             201301,201302,201303,201304,201305,201306,201307,201308,201309,201310,201311,201312,
             201401,201402,201403,201404,201405,201406,201407,201408,201409,201410,201411,201412,
             201501,201502,201503,201504,201505,201506,201507,201508,201509,201510,201511,201512,
             201601,201602,201603,201604,201605,201606,201607,201608,201609,201610,201611,201612,
             201701,201702,201703,201704,201705,201706,201707,201708,201709,201710,201711,201712,
             201801,201802,201803,201804,201805,201806,201807,201808,201809,201810,201811,201812,
             201901,201902,201903,201904,201905,201906,201907,201908,201909,201910,201911,201912])
             
             
plt.scatter(x,close_prices_msft,linestyle='dotted', marker = '.')
plt.ylabel("USD")
plt.grid(True, linewidth=0.5)
plt.title("Apple Stock Prices - 2000 to 2019")
plt.show


# In[27]:


close_prices_aapl = np.array([3.705357, 4.09375, 4.850446, 4.430804, 3, 3.741071, 3.629464, 4.352679, 1.839286, 1.397321, 1.178571, 1.0625, 1.544643, 1.303571, 1.576429, 1.820714, 1.425, 1.660714, 1.342143, 1.325, 1.107857, 1.254286, 1.521429, 1.564286, 1.765714, 1.55, 1.690714, 1.733571, 1.664286, 1.265714, 1.09, 1.053571, 1.035714, 1.147857, 1.107143, 1.023571, 1.025714, 1.072143, 1.01, 1.015714, 1.282143, 1.361429, 1.505714, 1.615, 1.48, 1.635, 1.493571, 1.526429, 1.611429, 1.708571, 1.931429, 1.841429, 2.004286, 2.324286, 2.31, 2.463571, 2.767857, 3.742857, 4.789286, 4.6, 5.492857, 6.408571, 5.952857, 5.151429, 5.68, 5.258572, 6.092857, 6.698571, 7.658571, 8.227143, 9.688571, 10.27, 10.787143, 9.784286, 8.96, 10.055715, 8.538571, 8.181429, 9.708571, 9.692857, 10.997143, 11.582857, 13.094286, 12.12, 12.247143, 12.087143, 13.272857, 14.257143, 17.312857, 17.434286, 18.822857, 19.782858, 21.924286, 27.135714, 26.031429, 28.297142, 19.337143, 17.860001, 20.5, 24.85, 26.964285, 23.92, 22.707144, 24.218571, 16.237143, 15.37, 13.238571, 12.192857, 12.875714, 12.758572, 15.017143, 17.975714, 19.401428, 20.347143, 23.341429, 24.030001, 26.478571, 26.928572, 28.558571, 30.104286, 27.437143, 29.231428, 33.57143, 37.298573, 36.697144, 35.932858,36.75,34.728573,40.535713,42.997143,44.450001,46.080002,48.474285,50.458572,49.787144,50.01857,49.689999,47.952858,55.782856,54.975716,54.474285,57.825714,54.599998,57.857143,65.211426,77.491432,85.650002,83.425713,82.53286,83.428574,87.251427,95.034286,95.300003,85.045715,83.611427,76.024284,65.07,63.057144,63.237144,63.254284,64.247147,56.647144,64.647141,69.602859,68.10714,74.671425,79.438568,80.145714,71.514282,75.177139,76.677139,84.298569,90.428574,92.93,95.599998,102.5,100.75,108,118.93,110.379997,117.160004,128.460007,124.43,125.150002,130.279999,125.43,121.300003,112.919998,110.300003,119.5,118.300003,105.260002,97.339996,96.690002,108.989998,93.739998,99.860001,95.599998,104.209999,106.099998,113.050003,113.540001,110.519997,115.82,121.349998,136.990005,143.660004,143.649994,152.759995,144.020004,148.729996,164,154.119995,169.039993,171.850006,169.229996,167.429993,178.119995,167.779999,165.259995,186.869995,185.110001,190.289993,227.630005,225.740005,218.860001,178.580002,157.740005,166.440002,173.149994,189.949997,200.669998,175.070007,197.919998,213.039993,208.740005,223.970001,248.759995,267.25,293.649994])
close_prices_msft = np.array([48.9375,44.6875,53.125,34.875,31.28125,40,34.90625,34.90625,30.15625,34.4375,28.6875,21.6875,30.53125,29.5,27.3437,33.875,34.59,36.5,33.095001,28.5,25.584999,29.07500,32.105,33.125,31.855,29.1,30.155001,26.12999,25.45,27.3,23.99,24.54000,21.870001,26.7350,28.84,25.85,23.73,23.700001,24.209999,25.57,24.610001,25.639999,26.41,26.52,27.799999,26.139999,25.70999,27.370001,27.65,26.530001,24.93,26.129999,26.23,28.559999,28.49,27.299999,27.65,27.969999,26.809999,26.719999,26.280001,25.16,24.1,25.299999,25.799999,24.8,25.61000,27.379,25.73,25.70000,27.6,26.15,28.15,26.870001,27.209999,24.15,22.6,23.299999,24.059999,25.700001,27.3,28.709999,29.360001,29.860001,30.860001,28.17,27.870001,29.94000,30.690001,29.469999,28.99,28.73,29.459999,36.81000,33.599998,35.599998,32.59999,27.20000,28.379999,28.52,28.32,27.5,25.719999,27.290001,26.690,22.33,20.219999,19.440001,17.1,16.15,18.370001,20.26,20.88999,23.77,23.52,24.65,25.719999,27.73,29.41,30.48,28.1,28.67,29.290001,30.540001,25.799999,23.01,25.809999,23.469999,24.49,26.67,25.26,27.91,27.73,26.58,25.389999,25.92,25.01,2,27.4,26.,24.889999,26.629999,25.58,25.959999,29.530001,31.7,32.259998,32.02,29.190001,30.59,29.469999,30.82,29.76,28.540001,26.620001,26.709999,27.45000,27.799999,28.610001,33.099998,34.900002,34.5400,31.84,33.400002,33.27999,35.41,38.130001,37.,37.84,38.310001,40.990002,40.400002,40.939999,41.700001,43.16,45.4,46.360001,46.950001,47.810001,46.450001,40.400002,43.849998,40.66,48.639999,46.86000,44.150002,46.70000,43.52,44.259998,52.639999,54.349998,55.,55.09,50.880001,55.23,49.869999,53,51.169998,56.68,57.459999,57.599998,59.919998,60.259998,62.139999,64.650002,63.98,65.86000,68.459999,69.839996,68.93,72.69999,74.769997,74.489998,83.1,84.169998,85.540001,95.010002,93.769997,91.269997,93.51999,98.839996,98.610001,106.080002,112.330002,114.370003,106.809998,110.889999,101.57,104.43,112.029999,117.940002,130.600006,123.68,133.960007,136.270004,137.860001,139.0299,143.369995,151.380005,157.699997])
plt.scatter(x,close_prices_msft,linestyle='dotted', marker = '.')
plt.scatter(x,close_prices_aapl,linestyle='dotted', marker = '.')

plt.legend(["MSFT","AAPL"])
plt.ylabel("USD")
plt.grid(True, linewidth=0.5)
plt.title("Comparision of Stock Prices - 2000 to 2019")
plt.show


# In[ ]:




