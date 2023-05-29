import tkinter

window = tkinter.Tk()
window.title("BMI QUIZ")
window.minsize(width=100,height=100)

def BMI():
    H = HInput.get()
    W = WInput.get()
    if W == "" or H == "":
        Result.config(text="Fill in the blanks !!")
    else:
        try:
            bmi = float(W) / ((float(H)/100)**2)
            MyResult = CalculateResult(bmi)
            Result.config(text=MyResult)


        except:
            Result.config("Enter a valid value !!")








weight = tkinter.Label(text="Enter Your Weight")
weight = tkinter.Label(text="Enter Your Weight (kg)")
weight.pack()
WInput = tkinter.Entry(width=6)
WInput.pack()
height = tkinter.Label(text="Enter Your Height (cm)")
height.pack()
HInput = tkinter.Entry(width=6)
HInput.pack()
MyButton = tkinter.Button(text="Calculate",command=BMI)
MyButton.pack()
Result = tkinter.Label()
Result.pack()

def CalculateResult(bmi):
    MyResult = f"BMI is {round(bmi,2)}. Body Class "
    if bmi <=16:
        MyResult += "severly thin"
    elif 16< bmi <=17:
        MyResult += "moderately thin"
    elif 17< bmi <= 18.75:
        MyResult += "mild thin"
    elif 18.75< bmi<=24:
        MyResult += "normal weight"
    elif 24 < bmi <= 30:
        MyResult += "overweight"
    elif 30< bmi <=36:
        MyResult += "obese class one"
    elif 36< bmi <=40:
        MyResult += "obese class two"
    else:
        MyResult += "obese class three"
    return MyResult
window.mainloop()








