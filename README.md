# Everything-Barcodes-Pi
***[ MADE FOR THE RASPBERRY PI, hence the name ]***    
**Note: check steps below for Windows support**

### Description
You can read barcodes (check "[barcodes list.docx](https://github.com/TeryakiiSauce/Everything-Barcodes-Pi/blob/master/Resources/barcodes%20list.docx)" to print the list) and related info is displayed. You can even edit, remove, insert, and view all records!

Before using the program make sure to install **Python** and **PyMySQL**

Python : `sudo apt-get update && sudo apt-get install python3.6`    
PyMySQL : `python3 -m pip install PyMySQL`

>To view the lastest source code [click here](https://github.com/TeryakiiSauce/Everything-Barcodes-Pi/blob/master/Releases/Everything%20Barcodes%20Pi%20v1.3.py)  
>To watch a YouTube demo video of the program [click here](https://youtu.be/Mpy9pa-zqYE)

*Just to make everything clear I'm new to python :)*

# What should you do to use the program? (Windows)

## PART #1 : Installation of Linux OS in Windows
You could either use a **Virtual Machine** to install a Linux distro *(Eg: Ubuntu)* or install *Ubuntu* from the **Microsoft Store** *(quicker to setup but GUI is not avaiable)*

### Recommendations :
- Install using **Virtual Machince** if you :
  1. Want a GUI
  2. Don't mind waiting for the installation & booting process
  3. Want to spend much time to edit the source code and debugging
  4. Have enough memory on your PC (SSD, HDD, RAM, etc)
  5. Your PC meets the minimum requirements to run the OS *(there's a lite version of Ubuntu for low-powered PCs called "Lubuntu")*
  
- Install *Ubuntu* from **Microsoft Store** if you :
  1. Want to run the program without extensive editing of the source code or debugging
  2. Familiar with the CLI
  3. Want a faster method
  
***Make sure to watch YouTube videos or visit other websites to install using a Virtual Machine***

## PART #2 : Moving ahead...
*Continue with the steps below once you have the Linux OS running without problems*

# What should you do to use the program? (Linux)

## PART #1 : Installing and setting up the database (locally)
1. Follow this [website](https://randomnerdtutorials.com/raspberry-pi-apache-mysql-php-lamp-server/) to install the required resources (Apache, MySQL, PHP, and PHPMyAdmin).
2. Once you are able to view your local website and phpmyadmin, it means you've done a great job and ready to continue hehe :)    
**By the way, your website can be viewed from any device connected to the same network*
3. Create a new database with the name of your choice *(eg: my_inventory)* by clicking on *New*
4. Once the database is created, click on *import (ignore all errors)* > *choose file* and search for the *"[product_details.sql](https://github.com/TeryakiiSauce/Everything-Barcodes-Pi/blob/master/Resources/product_details.sql)"* file (you may need to download it; also there is a [.csv](https://github.com/TeryakiiSauce/Everything-Barcodes-Pi/blob/master/Resources/product_details.csv) version if needed) and click **"Go"**.  
**Note: in the format section, make sure that the appropriate format is selected (eg: SQL for .sql files).**

***Note: Do not edit the columns as the program might not work well. You can only edit, add, and remove rows though it could also be done using the "Everything Barcodes Pi" program.***

## PART #2 : Editing the code
Once everything is working fine, all you need now is to let the program to be able to connect to your database.  
To do this, search for the [*line 355*](https://github.com/TeryakiiSauce/Everything-Barcodes-Pi/blob/master/Releases/Everything%20Barcodes%20Pi%20v1.3.py#L355) (v1.3) that says:

`connection = pymysql.connect("<ip address>", "<user; usually 'root'>", "<password>", "<database>")`

All you have to do now is to replace each segment with the appropriate values (keep the quotation marks)
> **IP Address :** *localhost* | To find the IP Address of your Raspberry Pi enter `hostname -I`  
> **User :** It is *root* by default  
> **Password :** The password of the user mentioned  
> **Database :** The database's name

## PART #3 : Executing the program
Once the zip file of the desired version is downloaded, all you have to do now is to extract it using the command

`tar xzf "Everything.Barcodes.Pi.vx.x.zip")"`

Then `cd` into that directory and enter the following command

### Example
`python3 Everything Barcodes Pi vx.x.py`  
or  
`python3 <path>/Everything Barcodes Pi vx.x.py`

### ENJOY!

![pixel art of a shop in Japan](https://github.com/TeryakiiSauce/Everything-Barcodes-Pi/blob/master/Resources/pixelart.gif)
