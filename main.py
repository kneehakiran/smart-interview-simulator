#Smart Interview Simulator
import random
print('WELCOME TO SMART INTERVIEW SIMULATOR')
name = input('Enter your name: ')
print('Hello', name)
print('Your interview is starting...')

questions = {
    'HR': [
        'Tell me about yourself',
        'Why do you want this job?'
    ],

    'Technical': [
        'What is Python?',
        'Explain loops in Python'
    ]
}

excellent_feedback = [
    'Outstanding response!',
    'Very confident answer!',
    'Excellent communication skills!'
]

good_feedback = [
    'Good Answer!',
    'Nice response!',
    'Well explained!'
]

score = 0
for category in questions:
   print(f'\n--- {category} Round --- ')


   for question in questions[category]:
      print('\nQuestion:', question)
      answer = input('Your Answer: ')

      if len(answer) > 50:
          print(random.choice(excellent_feedback))
          score += 3
      elif len(answer) > 20:
          print(random.choice(good_feedback))
          score += 2
      else:
          print('Answer could be more detailed.')
          score += 1
print('\nInterview Finished!')
print('Final Score:', score)

if score >= 6:
    result = 'Excellent Performance!'
    print(result)
elif score >= 4:
    result = 'Good Job!'
    print(result)
else:
    result = 'Needs Improvement.'
    print(result)

file = open('interview_results.txt', 'a')
file.write(f'Candidate Name: {name}\n')
file.write(f'Final Score: {score}\n')
file.write(f'Performance: {result}\n')
file.write('---------------------\n')
file.close()