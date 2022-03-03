def day(i):
    switcher={
                0:"Mondey",
                1:"Tuesday",
                2:"Wednesday",
                3:"Thursday",
                4:"Friday",
                5:"Saturday",
                6:"Sunday"
             }
    return switcher.get(i,"Invalid number ")         
if __name__ == "_main_":
    Day = int(input("Enter the number to get day at that number : "))
    print(day(Day))