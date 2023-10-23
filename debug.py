from Classes import *








def debug_start(board: Board):
    L_CPT = L(board)
    L_CPT.get_probability()
    C_CPT = C(board)
    C_CPT.get_probability()
    M_CPT = M(board)
    M_CPT.get_probability()
    S_CPT = S(board)
    S_CPT.get_probability()


