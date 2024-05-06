# See who unfollowed you on insta
A python script to see the people who don't follow you back

> [!NOTE]
> You have to get your account info via meta
> Need to have python installed in your computer

> [!TIP]
> If you dont have python you can download it from here: https://www.python.org/downloads/

Once python is installed you have to request your instagram account data via Meta:

(Accounts center -> Information and permissions -> Download your information -> Download or transfer information -> Part of your information )

![image](https://github.com/alexceend/see-who-unfollowed-you-insta/assets/136982252/fbe9f700-6125-4653-806e-be1d013bd568)
![image](https://github.com/alexceend/see-who-unfollowed-you-insta/assets/136982252/f1bbc858-dca2-4e51-ab14-46af095f8730)
![image](https://github.com/alexceend/see-who-unfollowed-you-insta/assets/136982252/a11dab96-c4e8-4e89-a58f-69c6b2429a75)
![image](https://github.com/alexceend/see-who-unfollowed-you-insta/assets/136982252/81026841-d8df-46eb-ad1f-96575d2c78b0)
![image](https://github.com/alexceend/see-who-unfollowed-you-insta/assets/136982252/7dc04728-e9ad-43f9-936c-4a0531db2448)

> [!NOTE]
> You will need to check only the followers and follows option
> 
![image](https://github.com/alexceend/see-who-unfollowed-you-insta/assets/136982252/c7a33e6d-90f8-4805-915b-940fcad80e2a)

> [!WARNING]
> Date interval must be from the beggining and the format must be JSON

![image](https://github.com/alexceend/see-who-unfollowed-you-insta/assets/136982252/b9a47093-4bb7-4840-85f7-6db7730af4d7)

After some minutes you will get an email with a download link. Download it and extract the .zip file 
Inside the connections/followers_and_followers folder there will be two files we'll need for the process: followers.json and following.json

> [!WARNING]
> In case followers.json is named followers_1.json you MUST name it followers.json

> [!WARNING]
> followers.json archive is not well formated so we must do some changes.
> 
> 1st Open the followers.json file
> 
> 2nd At the top of the file we MUST add the following text:
> 
> {
> 
> "relationships_followers":
> 
> 3rd At the end of the file we MUST add this: }

Then download the python script of this repository (unfollowers.py) and move it to the followers_and_following folder (The same directory as following.json and followers.json)

```bash
git clone https://github.com/alexceend/see-who-unfollowed-you-insta.git
```

Finally open a command prompt in the folder and execute the following command:
```bash
python unfollowers.py
```
A file named list.txt will be created containing the users who dont follow you back on insta
