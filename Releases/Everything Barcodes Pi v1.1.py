
#######################################################
##                                                   ##
##  Author         : Elias Rahma                     ##
##  Title          : Everything Barcodes Pi!         ##
##  Version        : 1.1                             ##
##  Description    : Scans product barcodes and      ##
##                   displays related information    ##
##  Date Created   : December 12, 2019 - 6:30 PM     ##
##  Date Updated   : December 20, 2019 - 9:55 PM     ##
##                                                   ##
##                 *****************                 ##
##                                                   ##
##  Twitter        : @TeryakiiSauce                  ##
##  Instagram      : @fckusernameslmao               ##
##                                                   ##
##                 *****************                 ##
##                                                   ##
##  Note : it may not be very efficient :(           ##
##                                                   ##
#######################################################

try :
    import pymysql
    from datetime import datetime
    import evdev
    from evdev import InputDevice, categorize, ecodes
    import os
    import re
    
except ImportError :
    print("\nmake sure you have installed these packages before running:\n\n1. pymysql : sudo apt-get install python3-pymysql or sudo pip install PyMySQL\n2. evdev   : sudo pip install evdev");
    print("\n========== see you soon hehe :) ==========");
    raise SystemExit;

##################################################
##                   CLASSES                    ##
##################################################

class record_details() :
    def __init__ (self, barcode) :
        sql_query = "SELECT * FROM `product_details` WHERE `prod_id` = %s" % barcode;
        cursor.execute(sql_query);
        results = cursor.fetchall();
        for record in results :
            prod_id = record[0];
            prod_name = record[1];
            description = record[2];
            price = record[3];
            stock = record[4];
            date = record[5];
            current_time = date.now();
            current_time = current_time.strftime("%B %d, %Y at %-I:%M:%S %p"); # eg: December 12, 2019 at 2:30:08 AM
        
        self.p_id = prod_id;
        self.prod_name = prod_name;
        self.description = description;
        self.price = round(price, 3);
        self.stock = int(stock);
        self.current_time = current_time;

##################################################
##                  FUNCTIONS                   ##
##################################################

def get_record(type) : # should get the barcode from Transmission() to continue; it also returns the barcode to whereever it's called from
    try :
        barcode_input = Transmission(type);
        
        sql_query = "SELECT * FROM `product_details` WHERE `prod_id` = %s" % barcode_input;
    
        cursor.execute( sql_query );
        results = cursor.fetchall();
    
        exists = False;
        while exists == False :
            if cursor.rowcount == 0 :
                print("Error 202 occured : product with the specified barcode ID does not exist\nPlease try again...\n");
                barcode_input = Transmission(type);
                sql_query = "SELECT * FROM `product_details` WHERE `prod_id` = %s" % barcode_input;
                cursor.execute(sql_query);
                results = cursor.fetchall();
            else :
                break;
        
        for record in results :
            prod_id = record[0];
            prod_name = record[1];
            description = record[2];
            price = record[3];
            stock = record[4];
            date = record[5];
            current_time = date.now();
            current_time = current_time.strftime("%B %d, %Y at %-I:%M:%S %p"); # eg: December 12, 2019 at 2:30:08 AM
            
        print("\n#########################################################\n\n1. Product ID        : %d\n2. Product name      : %s\n3. Description       : %s\n4. Price             : BHD %.3f\n5. Stock Remaining   : %d\n6. Date              : %s\n\n#########################################################\n" %(prod_id, prod_name, description, price, stock, current_time));
        
        return barcode_input;
        
    except Exception as e :
        print("Error 404 occured : %s\nPlease try again...\n" % e); # displays errors related to the database
        
