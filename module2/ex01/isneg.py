# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    isneg.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vkhut <vkhut@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/10 12:11:50 by vkhut             #+#    #+#              #
#    Updated: 2025/03/10 12:32:37 by vkhut            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

number = int(input(""))
if number < 0:
    print("This number is negative.")
elif number > 0:
    print("This number is positive")
else:
    print("This number is both positive and negative")
    