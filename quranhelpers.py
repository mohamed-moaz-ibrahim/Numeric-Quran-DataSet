quran_letters = {'ء','أ','إ','ا','ٱ','آ','ى','ب','ت','ث','ج','ح','خ','د','ذ','ر','ز','س','ش','ص','ض','ط','ظ','ع','غ','ف','ق','ك','ل','م','ن','ه','و','ؤ','ي','ئ'}
letter_jomal = {'ء': 1 ,'أ': 1 ,'إ': 1 ,'ا': 1 ,'ٱ': 1 ,'آ': 1 ,'ى': 1 ,'ب': 2 ,'ت': 400 ,'ة': 400 ,'ث': 500 ,'ج': 3 ,'ح': 8 ,'خ': 600 ,'د': 4 ,'ذ': 700 ,'ر': 200 ,'ز': 7 ,'س': 60 ,'ش': 300 ,'ص': 90 ,'ض': 800 ,'ط': 9 ,'ظ': 900 ,'ع': 70 ,'غ': 1000 ,'ف': 80 ,'ق': 100 ,'ك': 20 ,'ل': 30 ,'م': 40 ,'ن': 50 ,'ه': 5 ,'و': 6 ,'ؤ': 6 ,'ي': 10 ,'ئ': 10}

def get_written_aya_words(aya):
    aya = aya.split()[:-1]
    if aya[0] == '۞':
        aya = aya[1:]
    if aya[-1][-1] == '۩':
        aya[-1] = aya[-1][:-1]
    return aya

def get_letters(text):
    letters = []
    for words in text.split():
        for c in words:
            if c in quran_letters:
                letters.append(c)
    return letters

def get_invariant_letters(text):
    letters = []
    for words in text.split():
        for c in words:
            if c in quran_letters:
                if c in ['ء','آ','أ','إ','ا','ى','ٱ']:
                    letters.append('ا')
                elif c in ['ة','ت',]:
                    letters.append('ت')
                elif c in ['ؤ','و']:
                    letters.append('و')
                elif c in ['ئ','ي']:
                    letters.append('ي')
                else:
                    letters.append(c)
    return letters

def calculate_text_jomal(text):
    total = 0
    for c in get_letters(text):
        total += letter_jomal[c]
    return total
    
def calculate_letters_jomal(letters):
    total = 0
    for c in letters:
        total += letter_jomal[c]
    return total

def calculate_cumulative_sum(number):
    total = 0
    for n in range(number + 1):
        total += n
    return total

def get_aya_indexes_list(aya):
    pass
