from random import*
lst=['Указатель', 'Радуга', 'Мармелад', 'Поиск', 'Прятки', 'Сторож', 'Копейка',
     'Леопард', 'Аттракцион', 'Дрессировка', 'Ошейник', 'Карамель', 'Водолаз', 'Защита',
     'Батарея', 'Решётка', 'Квартира', 'Дельфинарий', 'Непогода', 'Вход', 'Полиция', 'Перекрёсток',
     'Башня', 'Стрелка', 'Градусник', 'Бутылка', 'Щипцы', 'Наволочка', 'Павлин', 'Карточка', 'Записка',
     'Лестница', 'Переулок', 'Сенокос', 'Рассол', 'Закат', 'Сигнализация', 'Журнал', 'Заставка', 'Тиранозавр',
     'Микрофон', 'Прохожий', 'Квитанция', 'Пауза', 'Новости', 'Скарабей', 'Серебро', 'Творог', 'Осадок', 'Песня',
     'Корзина', 'Сдача', 'Овчарка', 'Хлопья', 'Телескоп', 'Микроб', 'Угощение', 'Экскаватор', 'Письмо', 'Пришелец',
     'Айсберг', 'Пластик', 'Доставка', 'Полка', 'Билет', 'Вторник', 'Льдина', 'Интерес', 'Троллейбус', 'Футболист',
     'Лисёнок',
     'Пример', 'Баклажан', 'Лягушка', 'Джокер', 'Котлета', 'Накидка', 'Дикобраз', 'Барбарис', 'Работник', 'Кристалл',
     'Доспехи', 'Халва', 'Велосипед', 'Крючок', 'Кочка', 'Черепаха', 'Петля', 'Осень', 'Яйцо']
def get_w():
    return choice(lst).upper()
def risnk(trys):
    stgs= [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                ''']
    return(stgs[trys])



def game(nm):
    word=get_w()
    word=word.replace('Ё', 'Е')
    bilo=[]
    trys=6
    word1=word[0]+(len(word)-2)*'_'+word[-1]
    print(word1, '- загаданное слово')
    print(risnk(trys))
    while trys>0:
        print('------------------------------------------')
        print(f' {nm},  у вас осталось {trys} попыток', '\n'*3)
        print('\n'*2, ' '.join(word1), '\n'*2)
        gss=input(f'''  {nm},  предложите букву или слово:

        ''').upper()
        print('\n'*2)
        if gss not in bilo:
            if len(gss)==1:
                if gss in word:
                    lst_ind=[]
                    word2 = [ i for i in word]
                    for i in range(word2.count(gss)):
                        lst_ind.append(word2.index(gss))
                        word2.remove(gss)
                        word2.insert(0, '@')
                    for i in range(len(word1)):
                        if i in lst_ind:
                            word1=word1[:i]+gss+word1[i+1:]
                    print('повезло на этот раз', '\n')
                    print(' '.join(word1))
                    print('\n'*3)
                    bilo.append(gss)
                    if word1==word:
                        print(f'YHAAAAAAAAAA,  {nm.upper()} ,  U   WON 10000$$$$!!!!! it was    {word}    WORD!!')
                        break
                        
                    continue
                else:
                    print(f'не угадал, {nm}', '\n'*5)
                    bilo.append(gss)
                    trys-=1
                    print(risnk(trys))
            else:
                if gss==word:
                    print(f'YHAAAAAAAAAA,  {nm.upper()} ,  U   WON 10000$$$$!!!!! it was    {word}    WORD!!')
                    break
                else:
                    print('\n', 'no. you dont get it')
                    trys-=1
                    print(risnk(trys), '\n'*2)
                    bilo.append(gss)
        else:
            print('AAAAAAAA U JUST TRYIED IT!! STUPID PERSON!! YOUR IQ LOWER WHEN THE FLOOR', '\n'*2)
            
    else:
        print('''HAHA, U LOSE, LOSER!!!!
                                              HAHAHAHHAHHAHHAH
                                                                    GOOD LUCK
                        (～￣▽￣～)''')
        print('\n'*2, f'P.S. это было слово {word}')
        print('\n'*8)


name=input('КАК ТЕБЯ ЗОВУТ Э         ')
game(name)
while True:
    ng=input('хотите сыграть еще раз?? ( да = д, нет = н)')
    if ng=='д':
        print('\n'*10)
        game(name)
    elif ng=='н':
        break
    else:
        print('не понял, давайте еще раз', '\n')
