from Classes import *








def debug_start(board: Board):
    L_CPT = L(board)
    L_CPT.generate_CPT()
    C_CPT = C(board)
    C_CPT.generate_CPT()
    M_CPT = M(board)
    M_CPT.generate_CPT()
    S_CPT = S(board)
    S_CPT.generate_CPT()


