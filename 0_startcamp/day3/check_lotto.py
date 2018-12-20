from lotto_functions import am_i_lucky, pick_lotto, get_lotto

result = am_i_lucky(pick_lotto(), get_lotto(837))
print(result)

#↑↓ 같은 내용

import lotto_functions

lotto_functions.am_i_lucky(
    lotto_functions.pick_lotto(),
    lotto_functions.get_lotto(837)
)