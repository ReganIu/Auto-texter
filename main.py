import os

def get_words(file_path):
    with open(file_path, 'r') as f:
        text = f.readlines()[0]
        words = text.split()
    return words

def send_message(phone_number, message):
    os.system('osascript auto-text.scpt {} "{}"'.format(phone_number, message))

def get_lines(file_path):
    with open(file_path, 'r') as f:
        text = f.readlines()
    return text

if __name__ == '__main__':
    words = get_words('text.txt')
    for word in words:
        send_message(number, word) #replace number with phone number

#alternative code to complete the same task
    # full_word = ''
    # for word in words:
    #     full_word = full_word + word + ' '
    #     if word == 'you':
    #         send_message(number, full_word)
    #         full_word = ''

    # lines = get_lines('text.txt')
    # for line in lines:
    #     send_message(number, line)
