import json
import os

with open('followers.json') as f:  
    followers = json.load(f) 

with open('following.json') as g:  
    following = json.load(g) 

followers_list = []
following_list = []

for i in followers['relationships_followers']:
  followers_list.append(i['string_list_data'][0]['value'])

for i in following['relationships_following']:
  following_list.append(i['string_list_data'][0]['value'])

followers_list.sort()
following_list.sort()


print("Seguidores: " + str(len(followers_list)))
print("Siguiendo: " + str(len(following_list)))

print("\nUsuarios que no te siguen de vuelta: ")

dont_follow_back = []

for _ in range(len(following_list)):
    if following_list[_] not in followers_list:
        dont_follow_back.append(following_list[_])

for _ in range(len(dont_follow_back)):
  print(dont_follow_back[_])
  
try:
  os.remove("list.txt")
except:
  "No existe list.txt, se creará"
  
with open("list.txt", 'x') as l:
    
  l.write("USUARIOS QUE NO TE SIGUEN DE VUELTA:\n")
  i = 0
  for _ in range(len(dont_follow_back)):
    l.write(dont_follow_back[_])
    l.write("\n")
    i+=1
  l.write("Número total de usuarios que no te siguen de vuelta: " + str(i))
    
l.close()

exit()