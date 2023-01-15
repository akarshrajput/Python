#recursive function
def fun():
    global i
    if i<5:
        print("Hi")
        i=i+1
        fun()
i=0
fun()