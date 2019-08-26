def find_outlier(integers):
   if integers[0] % 2 == 0 and integers[1] % 2 == 0:
       for i in integers:
           if i % 2 != 0:
               return i
   elif integers[0] % 2 != 0 and integers[1] % 2 != 0:
        for i in integers:
            if i % 2 == 0:
                return i
   elif integers[0] % 2 == 0 and integers[1] % 2 != 0:
       if integers[2] % 2 == 0:
           return integers[1]
       else:
           return integers[0]
   elif integers[0] % 2 != 0 and integers[1] % 2 == 0:
       if integers[2] % 2 == 0:
           return integers[0]
       elif integers[2] % 2 != 0:
           return integers[1]