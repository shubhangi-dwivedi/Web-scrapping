from bs4 import BeautifulSoup

with open('index.html', 'r') as html_file:
    content= html_file.read()

    soup= BeautifulSoup(content, 'lxml')


#--------------------------------------------------------------------------------------
    #print all h5 tags, find() will print only 1 tag and execution will be stopped
    courses_html_tags= soup.find_all('h5')
    print(courses_html_tags)

    #can do iteration bcz now a list is formed storing h5 tag and data
    for course in courses_html_tags:
        print(course.text)  #getting text inside the tag

#-------------------------------------------------------------------------------------
    #grabing all the prices from the site
    course_cards= soup.find_all('div', class_='card') #passing card as a parameter to filter which div tags we want to store

    for course in course_cards:
        course_name= course.h5.text
        course_price= course.a.text

        print(course_name)
        print(course_price)


    #printing only course name with the price
    for course in course_cards:
        course_name= course.h5.text
        course_price= course.a.text.split()[-1] #printing the last element of the each element in price list

        print(course_name)
        print(course_price)

    #printing a dynamic string using f-string
        print(f'{course_name} costs {course_price}')

#---------------------------------------------------------------------------------------
