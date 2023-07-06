import sys

list = [7,"Burak",0,3,"6"]

for x in list:
    try:
        print("Number: " + str(x))
        result = 1 / int(x)
        print("Result: " + str(result))
    except ValueError:
        print(str(x) + " is not a number!")
    except ZeroDivisionError:
        print(str(x) + " number is can't be zero!")
    except:
        print(str(x) + " is doesn't calculated!")
        print("System says: " + str(sys.exc_info()[0]))
    finally:
        print("Process is over")
