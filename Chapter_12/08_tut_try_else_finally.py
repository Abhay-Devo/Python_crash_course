# Here we will see how to use try, & except with else and finally...

# Try with else:
try: 
    num = int(input("Enter a number:"))

except Exception as e:
    print(e) 
     
else: 
    print('we are inside else conditionals...')         
    # This is executed only if the try was successful, exception occur this will not run...


# Try with finally
# In normal uses finally work normally like in tut_07 even if exception is raised,
# but difference come in function, even if you say return to try & except it will still run finally:

def main():
    try:
        num = int(input("Enter a number..."))
        print(num)
        return
    
    except Exception as e:
        print("Please enter a valid synatx!!!")
        return
    
    finally:
        print("Now, we are in finally funtion!!!")
    # finally will run eventhough there are return in both(try, except), that's why we use finally in func

main()