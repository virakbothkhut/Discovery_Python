# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mult.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vkhut <vkhut@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/10 12:23:14 by vkhut             #+#    #+#              #
#    Updated: 2025/03/10 12:34:36 by vkhut            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

number1 = int(input("Enter the first number:\n"))
number2 = int(input("Enter the second number:\n"))
result  = number1 * number2
print(f"{number1} x {number2} = {result}")
if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")
