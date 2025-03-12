# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    round_up.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vkhut <vkhut@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/10 21:06:08 by vkhut             #+#    #+#              #
#    Updated: 2025/03/12 13:05:45 by vkhut            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import math
user_enter = input("Give me a number: ")
number = float(user_enter)
round1 = math.ceil(number)
print(f"{round1}")