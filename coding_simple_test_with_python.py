from random import randint
import time

name = input('What is Your name? : ')


print('\tWelcome ' + name + ' to Emmy\'s Coding quiz')
print('You just have 10 questions to Attempt.')
choice = input('If you\'re ready, Enter Y? and if not, N \n Your Choice : ')


if choice.title() == 'Y':
    myquestions = { 'questions':[
                    'What tag is used to create a line break without an extra space between the text blocks?',
                    'General HTML elements consist of:',
                    'Which attribute of the link tag contains the URL location that you are trying to link to?',
                    'Which attribute contains the URL address of the webpage that is located after a form submission?',
                    'Which value for the type attribute turns the input tag into submit button?',
                    'To make a circle in CSS3, the border radius should be ...',
                    'What value does the rotate function take?',
                    'Width and Height are usually expressed in?',
                    'why is the name of one of the fonts put in quotes?',
                    'The "else" statement is created to:',
                    'What is the output of this code? \n\tprint(10//4)',
                    'What is an exception?',
                    'Which exception is raised by this code?print("7" + 4) - Python',
                    'What part of an If statement should be indented?',
                    'Which Construct can be used to iterate through a list?',
                    ],

                    'options':[
                    
                        
                    {
                    'a':'li',
                    'b':'a',
                    'c':'br',
                    'd':'hr'},

                    
                    {
                    'a':'the body tag',
                    'b':'opening tag, content, closing tag',
                    'c':'only tags',
                    'd':'only content'},

                    {
                    'a':'address',
                    'b':'location',
                    'c':'target',
                    'd':'href'
                    },

                    {
                    'a':'name',
                    'b':'id',
                    'c':'method',
                    'd':'action'
                    },

                    {
                    'a':'checkbox',
                    'b':'submit',
                    'c':'radio',
                    'd':'button'
                    },

                    {
                    'a':'an even number',
                    'b':'equal to half of the height and the width',
                    'c':'100 pixels',
                    'd':'120 pixels',
                    },

                    {
                    'a':'direction',
                    'b':'angle',
                    'c':'coordinates',
                    'd':'none'
                    },

                    {
                    'a':'points and picas',
                    'b':'pixels and percents',
                    'c':'inches and centimeters',
                    'd':'kilometers'
                    },

                    
                    {
                    'a':'it\'s a rarely used font',
                    'b':'it support "fallback"',
                    'c':'it shows a font family',
                    'd':'it consists of two or more words'
                    },

                    
                    {
                    'a':'Ignore the condition testing',
                    'b':'Tell javascript to execute something if the condition is false',
                    'c':'Test a new condition for true or false',
                    'd':'none'
                    },

                     {
                    'a':'0',
                    'b':'1',
                    'c':'2',
                    'd':'3'
                    },

                    
                     {
                    'a':'A function',
                    'b':'An event that occurs due to incorrect code or input',
                    'c':'A program',
                    'd':'A variable'
                    },

                    
                     {
                    'a':'TypeError',
                    'b':'ZeroDivisionError',
                    'c':'ValueError',
                    'd':'None Of the above'
                    },

                    
                     {
                    'a':'All of it',
                    'b':'The first line',
                    'c':'The statements within it',
                    'd':'None'
                    },

                    
                     {
                    'a':'Loops',
                    'b':'Variable assignment',
                    'c':'If statement',
                    'd':'elif statement'
                    },
                        ],
                    'answers':['c', 'b', 'd', 'b', 'b', 'b', 'b', 'b', 'a', 'b', 'c', 'b', 'a', 'c', 'a']
                    }

    score = 0
    for i in range (len(myquestions['questions'])):
        print('\nQuestion ' + str(i+1) + ': ' + myquestions['questions'][i])
        for k,v in myquestions['options'][i].items(): 
            print('\t' + k.title() + ' : ' + v)
        ans = str(input('answer :'))
        options = ['a', 'b', 'c', 'd']
        if ans  not in options:
            print('invalid')
            continue
        elif ans == myquestions['answers'][i]:
            score+=1
        

    print('\n\t\tCorrect Answers')
    for i in range (len(myquestions['questions'])):
        print('\nQuestion ' + str(i+1) + ': ' + myquestions['questions'][i])
        for k,v in myquestions['options'][i].items(): 
            print('\t' + k.title() + ' : ' + v)
        print('Correct Answer : ' +  myquestions['answers'][i].title())
        time.sleep(3)
            
    print('\n\t\tTotal Score = ' + str(score))
else:
    print('Goodbye')
