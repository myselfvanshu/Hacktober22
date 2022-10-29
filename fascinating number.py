# Python 3 program to implement
# fascinating number
 
# function to check if number
# is fascinating or not
def isFascinating(num) :
 
    # frequency count array
    # using 1 indexing
    freq = [0] * 10
 
    # obtaining the resultant number
    # using string concatenation
    val = (str(num) + str(num * 2) +
                      str(num * 3))
 
    # Traversing the string
    # character by character
    for i in range(len(val)) :
 
        # gives integer value of
        # a character digit
        digit = int(val[i])
 
        # To check if any digit has
        # appeared multiple times
        if freq[digit] and digit != 0 > 0 :
            return False
        else :
            freq[digit] += 1
 
    # Traversing through freq array to
    # check if any digit was missing
    for i in range(1, 10) :
 
        if freq[i] == 0 :
            return False
 
    return True
 
# Driver Code
if __name__ == "__main__" :
 
    # Input number
    num = 192
 
    # Not a valid number
    if num < 100 :
        print("No")
 
    else :
         
        # Calling the function to
        # check if input number
        # is fascinating or not
        ans = isFascinating(num)
         
        if ans :
            print("Yes")
        else :
            print("No")
