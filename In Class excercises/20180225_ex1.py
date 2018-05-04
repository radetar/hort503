#put imports up here
#Make function to request string of numbers, return as list of floats
def request_numbers():
  list = input("Put in a list of 10 values seperated by commas ")
  list_sep = list.split(",")
  print(list_sep)
  float_list_sep = []
  if len(list_sep) == 10:
      for i in list_sep:
          float_list_sep.append(float(i))
      return(float_list_sep)
  else:
        print("ONLY TEN ITEMS PLEASE")



#take an average of all floats in a string
def make_average(float_list):
    total = sum(float_list)
    average = total/len(float_list)
    return(average)

def main():
    float_list = request_numbers()
    average = make_average(float_list)
    print("The the average of your numbers is {}".format(average))

main()
