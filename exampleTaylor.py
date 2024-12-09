import TSplotly_Musalar

plotter = TSplotly_Musalar.TaylorPlotter()
plotter.visualize_taylor_series(
    equation="sin(x)", 
    x_range=(-10, 10), 
    order=5
)