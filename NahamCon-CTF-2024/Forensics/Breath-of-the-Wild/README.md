## Breath of The Wild Writeup
First Analysis on the file shows that its a vhdx file (virtual Hard disk)
![alt text](assets/image2.png)

We probably need to resotre some regions of this disk.
![alt text](assets/image.png)

Simply what i did is to change the file to .vhdx entension and mount it using windows prebuilt function:
![alt text](assets/image3.png)

Taking a glance at the mounted disk dosent seem to have much other than random pics.

For This kind of task i usually use R-studio to try to recover some parts of the disk.
![alt text](assets/image4.png)

Lets Restore all and see what is gives.
![alt text](assets/image5.png)
![alt text](assets/image6.png)

A weird Html Chars appeared in the strings , let's decode and see :
![alt text](assets/image7.png)

Well it's the flag :smile: