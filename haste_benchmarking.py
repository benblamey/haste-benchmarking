
# coding: utf-8

# In[35]:


import csv
import itertools
import functools


# In[53]:


spamReader = csv.DictReader(open('benchmarking-simulator,2018-01-29.csv'), delimiter=',')

"""
            'benchmarking',
            'file',
            'topic',
            'description',
            'started_at_time',
            'ended_time',
            'duration_secs',
            'number_of_bytes'
"""
rows = []
for row in spamReader:
    rows.append(dict(row))
    
print(rows)   


# In[79]:


rows.sort(key=lambda row: row['topic'])
grouped_by_topic = itertools.groupby(rows, lambda row: row['topic'])

totals = {}

for (topic, group) in grouped_by_topic:
    #print(topic)
    durations = list(map(lambda x: float(x['duration_secs']), group))
    #print(durations)
    
    #print ('total durations: ')
    total_duration = functools.reduce(lambda x, y: x + y, durations)
    print()
    totals[topic] = total_duration

print(totals)

total = totals['stream_all_images']

for k,v in totals.items():
    print(k + ' '+ str(v / total * 100) + ' %')
    

