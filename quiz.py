import sys
import difflib

def get_questions():
    with open('questions.txt') as f:
        lines = f.readlines()
    return [(lines[i], lines[i+1].strip()) for i in range(0, len(lines), 2)]


try:
    questions = get_questions()
except IOError as e:
    print 'Error reading questions file %s' % e
    sys.exit()
except IndexError:
    print 'Error: all questions in the questions file must have answers.'
    sys.exit()

score = 0
total = len(questions)
for question, answer in questions:
    guesses = 1
    correct = 'no'

    while guesses < 4 and correct == 'no':
        guess = raw_input(question.strip() + ' (Guess %s)\n' % guesses)
        q = difflib.SequenceMatcher(None, guess, answer)
        # print round(q.ratio()*100, 1)
        if round(q.ratio()*100, 1) == 100:
            print '---CORRECT---'
            score += 1
            correct = 'yes'
        else:
            print '---WRONG---'
        guesses += 1


print 'You got %s out of %s questions right' % (score, total)
