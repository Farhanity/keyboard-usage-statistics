import keyboard


print('To stop the recording press Escape button\n')

board = {0: '1234567890!@#$%^&*()_+-=', 1: 'qwertyuiop[]\\{}йцукенгшщзхъ',
         2: 'asdfghjkl;\':"фывапролджэ', 3: 'zxcvbnm,./<>?ячсмитьбю'}

kb = keyboard.record(until = 'Esc')

keys = [item.name.lower() for item in kb if item.event_type == 'up']

numbers_symb = len([item for item in keys if item in board[0]])
first_layer = len([item for item in keys if item in board[1]])
second_layer = len([item for item in keys if item in board[2]])
third_layer = len([item for item in keys if item in board[3]])
shifts = len([item for item in keys if item == 'shift'])
backspaces = len([item for item in keys if item == 'backspace'])

print(f'Totally You pressed any button {len(keys)} times')
print(f'You have pressed numbers row (with symbols) {numbers_symb} times,')
print(f'the first row {first_layer} times,')
print(f'the second row {second_layer} times,')
print(f'the third row {third_layer} times.')
print(f'You have pressed shift {shifts} times')
print(f'And also You have pressed backspace {backspaces} times')

print('\nPress Enter to close the program')
keyboard.wait('enter')




                    


