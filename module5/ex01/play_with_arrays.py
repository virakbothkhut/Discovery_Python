# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    play_with_arrays.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vkhut <vkhut@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/11 13:03:03 by vkhut             #+#    #+#              #
#    Updated: 2025/03/11 13:03:03 by vkhut            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

original_array = [2, 8, 9, 48, 8, 22, -12, 2]
modified_array = [x + 2 for x in original_array]
print(f"Original array:  {original_array}")
print(f"New_array: {modified_array}")