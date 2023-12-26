def ask_for_init():
    try:
        result=int(input("please enter number: "))
    except: 
        print("whoops!  that's not the number")
    finally:
        print("end of try/except/finally")

  ask_for_init()

//added this line to check modified file