def insert_record(type) :
    barcode_input = Transmission(type);
    
    primary_keys_query = "SELECT `prod_id` FROM `product_details`";
    cursor.execute(primary_keys_query);
    primary_keys = cursor.fetchall();
    for primary_key in primary_keys :
        if barcode_input == str(primary_key[0]) :
            print("This barcode already exists in the database!\nPlease try again...\n");
            return None;
    
    p_name_temp = input("Product name      : ");
    p_name = re.sub('\'', '\\\'', p_name_temp);
    p_desc_temp = input("Description       : ");
    p_desc = re.sub('\'', '\\\'', p_desc_temp);
    p_price = input("Price (3 dp. max) : BHD ");
    p_stock = input("Stock (quantity)  : ");
    current_time = datetime.now();
    current_time = current_time.strftime("%Y-%m-%d %H:%M:%S"); # eg: 2019-12-16 03:47:00
    
    print("\n#########################################################\n\n1. Product ID        : {0}\n2. Product name      : {1}\n3. Description       : {2}\n4. Price             : BHD {3}\n5. Stock Remaining   : {4}\n6. Date              : {5}\n\n#########################################################\n" .format(barcode_input, p_name_temp, p_desc_temp, p_price, p_stock, current_time));
    confirm("INSERT INTO `product_details` (`prod_id`, `prod_name`, `description`, `price`, `stock`, `date`) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(barcode_input, p_name, p_desc, p_price, p_stock, current_time), "insert");

def remove_record(type) :
    barcode_input = get_record(type);
    confirm("DELETE FROM `product_details` WHERE `prod_id` = %s" % barcode_input, "remove");

def file_rw (something, what) :
    reader = open("will be removed automatically dw.tmp", "r");
    string = reader.read();
    writer = open ("will be removed automatically dw.tmp", "w");
    
    if what == 'id' :
        writer.write(re.sub('^1.*:*', '1. Product ID        : */{0}/*'.format(something), string, flags = re.M));
    elif what == 'name' :
        writer.write(re.sub('^2.*:*', '2. Product name      : */{0}/*'.format(something), string, flags = re.M));
    elif what == 'desc' :
        writer.write(re.sub('^3.*:*', '3. Description       : */{0}/*'.format(something), string, flags = re.M));
    elif what == 'price' :
        writer.write(re.sub('^4.*:*', '4. Price             : */{0}/*'.format(something), string, flags = re.M));
    elif what == 'stock' :
        writer.write(re.sub('^5.*:*', '5. Stock             : */{0}/*'.format(something), string, flags = re.M));
    
    writer.close();
    reader = open("will be removed automatically dw.tmp", "r");
    print("\n#########################################################\n");
    print(reader.read());
    print("\n#########################################################\n");

def edit_record(type) :
    p_id = get_record(type);
    writer = open ("will be removed automatically dw.tmp", "w+");
    p = record_details(p_id);
    writer.write("1. Product ID        : {0}\n2. Product name      : {1}\n3. Description       : {2}\n4. Price             : BHD {3:.3f}\n5. Stock Remaining   : {4}\n6. Date              : {5}" .format (p.p_id, p.prod_name, p.description, round(p.price, 3), int(p.stock), p.current_time));
    writer.close();
    
    product_details = {
        "id": p.p_id,
        "name": p.prod_name,
        "description": p.description,
        "price": round(p.price, 3),
        "stock": int(p.stock),
        "date": p.current_time
    };
    
    isChosen = False;
    while isChosen == False :
        # 1. pid | 2. pname | 3. pdesc | 4. pprice | 5. pstock
        try :
            command = input ("Enter '\d' to confirm changes\nEnter the number of the appropriate row to edit: ");
            
            if command == '\d' :
                pid = product_details.get("id");
                pname = product_details.get("name");
                pdesc = product_details.get("description");
                pprice = product_details.get("price");
                pstock = product_details.get("stock");
                pdate = product_details.get("date");
                
                print("\n#########################################################\n\n1. Product ID        : {}\n2. Product name      : {}\n3. Description       : {}\n4. Price             : BHD {}\n5. Stock Remaining   : {}\n6. Date              : {}\n\n#########################################################\n".format(pid, pname, pdesc, pprice, pstock, pdate));
                
                confirm("UPDATE `product_details` SET `prod_id` = '{}', `prod_name` = '{}', `description` = '{}', `price` = '{}', `stock` = '{}' WHERE `product_details`.`prod_id` = {};".format(pid, pname, pdesc, pprice, pstock, p_id), 'edit');
                os.remove("will be removed automatically dw.tmp");
                break;
            
            elif command == '1' :
                exists = False;
                while exists == False :
                    pid = input ("Enter new product ID     : ");
                    does_exist = False;
                
                    if pid.isdigit() == True or "-" in pid :
                        primary_keys_query = "SELECT `prod_id` FROM `product_details`";
                        cursor.execute(primary_keys_query);
                        primary_keys = cursor.fetchall();
                        for primary_key in primary_keys :
                            if pid == str(primary_key[0]) :
                                print("This barcode already exists in the database!\nPlease try again...\n");
                                does_exist = True;
                                
                        break;
                    
                    else :
                        print("Error 101 occured : Barcodes should only contain digits and - (dashes)!\nPlease try again...\n");
                        
                if does_exist == False :
                    file_rw(pid, 'id');
                    product_details["id"] = pid;
                    
            elif command == '2' :
                pname = input ("Enter new product name     : ");
                pname = pname.strip();
                
                file_rw(pname, 'name');
                product_details["name"] = pname;
                
            elif command == '3' :
                pdesc = input ("Enter new item description : ");
                pdesc = pdesc.strip();
                
                file_rw(pdesc, 'desc');
                product_details["description"] = pdesc;
                
            elif command == '4' :
                valid = False;
                while valid == False :
                    pprice = input ("Enter new item price      : ");
                    pprice = pprice.strip();
                
                    try :
                        pprice = float(pprice);
                        pprice = round(pprice, 3);
                        valid = True;
                    
                    except ValueError :
                        print("Only numbers are allowed!\nPlease try again...\n");
                        
                file_rw(pprice, 'price');
                product_details["price"] = pprice;
                
            elif command == '5' :
                valid = False;
                while valid == False :
                    pstock = input ("Enter new item quantity   : ");
                    pstock = pstock.strip();
                    
                    try :
                        pstock = int(pstock);
                        valid = True;
                        
                    except ValueError :
                        print("Only numbers are allowed!\nPlease try again...\n");
                
                file_rw(pstock, 'stock');
                product_details["stock"] = pstock;
                
            elif command == '6' :
                print("Dates should not be changed, they are updated automatically!\n");
        
            else :
                print("Wrong entry!\n");
                
        except KeyboardInterrupt :
            print("\n========= Have a nice day hehe :) =========");
            connection.close();
            os.remove("will be removed automatically dw.tmp");
            raise SystemExit;

def Transmission(which) : # choose between 'man' (manual) or 'auto' (automatic) when entering the barcode
    try :
        if which == "man" :
            valid = False;
    
            while valid == False :
                barcodeInput = input ("Enter product ID  : ");
    
                if barcodeInput.isdigit() == True or "-" in barcodeInput :
                    return barcodeInput;
                    
                else :
                    print("Error 101 occured : Barcodes should only contain digits and - (dashes)!\nPlease try again...\n");
            
        else :
            barcodeInput = input("======= Ready to read barcodes yay! =======\n");
            return barcodeInput;

    except KeyboardInterrupt : # to force-exit program peacefully :)
        print("\n========= Have a nice day hehe :) =========");
        connection.close();
        raise SystemExit;

device = None; # default = automatically read from device
def find_device() :
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()];

    for d_temp in devices :
        #if d_temp.name == 'USB Barcode Scanner USB Barcode Scanner' : # device name
        d_temp.name = d_temp.name.lower();
        device_name = 'Barcode Scanner'; # device name
        device_name = device_name.lower();
        if device_name in d_temp.name :
            global device;
            device = d_temp;
            
    return device;

