
#######################################################
##                                                   ##
##  Author         : Elias Rahma                     ##
##  Title          : Barcode Scanner                 ##
##  Version        : 1.0                             ##
##  Description    : Scans product barcodes and      ##
##                   displays related information    ##
##  Date Created   : December 12, 2019 - 6:30 PM     ##
##  Date Updated   : December 15, 2019 - 9:35 PM     ##
##                                                   ##
##                 *****************                 ##
##                                                   ##
##  Twitter        : @TeryakiiSauce                  ##
##  Instagram      : @fckusernameslmao               ##
##                                                   ##
#######################################################

try :
    import pymysql
    from datetime import datetime
    import evdev
    from evdev import InputDevice, categorize, ecodes
    
except ImportError :
    print("\nmake sure to install these packages before running:\n\n1. pymysql : sudo apt-get install python3-pymysql or sudo pip install PyMySQL\n2. evdev   : sudo pip install evdev");
    print("\n========== see you soon hehe :) ==========");
    raise SystemExit;

##################################################
##                  FUNCTIONS                   ##
##################################################

def get_record(type) : # should get the barcode from Transmission() to continue
    barcode_input = Transmission(type);

    sql_query = "SELECT * FROM `product_details` WHERE `prod_id` = %s" % barcode_input;
    
    try :
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
            current_time = date.today();
            current_time = current_time.strftime("%B %d, %Y at %-I:%M:%S %p"); # eg: December 12, 2019 at 2:30:08 AM
            
        print("\n#####################################################\n\nProduct ID        : %d\nProduct name      : %s\nDescription       : %s\nPrice             : BHD %.3f\nStock Remaining   : %d\nDate              : %s\n\n#####################################################\n" %(prod_id, prod_name, description, price, stock, current_time));
        
    except Exception as e :
        print("Error 404 occured : %s\nPlease try again...\n" % e); # displays errors related to the database

def Transmission(which) : # choose between 'man' (manual) or 'auto' (automatic) when entering the barcode
    try :
        if which == "man" :
            valid = False;
    
            while valid == False :
                barcodeInput = input ("Enter product ID  : ")
    
                if barcodeInput.isdigit() == True or "-" in barcodeInput :
                    return barcodeInput;
                    
                else :
                    print("Error 101 occured : Barcodes should only contain digits and - (dashes)!\nPlease try again...\n");
            
        else :
            code = input("======= Ready to read barcodes yay! =======\n");
            return code;

    except KeyboardInterrupt : # to force-exit program peacefully :)
        print("\n========= Have a nice day hehe :) =========");
        connection.close();
        raise SystemExit;

device = None; # default = automatically read from device
def find_device() :
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()];

    for d_temp in devices :
        if d_temp.name == 'USB Barcode Scanner USB Barcode Scanner' : # device name
            global device;
            device = d_temp;
            
    return device;

def device_found() :
    if find_device() == None :
        print("No barcode scanner was detected!\n\n*if a barcode is connected but not recognised, please edit the code in line *94*. To find the device name enter '$ python3 -m evdev.evtest'. However, in order to use the command, you need to install 'evdev' from: https://python-evdev.readthedocs.io/en/latest/install.html#from-source\n");
        return False;
    
    else :
        print("Barcode scanner ready!");
        return True;
            
##################################################
##                     MAIN                     ##
##################################################

try : 
    connection = pymysql.connect("<ip address>", "<user; usually 'root'>", "<password>", "<database>"); # open connection to MySQL [ IP ADDR | USERNAME | PASSWORD | DATABASE FILE ]
    #print("Connection successful!");
    
except Exception:
    print("Error 303 occured : please review your credintials... (ln 117)");  # displays errors related to MySQL connection
    raise SystemExit;
    
cursor = connection.cursor();

##################################################
##                    CHECKS                    ##
##################################################

is_found = device_found();

while is_found == True : # scans barcode automatically if a barcode scanner was found
    try :
        command = input ("Enter '\m' for manual entry or 'CTRL+C' to exit\nPress 'return' to continue scanning automatically...\n");
        
        if command == '\m' :
            get_record('man');
            #break; # to run the code once only
    
        elif command == "" :
            get_record('auto');
            #break; # to run the code once only
        
        else :
            
            print("Error 505 occured : the specified command does not exist...\nPlease try again...\n");
        
    except KeyboardInterrupt :
        print("\n========= Have a nice day hehe :) =========");
        connection.close();
        raise SystemExit;

while is_found == False : # escapes to a manual transmission engine haha (jk manual entry) :')
    try :
        get_record('man');
        
    except KeyboardInterrupt :
        print("\n========= Have a nice day hehe :) =========");
        connection.close();
        raise SystemExit;
    
connection.close();
raise SystemExit;
