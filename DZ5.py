# Напишите программу, удаляющую из текста все слова содержащие "абв", 
# которое регистронезависимо. Используйте знания с последней лекции. 
# Выполните ее в виде функции. 
# Пример: «абвгдеж рабав копыто фабв Абкн абрыволк аБволк»
# Примечание: в итоговой строке все слова будут в нижнем регистре. Как сохранить
# оригинальный регистр мне непонятно. 

# orign_str = 'абвгдеж рабав копыто фабв Абкн абрыволк аБволк'
# fragment = 'абв'
# def delete_words(work_str, frag):
#     work_str = work_str.lower()
#     work_str = work_str.split()
#     new_str = []
#     for i in work_str:
#         if frag not in i:
#             new_str.append(i)
#     new_str = ' '.join(new_str)
#     return new_str

# print(delete_words(orign_str, fragment))

#============================= Задача 2 ============================

# Создать игру крестики нолики.

# board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# def draw_board(board):
#     print ('-------------')
#     for i in range(3):
#         print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#         print ('-------------')

# def take_input(player_token):
#     valid = False
#     while not valid:
#         player_answer = input("Куда поставим " + player_token+"? ")
#         try:
#             player_answer = int(player_answer)
#         except:
#             print ("Некорректный ввод. Вы уверены, что ввели число?")
#             continue
#         if player_answer >= 1 and player_answer <= 9:
#             if (str(board[player_answer-1]) not in "XO"):
#                 board[player_answer-1] = player_token
#                 valid = True
#             else:
#                 print ("Эта клеточка уже занята")
#         else:
#             print ("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

# def check_win(board):
#     win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
#     for each in win_coord:
#         if board[each[0]] == board[each[1]] == board[each[2]]:
#             return board[each[0]]
#     return False

# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#             take_input("X")
#         else:
#             take_input("O")
#         counter += 1
#         if counter > 4:
#             tmp = check_win(board)
#             if tmp:
#                 print (tmp, "выиграл!")
#                 win = True
#                 break
#         if counter == 9:
#             print ("Ничья!")
#             break
#     draw_board(board)

# main(board)

#============================= Задача 3 ============================

# orign_text = 'Ну, вышел я, короче, из подъезда. В общем, короче говоря, \
#     шел я, кажется, в магазин. Ну,эээ, в общем, было лето, кажется. \
#     Как бы тепло. Солнечно, короче. Иду я, иду, в общем, по улице, а тут, \
#     короче, яма. Я, эээээ…. Упал в нее. И снова вышел, короче, из подъезда. \
#     Ясен пень, в магазин. В общем, лето на дворе, жарко, солнечно, птицы, \
#     короче, летают. Кстати, иду я по улице, иду, а тут, короче, яма. \
#     Ну, я в нее упал, в общем. Вышел из подъезда, короче. Лето на дворе, \
#     ясен пень. Птицы поют, короче, солнечно. В общем, в магазин мне надо. \
#     Что-то явно не так, короче. «Рекурсия», - подумал я. Ээээ...короче, \
#     в общем, пошел другой дорогой и не упал в эту… ээээ… яму. Хлеба купил'


# ban_list = 'Ну, короче, кажется, Ну,эээ, кажется. короче. \
#     эээээ…. Кстати, Ээээ...короче, эту… ээээ…'.split()
# ban_list_2 = ['В общем', 'короче говоря', 'в общем', 'Как бы', 'Ясен пень', 'ясен пень']
# work_text = orign_text.split()
# result_list = [word for word in work_text if word not in ban_list]
# final_text = ' '.join(result_list)

# import re
# remov = [r'\b' + phrase + r'\b' for phrase in ban_list_2]
# for rem in remov:
#     final_text = re.sub(rem, '', final_text)

# final_text = final_text.replace(' ,','')
# final_text = final_text.replace(' .','')
# print(final_text)

            