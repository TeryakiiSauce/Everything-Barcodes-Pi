# Everything-Barcodes-Pi
***[ MADE FOR THE RASPBERRY PI, hence the name ]***

### Description
You can read barcodes (check "[barcodes list.docx](https://github.com/TeryakiiSauce/Everything-Barcodes-Pi/blob/master/Resources/barcodes%20list.docx)" to print the list) and related info is displayed. You can even edit, remove, insert, and view all records!

Before using the program make sure to install **PyMySQL**

`python3 -m pip install PyMySQL`

To view the lastest source code [click here](https://github.com/TeryakiiSauce/Everything-Barcodes-Pi/blob/master/Releases/Everything%20Barcodes%20Pi%20v1.2.py)

*Just to make everything clear I'm new to python :)*

# What should you do to use the program?

## PART #1 : Installing and setting up the database
1. Follow this [website](https://randomnerdtutorials.com/raspberry-pi-apache-mysql-php-lamp-server/) to install the required materials (Apache, MySQL, and PHP).
2. Once your local website is displayed, it means you've done a great job and ready to continue hehe :)
3. Create a new database with the name of your choice *(eg: my_inventory)* by clicking on **"New"**
4. Once the database is created, click on import > choose file and search for the *"[product_details.sql](https://github.com/TeryakiiSauce/Everything-Barcodes-Pi/blob/master/Resources/product_details.sql)"* file (you may need to download it; also there is a [.csv](https://github.com/TeryakiiSauce/Everything-Barcodes-Pi/blob/master/Resources/product_details.csv) version if needed) and click **"Go"**.  
**Note: in the format section, make sure SQL is selected.**

***Note: Do not edit the columns as the program might not work well. You can only edit, add, and remove rows though it could also be done using the "Everything Barcodes Pi.py" program.***

## PART #2 : Editing the code
Once everything is working fine, all you need now is to let the program to be able to connect to your database.  
To do this, search for the [*line 338*](https://github.com/TeryakiiSauce/Everything-Barcodes-Pi/blob/master/Releases/Everything%20Barcodes%20Pi%20v1.2.py#L338) (v1.2) that says:

`connection = pymysql.connect("<ip address>", "<user; usually 'root'>", "<password>", "<database>")`

### ENJOY!

![pixel art of a shop in Japan](https://github.com/TeryakiiSauce/Everything-Barcodes-Pi/blob/master/Resources/pixelart.gif)