def device_found() :
    if find_device() == None :
        print("No barcode scanner was detected!\n*if a barcode is connected but not recognised, you can edit the code in line *301*. To find the device name enter '$ python3 -m evdev.evtest'. However, in order to use the command, you need to install 'evdev' from: https://python-evdev.readthedocs.io/en/latest/install.html#from-source\n");
        return False;
    
    else :
        print("Barcode scanner ready!");
        return True;

def confirm(sql_query, menu_option) : # takes sql_query as argument
    try :
        valid = False;
        while valid == False :
            if menu_option == 'insert' :
                confirmation = input ("Enter 'yes' if the above record is correct: ");
            elif menu_option == 'remove' :
                confirmation = input ("Enter 'yes' to remove the item: ");
            elif menu_option == 'edit' :
                confirmation = input ("Enter 'yes' if everything looks good: ");
        

            confirmation = confirmation.lower();
            confirmation = confirmation.strip();
            confirmation = confirmation.replace(' ', '');
    
            if confirmation == 'y' or confirmation == 'yes' or confirmation == 'ye' :        
                    cursor.execute(sql_query);
                    connection.commit(); # save changes
                    if menu_option == 'insert' :
                        print("Record has been successfully saved in the database!\n");
                    elif menu_option == 'remove' :
                        print("Record was successfully removed from the database!\n");
                    elif menu_option == 'edit' :
                        print("Record was successfully modified in the database!\n");
                    
                    valid = True;
            
            elif confirmation == 'n' or confirmation == 'no' or confirmation == 'nah' :
                print("No changes were made...\n");
                valid = True;
        
            else :
                print("Wrong entry!");
            
    except Exception as e:
        print("Error 606 occured : %s\nPlease try again...\n" % e);
            
    return;
            
##################################################
##                     MAIN                     ##
##################################################

