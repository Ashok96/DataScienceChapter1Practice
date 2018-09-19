'''Chapter 1 Data Science
list of user , each represented by dict that contains for each user his or her id(which is a number) and name (which  rhymes with the usr's id)'''

users = [ {"id":0 , "name": "Hero"},
           {"id":1 , "name": "Dunn"},
           {"id":2 , "name": "Sue"},
           {"id":3 , "name": "Chi"},
           {"id":4 , "name": "Thor"},
           {"id":5 , "name": "Clive"},
           {"id":6 , "name": "Hicks"},
           {"id":7 , "name": "Devin"},
           {"id":8 , "name": "Kate"},
           {"id":9 , "name": "Klein"} ]
friendships =[(0,1), (0,2), (1,2), (1,3), (2,3), (3,4),(4,5),(5,6),(6,7),(7,8),(8,9)]
'''add a list of friends to each user . set each user's friends property to an empty list'''
for user in users:
  print("Hello WORLD")
  print(user)
  user['friends']=[]

#populate the list using the friendships data

for i, j in friendships:
  users[i]["friends"].append(users[j])#add i as a friend of j
  users[j]["friends"].append(users[i])#add j as a friend of i

  '''Now we can easily find the average number of connections, first let us find the total connections'''
  print(user)

def number_of_friends(user):
  '''how many friends does user have'''

  return len(user["friends"]) #length of friends_ids list
total_connections = sum(number_of_friends(user) for user in users)
print ("%s" %total_connections + " is the total connections") #22

#Now we divide by number of users

num_users = len(users)
avg_connections = total_connections /num_users
print("%s " % avg_connections + "is the avg connection")

'''Now to find most connected people, they are the one wwith largest number of friends
First sort all of them from "most friends" to least friends by creating a list where we have ids and number of friends with that respective user id '''

def takesecond(elem):
  return elem[1]
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
sorted(num_friends_by_id, key=takesecond,reverse=True)
print ("Each pair is (user_id, num_friends) %s" %num_friends_by_id)

''' A user might know the friends of friends. for each of a user's friends, iterate over that person's friends and collect all the results'''

def friends_of_friends_ids_bad(user):
  #"foaf" is short for "friend of a friend"
  return [foaf["id"] for friend in user["friends"] for foaf in friend["friends"]] #got complex

print("hello")
print(friends_of_friends_ids_bad(users[9]))
print([friend["id"] for friend in users[0]["friends"]])

'''produce a count of mutual friends and exclude people already known to the user'''

from collections import Counter
def not_the_same(user, other_user):
  """two users are no the same if they have different ids"""
  return user["id"] !=other_user["id"]

def not_friends(user, other_user):
  """Other _user is not a friend if he's not in user["friends"]"""
  return all(not_the_same(friend, other_user) for friend in user["friends"])

def friends_of_friend_ids(user):
  return Counter(foaf["id"] 
  for friend in user["friends"] 
  for foaf in friend["friends"] 
  if not_the_same(user, foaf)
  and not_friends(user, foaf)) 
print (friends_of_friend_ids(users[3]) )

interests = [
(0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
(0, "Spark"), (0, "Storm"), (0, "Cassandra"),
(1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
(1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
(2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
(3, "statistics"), (3, "regression"), (3, "probability"),
(4, "machine learning"), (4, "regression"), (4, "decision trees"),
(4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
(5, "Haskell"), (5, "programming languages"), (6, "statistics"),
(6, "probability"), (6, "mathematics"), (6, "theory"),
(7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
(7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
(8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
(9, "Java"), (9, "MapReduce"), (9, "Big Data")
]
