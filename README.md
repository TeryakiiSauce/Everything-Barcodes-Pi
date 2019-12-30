# Everything-Barcodes-Pi
***[ MADE FOR THE RASPBERRY PI, hence the name ]***

### Description
You can read barcodes (few only; check "barcodes list.docx" to print the list) and related info is displayed. You can even edit, remove, insert, and view all records!

Before using the porgram make sure to install [PyMySQL](https://www.youtube.com/watch?v=Hja8XzTgJHI) (Windows)

To view the lastest source code [click here](https://github.com/TeryakiiSauce/Everything-Barcodes-Pi/blob/master/Releases/Everything%20Barcodes%20Pi%20v1.2.py)

*Just to make everything clear I'm new to python :)*

# What should you do to use the program?

## PART #1 : Installing and setting up the database
1. Install mysql *(easy)* : [ windows: https://dev.mysql.com/downloads/installer/ ] Also watch [this video](https://www.youtube.com/watch?v=2WyFx9Zt7YU) for more info.
2. Install xampp *(easy)* : [ https://www.apachefriends.org/index.html ] Info : install xampp into C:\xampp (default) > open it > start Apache and MySQL. *To check if the site works or not type your ip address in the browser*.
3. Once the website is displayed, it means you've done a great job hehe :) anyway, click **phpMyAdmin**.
4. Create a new database with the name of your choice *(eg: my_inventory)* by clicking on **"New"**
5. Once the database is created, click on import > choose file and search for the *"product_details.sql"* file and click **"Go"**.  
**Note: in the format section, make sure SQL is selected.**

***Note: Do not edit the columns as the program might not work well. You can only edit, add, and remove rows though it could also be done using the "Everything Barcodes Pi.py" program.***

## PART #2 : Editing the code
Once everything is working fine, all you need now is to let the program to be able to connect to your database.  
To do this, search for the [line *338*](https://github.com/TeryakiiSauce/Everything-Barcodes-Pi/blob/master/Releases/Everything%20Barcodes%20Pi%20v1.2.py#L338) (v1.2) that says:

`connection = pymysql.connect("<ip address>", "<user; usually 'root'>", "<password>", "<database>")`

### ENJOY!
