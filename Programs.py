class Program():

    def Subfields(self):
        # Create a function, and list out the items in the list 
        AIDomains = ["Machine Learning", "Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
    
        print("Sub-fields in AI are:")
        for eachdomain in AIDomains:
            print(eachdomain)
    
    # Create a function that checks whether the given number is Odd or Even()
    def OddEven(self):
        number= int(input("Enter a number:"))
        if(number%2==0):
            print(f"{number} is Even number")
        else:
            print(f"{number} is Odd number")

    # Create a function that tells elegibility of marriage for male and female according to their 
    #age limit like 21 for male and 18 for female 
    def Eligible(self):
        gender = input("Your Gender:") 
        age = int(input("Your Age:"))
        if (gender == "Male"):
            if age>=21:
                print( "ELIGIBLE")
            else:
                print( "NOT ELIGIBLE")
        elif (gender == "Female"):
            if age>=18:
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        
    #calculate the percentage of your 10th mark 
    def percentage(self):
        total = 0
        for i in range(5):
            marks = int(input(f"Subject{i+1}="))
            total = total + marks
        percent = total / 5
        print("Total :", total)
        print("Percentage : ",percent)
    
    
    #print area and perimeter of triangle using and functions
    def triangle(self):
        height=int(input("Height:"))
        breadth = int(input("Breadth:"))
        area = (height * breadth) / 2
        print("Area formula: (Height*Breadth)/2 ")
        print("Area of Triangle:", area)
        height1 = int(input("Height1:"))
        height2 = int(input("Height2:"))
        breadth = int(input("Breadth:"))
        perimeter = height1 + height2 + breadth
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:",perimeter)
