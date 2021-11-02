from dusk.script import *

lb, nudging, interior, halo, end = HorizontalDomains(0, 1000, 2000, 3000, 4000)

@stencil
def unroll_v_c_v_unroll(kh_smag_e: Field[Cell, K], inv_dual_edge_length: Field[Cell], theta_v: Field[Vertex, K], z_temp: Field[Vertex, K]):
    with domain.upward.across[nudging:halo]:
        z_temp = sum_over(Vertex > Cell, kh_smag_e*inv_dual_edge_length*sum_over(Cell>Vertex, theta_v))
