# Taking Up Residence Writeup 

My methodology Here is to mount the file to a H/V disk and then using R-studio to explore the restored mft sectors.
![alt text](assets/image-1.png)

Exploring the secotrs we can Obv see an existance of flag.txt  and a ransom.py
![alt text](assets/image2.png)
![alt text](assets/image3.png)
![alt text](assets/image4.png)
![alt text](assets/image5.png)

Flag is getting encrypted with Fernet method , they key is getted via Get-Content -Path and the '-stram' ntfs function
Let's Try to simulate it and retreive the key 
![alt text](assets/image6.png)

We have everything now , lets decrypt:
![alt text](assets/image7.png)