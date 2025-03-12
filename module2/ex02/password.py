# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    password.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vkhut <vkhut@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/10 12:17:49 by vkhut             #+#    #+#              #
#    Updated: 2025/03/10 12:21:06 by vkhut            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

password = "Python is awesome"

enter_password = input("")
if enter_password == password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")