# concept is same as Java
# try crictical statements -- catch is here except a Exception parent Exception -- multiple Exceptions except - finally used to close the statement - finally excuted irresatptive of error or not


class Excep:

    a = 5
    b = 0
    try:
        print(a/b)
    except Exception as e:
        print("arithmetic exception", e)
    finally:
        print("work done")
    print("bye")



c = Excep()