'''
Converts a given integer number in numerals to words.
'''

def get_words(num):
    '''
    Takes a number in a string and makes it returns it in words in a string.
    '''

    minimal_digit = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten',
    11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}

    tens_digit = {2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}

    large_digit = ['hundred', 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'hextillion', 'septillion', 'octillion', 'nonillion', 'Decillion', '']

    word = ''
    i = len(num) - 1

    if len(num) >= 3:
        while i >= 0:
            if i == 0:
                segment = num[i] # Should give a single digit number in string format.
            elif i == 1:
                segment = num[i-1: i+1] # Should give a two digit number in string format.
            else:
                segment = num[i-2: i+1] # Should give a three digit number in string format.
            check_size = len(segment)
            if check_size < 3:
                for add in range(3 - check_size):
                    segment = '0' + segment
            j = 0
            small_word = ''
            while j < 3:
                if segment[j] == '0':
                    j += 1
                elif j == 0:
                    small_word += minimal_digit[int(segment[j])] + ' ' + large_digit[0] + ' '
                    j += 1
                elif (j == 1 and segment[j] == '1') or j == 2:
                    small_word += minimal_digit[int(segment[j:])] + ' '
                    j = 3
                elif j == 1:
                    small_word += tens_digit[int(segment[j])] + ' '
                    j += 1
                else:
                    pass
            # Done with this now need to put logic for larger numbers like thousand etc.
            k = int((len(num) - i )/ 3)  # Gives any suffix like thousand that may be necessary
            if k > 0 and small_word != '': # small_word condition removes rrequirement of entering trailing zeroes.
                if large_digit[k] == '':
                    return 'Sorry but that number is too large for me to spell out right now.\nBut don\'t worry, I am still learning.'
                small_word += large_digit[k] + ' '
            word = small_word + word
            i -= 3
    else:
        if num[0] == '1' or len(num) == 1:
            word = minimal_digit[int(num)] + ' '
        else:
            word = tens_digit[int(num[0])] + ' ' + minimal_digit[int(num[1])] + ' '
    return word


def main():
    while True:
        # Number kept in string
        while True:
            num = input('Enter an Integer you wish  to generate in words\n')
            try:
                n = int(num)
                break
            except:
                print('Please Enter input correctly. Non Numerals are not allowed.')
                continue
        word = get_words(num)
        print(word)
        while True:
            val = input('Enter y to try more, enter q to exit\n').lower()
            if val == 'y' or val == 'q':
                break
            else:
                print('Enter input correctly')
                continue
        if val == 'y':
            continue
        else:
            break
    return


if __name__ == "__main__":
    main()
