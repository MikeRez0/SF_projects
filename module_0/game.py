import numpy as np

#Константы для интервала угадываемых чисел
INTERVAL_MIN = 1
INTERVAL_MAX = 1000

def game_core_v1(number):
    '''Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count+=1
        predict = np.random.randint(1,101) # предполагаемое число
        if number == predict: 
            return(count) # выход из цикла, если угадали

def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = np.random.randint(INTERVAL_MIN,INTERVAL_MAX+1)
    while number != predict:
        count+=1
        if number > predict: 
            predict += 1
        elif number < predict: 
            predict -= 1
    return(count) # выход из цикла, если угадали

def game_core_v3(number):
    '''Сначала устанавливаем любое random число в интервале 1,101, а потом берем random число из интервала в зависимости от больше-меньше.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    lo = INTERVAL_MIN
    hi = INTERVAL_MAX+1
    predict = np.random.randint(lo,hi)
    while number != predict:
        count+=1
        if number > predict: 
            lo = predict
        elif number < predict: 
            hi = predict + 1       
        predict = np.random.randint(lo,hi)

    return(count) # выход из цикла, если угадали

def game_core_v4(number, debug=False):
    '''Каждую попытку выбираем середину интервала между максимум и минимумом
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    lo = INTERVAL_MIN
    hi = INTERVAL_MAX
    predict = int((hi-lo)/2) + lo
    if debug: print(f'Count {count} predicted: {predict}')
    while number != predict:
        count+=1
        if number > predict: 
            lo = predict
        elif number < predict: 
            hi = predict

        #Особая ситуация: или hi или lo
        if hi-lo ==1:
            predict= hi if predict == lo else lo
        else:
            predict = int((hi-lo)/2) + lo
        
        #Для целей отладки
        if debug: print(f'Count {count} predicted: {predict}')
        if count>INTERVAL_MAX:
            
            print('Too many counts :(')
            return (count)

    if debug: print(f'Count {count} success: {predict}\n')
    return(count) # выход из цикла, если угадали
        
def score_game(game_core, debug = False):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(INTERVAL_MIN,INTERVAL_MAX+1, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number, debug))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

# запускаем
score_game(game_core_v4, False)