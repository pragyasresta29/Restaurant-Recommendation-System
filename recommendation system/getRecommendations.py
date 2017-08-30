
# coding: utf-8

# In[1]:

import pickle


# In[2]:

def load_obj(name ):
    with open( name + '.pkl', 'rb') as f:
        return pickle.load(f)


# In[3]:

reviews = load_obj('reviews')


# In[4]:

restaurants = load_obj('restaurants')


# In[10]:

def loadDataset(reviews, restaurants):
    restaurant={}
    for data in restaurants:
        res_id=data['business_id']
        name=data['name']
        restaurant[res_id]=name
    prefs={}
    count=0
    for data in reviews:
        user_id=data['user_id']
        res_id=data['restaurant_id']
        rating=data['rating']
        prefs.setdefault(user_id,{})
        prefs[user_id][restaurant[res_id]]=float(rating)
    return prefs 


# In[11]:

from math import sqrt
# Returns the Pearson correlation coefficient for p1 and p2
def sim_pearson(prefs,p1,p2):
  # Get the list of mutually rated items
  si={}
  for item in prefs[p1]:
    if item in prefs[p2]: si[item]=1
  # Find the number of elements
  n=len(si)
  # if they are no ratings in common, return 0
  if n==0: return 0
  # Add up all the preferences
  sum1=sum([prefs[p1][it] for it in si])
  sum2=sum([prefs[p2][it] for it in si])
  # Sum up the squares
  sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
  sum2Sq=sum([pow(prefs[p2][it],2) for it in si])
  # Sum up the products
  pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])
  # Calculate Pearson score
  num=pSum-(sum1*sum2/n)
  den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
  if den==0: return 0
  r=num/den
  return r


# In[12]:

# Gets recommendations for a person by using a weighted average
# of every other user's rankings
def getRecommendations(prefs,person,similarity=sim_pearson):
  totals={}
  simSums={}
  for other in prefs:
    # don't compare me to myself
    if other==person: continue
    sim=similarity(prefs,person,other)
    # ignore scores of zero or lower
    if sim<=0: continue
    for item in prefs[other]:
      # only score movies I haven't seen yet
      if item not in prefs[person] or prefs[person][item]==0:
        # Similarity * Score
        totals.setdefault(item,0)
        totals[item]+=prefs[other][item]*sim
        # Sum of similarities
        simSums.setdefault(item,0)
        simSums[item]+=sim
  # Create the normalized list
  rankings=[(total/simSums[item],item) for item,total in totals.items( )]
  # Return the sorted list
  rankings.sort( )
  rankings.reverse( )
  return rankings


# In[16]:

prefs=loadDataset(reviews,restaurants)


# In[17]:

rec=getRecommendations(prefs, 'rLtl8ZkDX5vH5nAx9C3q5Q')


# In[19]:

rec[:15]


# In[20]:

len(rec)


# In[ ]:




# In[17]:

recommendations={}
data=[]
for i in rec:
    list={}
    list['sim_score']=i[0]
    list['id']=i[1]
    data.append(list)
recommendations['recommendations']=data


# In[18]:

recommendations['recommendations'][0]


# In[19]:

import json


# In[21]:

with open('userrec.json', 'w') as userrec:
   json.dump(recommendations,userrec)


# In[39]:

newrec=''


# In[40]:

jsonrec= open('userrec.json')


# In[41]:

for line in jsonrec:
    newrec= line


# In[42]:

testrec=json.loads(newrec)


# In[44]:

testrec[:15]




