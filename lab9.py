import logging
logging.basicConfig(level=logging.INFO, filename="logger.log",
                    format='%(levelname)s (%(asctime)s): %(message)s',
                    encoding='utf-8', force=True)
logger = logging.getLogger(__name__)
logger.info('Программа запущена...')

import random
x = 0
kegs = []
while x == 0:
    N = input("Введите количество бочонков: ")
    if int(N) <= 0 or N.isdigit() == False:
        print("Некорректно введены данные, попробуйте ещё раз!")
        logger.info('Некорректно введены данные, попробуйте ещё раз!')
    else:
        logger.info(f'Количество бочонков: {N}')
        N = int(N)
        kegs = list(range(1,N+1))
        random.shuffle(kegs)
        x = 1
while len(kegs) != 0:
    ques = input("Нажмите Enter, чтобы вытащить бочонок из мешка\nВведите quit - чтобы завершить программу ")
    if ques == "quit":
        print("Программа завершена!")
        logger.info('Программа завершена!')
        break
    else:
        n = random.choice(kegs)
        print(f"Вам выпал бочонок с номером {n}!")
        logger.info(f'Выпал бочонок под номеров {n}')
        kegs.remove(n)
        logger.info(f'Бочонок под номером {n} удалён')
else:
    print("Программа завершена!")
    logger.info('Программа завершена...')