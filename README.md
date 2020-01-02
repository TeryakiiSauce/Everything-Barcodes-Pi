# Everything-Barcodes-Pi
***[ MADE FOR THE RASPBERRY PI, hence the name ]***

### Description
You can read barcodes (check "[barcodes list.docx](https://github.com/TeryakiiSauce/Everything-Barcodes-Pi/blob/master/Resources/barcodes%20list.docx)" to print the list) and related info is displayed. You can even edit, remove, insert, and view all records!

Before using the program make sure to install **PyMySQL**

`python3 -m pip install PyMySQL`

To view the lastest source code [click here](https://github.com/TeryakiiSauce/Everything-Barcodes-Pi/blob/master/Releases/Everything%20Barcodes%20Pi%20v1.2.py)

*Just to make everything clear I'm new to python :)*

# What should you do to use the program?

## PART #1 : Installing and setting up the database (local)
1. Follow this [website](https://randomnerdtutorials.com/raspberry-pi-apache-mysql-php-lamp-server/) to install the required resources (Apache, MySQL, and PHP).
2. Once you are able to view your local website, it means you've done a great job and ready to continue hehe :)
3. Create a new database with the name of your choice *(eg: my_inventory)* by clicking on *New*
4. Once the database is created, click on *import* > *choose file* and search for the *"[product_details.sql](https://github.com/TeryakiiSauce/Everything-Barcodes-Pi/blob/master/Resources/product_details.sql)"* file (you may need to download it; also there is a [.csv](https://github.com/TeryakiiSauce/Everything-Barcodes-Pi/blob/master/Resources/product_details.csv) version if needed) and click **"Go"**.  
**Note: in the format section, make sure that the appropriate format is selected (eg: SQL for .sql).**

***Note: Do not edit the columns as the program might not work well. You can only edit, add, and remove rows though it could also be done using the "Everything Barcodes Pi.py" program.***

## PART #2 : Editing the code
Once everything is working fine, all you need now is to let the program to be able to connect to your database.  
To do this, search for the [*line 338*](https://github.com/TeryakiiSauce/Everything-Barcodes-Pi/blob/f298b3a7f5527184b4fb551ac826bc0f94ad1443/Releases/Everything%20Barcodes%20Pi%20v1.2.py#L339) (v1.2) that says:

`connection = pymysql.connect("<ip address>", "<user; usually 'root'>", "<password>", "<database>")`

## PART #3 : Executing the program
All you have to do is search for the version you'd like to use in the '*Releases*' folder and then `cd` into that directory and enter the following command

### Example
`python3 Everything Barcodes Pi v1.2.py`  
or  
`python3 <path>/Everything Barcodes Pi v1.2.py`

### ENJOY!

![pixel art of a shop in Japan](https://github.com/TeryakiiSauce/Everything-Barcodes-Pi/blob/master/Resources/pixelart.gif)
