#recursive function to print the even numbers by taking input range
def function():
    global i 
    if i<=10:
        if i%2==0:
            print(i)
        i=i+1
        function()
i=1
function()