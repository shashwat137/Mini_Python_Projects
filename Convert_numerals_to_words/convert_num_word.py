'''
Converts a given integer number in numerals to words.
'''

def get_words(num):
    '''
    Takes a number in a string and makes it returns it in words in a string.
    '''

    minimal_digit = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 10:'Ten',
    11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen', 19:'Nineteen'}

    tens_digit = {2:'Twenty', 3:'Thirty', 4:'Forty', 5:'Fifty', 6:'Sixty', 7:'Seventy', 8:'Eighty', 9:'Ninety'}

    large_digit = ['Hundred', 'Thousand', 'Million', 'Billion', 'Trillion', 'Quadrillion', 'Quintillion', 'Hextillion', 'Septillion', 'Octillion', 'Nonillion', 'Decillion',
                   'Undecillion', 'Duodecillion', 'Tredecillion', 'Quattuordecillion', 'Quindecillion', 'Hexdecillion', 'Septendecillion', 'Octodecillion', 'Novemdecillion',
                   'Vigintillion', 'Unvigintillion', 'Duovigintillion', 'Trevigintillion', 'Quattourvigintillion', 'Quinvigintillion', 'Hexvigintillion', 'Septenvigintillion',
                   'Octovigintillion', 'Novemvigintillion', 'Trigintillion', 'Untrigintillion', 'Duotrigintillion',
                   '']

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
