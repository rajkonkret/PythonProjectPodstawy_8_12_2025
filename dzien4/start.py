import fun8

fun8.all_params(1, 2, 3, 4)

import pakiet
# pakiet.powianie()

from pakiet import fun
fun.powitanie() # Hello

# alias
import pakiet.fun as pk
pk.powitanie()
# Hello

# po dodaniu w __all__
pakiet.info()