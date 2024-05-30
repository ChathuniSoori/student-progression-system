from graphics import *
terminate=False

#list count
progress_list = []
trailer_list = []
retriever_list = []
exclude_list = []

#except the out of range and wrong data type
def get_credit_input(prompt):
    while True:
        try:
            credit_input = input(prompt)                          
            credit = int(credit_input)
            if credit not in range(0, 121, 20):
                print("Out of range.")
                continue

            return credit
        except ValueError:
            print("Integer Required\n")

while not terminate:
    pass_credit = get_credit_input("Enter your credit at pass: ")
    defer_credit = get_credit_input("Enter your credit at defer: ")
    fail_credit = get_credit_input("Enter your credit at fail: ")

#check the total 
    if (pass_credit + defer_credit + fail_credit) != 120:
        print("Total incorrect\n")
        continue

#check the credit values
    if pass_credit == 120 :
        print("Progress")
        progress_list.append((pass_credit, defer_credit, fail_credit))
        
    elif pass_credit == 100:
        print("Progress (module trailer)")
        trailer_list.append((pass_credit, defer_credit, fail_credit))
        
    elif fail_credit >= 80:
        print("Exclude")
        exclude_list.append((pass_credit, defer_credit, fail_credit))
    else:
        print("Do not progress- module retriever")
        retriever_list.append((pass_credit, defer_credit, fail_credit))
    # Save data to a text file
    outcome_text= open("outcome_text_file.txt","w")
    outcome_text.write("Part 3: \n\n")
    for outcome in progress_list:
        outcome_text.write(f"Progress - {outcome[0]}, {outcome[1]}, {outcome[2]}\n")
    for outcome in trailer_list:
        outcome_text.write(f"Progress (module trailer) - {outcome[0]}, {outcome[1]}, {outcome[2]}\n")
    for outcome in retriever_list:
        outcome_text.write(f"Module retriever - {outcome[0]}, {outcome[1]}, {outcome[2]}\n")
    for outcome in exclude_list:
        outcome_text.write(f"Exclude - {outcome[0]}, {outcome[1]}, {outcome[2]}\n")
    outcome_text.close()

# Ask the user if they want to enter another set of data
    print()
    print("Would you like to enter another set of data?")
    role = input("Enter 'y' for yes or 'q' to quit and view results: ")

    if role.lower() == 'y':
        print()
        continue

    while role.lower() != 'y' and role.lower() != 'q':
        role = input("Enter 'y' for yes or 'q' to quit and view results: ")     #debugging ValueError
        print()
        continue

    if role.lower() == 'q':
 #part 2-print the list  
        print()     
        print("\nPart 2:")
        for outcome in progress_list:
            print("Progress -", outcome[0],",", outcome[1],"," ,outcome[2])
        for outcome in trailer_list:
            print("Progress (module trailer) -", outcome[0],",", outcome[1],",", outcome[2])
        for outcome in retriever_list:
            print("Module retriever -", outcome[0],",", outcome[1],",", outcome[2])
        for outcome in exclude_list:
            print("Exclude -", outcome[0],",", outcome[1],",", outcome[2])
        break
    
#histogram part
    
def draw_bar(win, x, height, color, label, value):
# Draw rectangular
    bar = Rectangle(Point(x, 550), Point(x + 50, 549 - height))
    bar.setFill(color)
    bar.setOutline(color_rgb(224, 250, 252))
    bar.draw(win)
# Add label under each rectangle
    bar_text = Text(Point(x + 25,570), label)
    bar_text.setSize(14)
    bar_text.draw(win)
# Add value on each rectangle
    value_text = Text(Point(x + 25, 555 - height - 20), str(value))
    value_text.setSize(12)
    value_text.setStyle("bold")
    value_text.draw(win)

def histogram():
    win = GraphWin("Histogram", 500, 660)
# Title
    title_of_bargraph = Text(Point(180, 45), "Histogram Results")
    title_of_bargraph.setSize(20)
    title_of_bargraph.setStyle("bold")
    title_of_bargraph.draw(win)
# Bar 1= progress
    draw_bar(win, 50, 20 *len(progress_list), "blue", "Progress", len(progress_list))
# Bar 2 = trailer
    draw_bar(win, 150, 20 *len(trailer_list), "green", "Trailer", len(trailer_list))
# Bar 3 = retriever
    draw_bar(win, 250, 20 *len(retriever_list), "red", "Retriever", len(retriever_list))
# Bar 4 = excluded
    draw_bar(win, 350, 20 *len(exclude_list), "purple", "Excluded", len(exclude_list))
# horizontal line
    line = Line(Point(30,550), Point(420, 550))
    line.draw(win)
# represent the total value
    horizontal_line_represent = Text(Point(150, 610),
                                     f"{len(progress_list) + len(trailer_list) + len(retriever_list) + len(exclude_list)} Outcomes in Total")
    horizontal_line_represent.setSize(15)
    horizontal_line_represent.setStyle("bold")
    horizontal_line_represent.draw(win)

    win.getMouse()
    win.close()
histogram()

# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# student ID : 20231046
#Date : 2023/12/11


