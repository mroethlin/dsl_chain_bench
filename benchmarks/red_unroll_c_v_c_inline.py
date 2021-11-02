from dusk.script import *

lb, nudging, interior, halo, end = HorizontalDomains(0, 1000, 2000, 3000, 4000)

@stencil
def unroll_c_v_c_inline(kh_smag_e: Field[Vertex, K], inv_dual_edge_length: Field[Vertex], theta_v: Field[Cell, K], z_temp: Field[Cell, K]):
    tmp: Field[Vertex, K]
    with domain.upward.across[nudging:halo]:
        tmp = sum_over(Vertex>Cell, theta_v)
        z_temp = sum_over(Cell > Vertex, kh_smag_e*inv_dual_edge_length*tmp)