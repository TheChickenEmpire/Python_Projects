def Quiz(questions:str, answers:str):
    """Use this function for a quiz example: Quiz(questions='What is python, Who is notch', answer='Coding language, Creator of minecraft')"""
    questions=questions.split(', ')
    answers=answers.split(', ')
    num = -1
    times = 0
    correct = 0
    open('Quiz results.txt','a').write(str(input('Your name:\n')+':\n'))
    for qustion in questions:
        num = num + 1
        question = str(questions[num]).capitalize()
        answer = str(answers[num])
        answer2 = answer.lower()
        it = str(input('Question '+str(times+1)+'\n'+question+':\n')).lower()
        if it == answer2:
            print('Correct')
            correct = correct + 1
        else:
            print('Wrong the answer was '+ answer)
        times = times + 1
    print('Your score is '+str(correct)+'/'+str(times))
    open('Quiz results.txt','a').write(str(correct)+'/'+str(times))

class Survey:
    def Survey(*questions:str):
        """Use this function for surveys example: Survey.Survey(questions = #your questions, #yourquestions)
        these will be saved automatically to Survey results"""
        open('Survey results.txt','a').write(str(input('Your name:\n')+':\n'))
        num = -1
        times = 0
        for qustion in questions:
            num = num + 1
            question = str(questions[num]).capitalize()
            it = str(input('Question '+str(times+1)+'\n'+question+':\n')).lower()
            times = times + 1
            open('Survey results.txt','a').write(it+'\n')