try : 
    connection = pymysql.connect("<ip address>", "<user; usually 'root'>", "<password>", "<database>"); # open connection to MySQL [ IP ADDR | USERNAME | PASSWORD | DATABASE FILE ]
    
except Exception:
    print("Error 303 occured : please review your credintials... (ln 363)");  # displays errors related to MySQL connection
    raise SystemExit;
    
cursor = connection.cursor();

##################################################
##                   WELCOME                    ##
##################################################


isDecided = False;
while isDecided == False :
    print("\n       -  Everything Barcodes Pi  -       ");
    try :
        menu_choice = input("=============== { WELCOME } ===============\n==                                       ==\n==  1. remove items   2. view all items  ==\n==                                       ==\n==  3. insert items   4. get item info   ==\n==                                       ==\n==  5. modify items   6. buy items       ==\n==                                       ==\n==                                       ==\n==      ~ to exit enter 'CTRL+C' ~       ==\n==                                       ==\n==                           Elias Rahma ==\n================ {  END  } ================\nI would like to: ");
        menu_choice = menu_choice.strip();

        ##################################################
        ##                    CHECKS                    ##
        ##################################################
        
        # 1 : deleting items | 2 : viewing all items | 3 : inserting items | 4 : get items info | 5 : editing items | 6 : buying items
        
        if menu_choice == '1' or menu_choice == '3' or menu_choice == '4' or menu_choice == '5' : # add later : [ or menu_choice == '6' ]
            is_found = device_found();

            while is_found == True : # default : scans barcode automatically if a barcode scanner was found
                try :
                    command = input ("Enter '\m' for manual entry\nPress 'return' to continue scanning barcode automatically...\n");
        
                    if command == '\m' : # manual transmission
                        if menu_choice == '1' :
                            remove_record('man');
                        elif menu_choice == '3' :
                            insert_record('man');
                        elif menu_choice == '4' :
                            get_record('man');
                        elif menu_choice == '5' :
                            edit_record('man');
                        #elif menu_choice == '6' :
                        #    print('coming soon...');
                        #    connection.close();
                        #    raise SystemExit;
    
                    elif command == "" : # auto transmission
                        if menu_choice == '1' :
                            remove_record('auto');
                        elif menu_choice == '3' :
                            insert_record('auto');
                        elif menu_choice == '4' :
                            get_record('auto');
                        elif menu_choice == '5' :
                            edit_record('auto');
                        #elif menu_choice == '6' :
                        #    print('coming soon...');
                        #    connection.close();
                        #    raise SystemExit;
        
                    else :
                        print("Error 505 occured : the specified command does not exist...\nPlease try again...\n");
        
                except KeyboardInterrupt :
                    print("\n========= Have a nice day hehe :) =========");
                    connection.close();
                    raise SystemExit;

            while is_found == False : # escapes to manual transmission, get a barcode reader boi :')
                try :
                    if menu_choice == '1' :
                        remove_record('man');
                    elif menu_choice == '3' :
                        insert_record('man');
                    elif menu_choice == '4' :
                        get_record('man');
                    elif menu_choice == '5' :
                        edit_record('man');
                    #else :
                    #    print('coming soon...');
                    #    connection.close();
                    #    raise SystemExit;
        
                except KeyboardInterrupt :
                    print("\n========= Have a nice day hehe :) =========");
                    connection.close();
                    raise SystemExit;
                
            break;
            
        elif menu_choice == '2' :
            sql_query = "SELECT * FROM `product_details` ORDER BY `date` ASC";
    
            try :
                cursor.execute( sql_query );
                results = cursor.fetchall();
        
                for record in results :
                    prod_id = record[0];
                    prod_name = record[1];
                    description = record[2];
                    price = record[3];
                    stock = record[4];
                    date = record[5];
                    current_time = date.today();
                    current_time = current_time.strftime("%B %d, %Y at %-I:%M:%S %p"); # eg: December 12, 2019 at 2:30:08 AM
            
                    print("\n#########################################################\n1. Product ID        : %d\n2. Product name      : %s\n#########################################################\n" %(prod_id, prod_name));
                    
                print("Total items: %s\nSorted by: earliest first, latest last" % cursor.rowcount);
        
            except Exception as e :
                print("Error 404 occured :",e); # displays errors related to the database
                
            break;
        
        elif menu_choice == '6' :
            print('coming soon hehe :)');
        
        else :
            print("Wrong entry!");
    
    except KeyboardInterrupt :
        print("\n========= Have a nice day hehe :) =========");
        connection.close();
        raise SystemExit;
    
connection.close();
raise SystemExit;
