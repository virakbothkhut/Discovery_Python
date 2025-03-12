# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    float.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vkhut <vkhut@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/10 20:52:16 by vkhut             #+#    #+#              #
#    Updated: 2025/03/10 21:04:09 by vkhut            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

user_enter = input("Give me a number: ")

number = float(user_enter)
if number.is_integer():
    print("This number is an integer")
else:
    print("This number is a decimal")