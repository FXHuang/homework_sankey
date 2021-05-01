#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd # import pands to handle csv
from pyecharts.charts import Page,Sankey 
from pyecharts import options as opts
import collections # try to use OrderedDict


# In[36]:


data = pd.read_csv('sankey_exercise1.csv',sep = ';',encoding = 'utf-8',header=None) # data and data stream(hidden stored) are stored in this csv 
print(data)


# In[37]:


nodes = []
nodes.append({'name':'A1'})
for i in data[0].unique():
    dictnode = {}
    dictnode = collections.OrderedDict()
    dictnode['name'] = i
    nodes.append(dictnode)
print(nodes)


# In[38]:


links = []
for i in data.values:
    diclink = {}
    diclink = collections.OrderedDict()
    diclink['source'] = i[0]
    diclink['target'] = i[1]
    diclink['value'] = i[2]
    links.append(diclink)
print(links)


# In[39]:


c = (Sankey().add("scale/tone",nodes,links,linestyle_opt=opts.LineStyleOpts(opacity=0.2, curve=0.5, color="source",type_="dotted"),label_opts=opts.LabelOpts(position="right",),).set_global_opts(title_opts=opts.TitleOpts(title="sankey_exercise1")))
c.render('result0430.html')

