

#def my_func():
    #Does something:
    # if base_case:
    #   end function
    #else (recursive case):
    #   my_func()


# while condition:
    #do something


# 3 * 2 * 1

# def factorial(num):
#     if num == 1: #base case and start returning
#         print(f"factorial({num}) = 1 BASECASE")
#         return 1 
        
#     else:
#         print(f"factorial({num}) = {num} * factorial({num-1})")
#         result = factorial(num - 1)
#     return num * result

# print(factorial(5))


#We have multiple companies represented as lists, each company has systems that
#need to checked, if the systems of each company are okay, return "Okay", if not
# return "Not Okay"

#[[T,T,T], [T,F,T], [T,T,T]]

def reco_check(companies):
    if not companies: #Base Case
        return "Okay"
    
    checking_company = companies.pop()
    for system in checking_company:
        if system == "F":
            return "Not Okay"
    
    status = reco_check(companies)
    return status

print(reco_check([["T","T","T"], ["T","T","T"], ["T","T","T"]]))


