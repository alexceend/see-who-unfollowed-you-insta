import json

# get information from followers file
with open('followers.json') as f:  
    follower = json.load(f) 

# get information from following file
with open('following.json') as g:  
    following = json.load(g) 

followers_list = []
following_list = []
following_list_url = []

for i in follower['relationships_followers']:
  followers_list.append(i['string_list_data'][0]['value'])

for i in following['relationships_following']:
  following_list.append(i['string_list_data'][0]['value'])
  following_list_url.append(i['string_list_data'][0]['href'])
  

followers_list.sort()
following_list.sort()
following_list_url.sort()

print("Seguidores: " + str(len(followers_list)))
print("Siguiendo: " + str(len(following_list)))

dont_follow_back = []
dont_follow_back_url = []

print("\nUsuarios que no te siguen de vuelta: ")

for _ in range(len(following_list)):
    if following_list[_] not in followers_list:
        dont_follow_back.append(following_list[_])
        dont_follow_back_url.append(following_list_url[_])

for _ in range(len(dont_follow_back)):
  print(dont_follow_back[_], " | ", dont_follow_back_url[_])
try:
  os.remove("list.txt")
except:
  "No existe list.txt, se creará"
  
with open("list.txt", 'x') as l:
    
  l.write("USUARIOS QUE NO TE SIGUEN DE VUELTA:\n")
  i = 0
  for _ in range(len(dont_follow_back)):
    l.write(dont_follow_back[_] + " | " + dont_follow_back_url[_])
    l.write("\n")
    i+=1
  l.write("Número total de usuarios que no te siguen de vuelta: " + str(i))
    
l.close()

exit()