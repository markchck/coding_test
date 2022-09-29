def get_count(x,number):
     count = 0

     if number < 10:
         change_number = number * 10 + number
     else:
         change_number = (number // 10) + (number % 10)
         change_number = (number % 10) * 10 + (change_number % 10)
     count += 1

     if x == change_number:
         return count

     return count + get_count(x,change_number)


number = int(input())
x = number

print(get_count(x,number))