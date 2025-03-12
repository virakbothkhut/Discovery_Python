# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    calculator.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vkhut <vkhut@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/10 20:52:19 by vkhut             #+#    #+#              #
#    Updated: 2025/03/12 13:32:45 by vkhut            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

while True:
    try:
        user_enter1 = int(input("Give me the first number: "))
        user_enter2 = int(input("Give me the seconde number: "))
        if user_enter1 == 0:
            print(" Input can not be zero")
            print("Thank you!")
            break
        if user_enter2 == 0:
            print("Input can not be zero")
            print("Thank you!")
            break

        result_additional = user_enter1 + user_enter2
        print(f"{user_enter1} + {user_enter2} = {result_additional}")

        result_substration = user_enter1 - user_enter2
        print(f"{user_enter1} - {user_enter2} = {result_substration}")

        result_division = user_enter1 // user_enter2
        print(f"{user_enter1} / {user_enter2} = {result_division}")

        result_multiplication = user_enter1 * user_enter2
        print(f"{user_enter1} * {user_enter2} = {result_multiplication}")
    except ValueError:
        print("ERROR input")