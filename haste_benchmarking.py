
# coding: utf-8

# In[35]:


import csv
import itertools
import functools


# In[93]:


spamReader = csv.DictReader(open('benchmarking-simulator,2018-01-29-b.csv'), delimiter=',')

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
    
#print(rows)   


# In[102]:


rows.sort(key=lambda row: row['topic'])
grouped_by_topic = itertools.groupby(rows, lambda row: row['topic'])

totals = {}

for (topic, group) in grouped_by_topic:
    #print(topic)
    durations = list(map(lambda x: float(x['duration_secs']), group))
    #print(durations)
    
    #print ('total durations: ')
    total_duration = functools.reduce(lambda x, y: x + y, durations)
    totals[topic] = total_duration

#print(totals)

print("Running the simulator...")
total = totals['stream_all_images']
print('total time: ' + str(total) + 'secs')

print('durations as % of total streaming time: ')
for k,v in totals.items():
    if k == 'full': # exclude waiting for processing.
        continue
    print(k + ' '+ str(v / total * 100) + '%')

print()
print("Completion of all processing...")
print('total processing time: ' + str(totals['full']) + ' secs')
# Assuming single processing node
print('total processing time per image: ' + str(totals['full']/500) + ' secs')

