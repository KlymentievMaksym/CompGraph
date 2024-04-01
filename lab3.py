import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
# from numba import njit
import time


# @njit(nogil=True)
def calculate_xy(axiom, N, L, fi, dfi):
    x = np.zeros(N+1)
    y = np.zeros(N+1)
    for i in range(N):
        # print(x[i], x)
        x[i+1] = x[i]
        y[i+1] = y[i]
        if axiom[i] == 'F':
            x[i+1] += L*np.cos(fi)
            y[i+1] += L*np.sin(fi)
        elif axiom[i] == '+':
            fi += dfi
        elif axiom[i] == '-':
            fi -= dfi
    return x, y

def plot_fractal(axiom, fi, dfi, show_on_one, is_animation=False):
    N = len(axiom)
    L = 2
    fig, ax = plt.subplots()
    if not is_animation:
        x1, y1 = calculate_xy(axiom, N, L, fi, dfi)
        ax.plot(x1, y1)
    else:
        all_data = []
        dphi_data = []
        for dphi in np.arange(dfi[0], dfi[1], dfi[2]):
            x, y = calculate_xy(axiom, N, L, fi, dphi)
            all_data += [[x, y]]
            dphi_data += [dphi]
            
        def update(frame):
            ax.clear()
            x, y = all_data[frame]
            ax.plot(x, y)
            ax.set_title(f'dphi={dphi_data[frame]}')
        
        ani = animation.FuncAnimation(fig=fig, func=update, frames=len(all_data), interval=10)
        ani.save(str(time.time())+'.gif', writer=animation.PillowWriter(fps=30) )
    if not show_on_one:
        plt.show()

def create_fractal(axiom, rule, max_iter, fi, dfi, is_degree=False, show_all=False, show_on_one=False, is_animation=False):
    if is_degree:
        fi = np.radians(fi)
        if not is_animation:
            dfi = np.radians(dfi)
        else:
            for element in dfi:
                dfi[dfi.index(element)] = np.radians(element)
    if type(rule) is str:
        for iteration in range(max_iter):
            # print(axiom)
            new_axiom = ''
            for word_place in range(len(axiom)):
                if axiom[word_place] == 'F':
                    new_axiom += rule
                else:
                    new_axiom += axiom[word_place]
            axiom = new_axiom
            if show_all:
                plot_fractal(axiom, fi, dfi, show_on_one, is_animation)
    elif type(rule) is dict:
        for iteration in range(max_iter):
            # print(axiom)
            new_axiom = ''
            for word_place in range(len(axiom)):
                # print(rule.keys())
                if axiom[word_place] in rule.keys():
                    new_axiom += rule[axiom[word_place]]
                else:
                    new_axiom += axiom[word_place]
            axiom = new_axiom
            if show_all:
                plot_fractal(axiom, fi, dfi, show_on_one, is_animation)
    # print(axiom)
    if not show_all:
        plot_fractal(axiom, fi, dfi, show_on_one, is_animation)
        
plt.close(fig='all') 
# axiom = "F+F+F+F"
# rule = "FF+F++F+F"
# max_iter = 3
# fi = 0
# # dfi = np.pi/2
# dfi = [0, 2*np.pi, 1e-2]
# create_fractal(axiom, rule, max_iter, fi, dfi, is_animation=True)

# axiom = "X"
# rule = {"X": "XFYFX+F+YFXFY-F-XFYFX", "Y": "YFXFY-F-XFYFX+F+YFXFY"}
# max_iter = 4
# fi = 0
# dfi = [0, 2*np.pi, 1e-2]
# create_fractal(axiom, rule, max_iter, fi, dfi, is_animation=True)

# axiom = "FF+FF+FF+FF"
# rule = "F+F-F-F+F"
# max_iter = 4
# fi = 0
# # dfi = np.pi/2
# dfi = [0, 2*np.pi, 1e-2]
# create_fractal(axiom, rule, max_iter, fi, dfi, is_animation=True)

# axiom = "X+X+X+X+X+X+X+X"
# rule = {"X": "X+YF++YF-FX--FXFX-YF+X", "Y": "-FX+YFYF++YF+FX--FX-YF"}
# max_iter = 4
# fi = 0
# # dfi = np.pi/4
# dfi = [0, 2*np.pi, 1e-2]
# create_fractal(axiom, rule, max_iter, fi, dfi, is_animation=True)

# axiom = "XF"
# rule = {"X": "X+YF++YF-FX--FXFX-YF+", "Y": "-FX+YFYF++YF+FX--FX-Y"}
# max_iter = 4
# fi = 0
# # dfi = 60
# dfi = [0, 2*np.pi, 1e-2]
# create_fractal(axiom, rule, max_iter, fi, dfi, is_animation=True)

# axiom = "FX"
# rule = {"X": "X+YF+", "Y": "-FX-Y"}
# max_iter = 16
# fi = 0
# # dfi = 90
# dfi = [0, 2*np.pi, 1e-2]
# create_fractal(axiom, rule, max_iter, fi, dfi, is_animation=True)

# axiom = "F++F++F++F++F"
# rule = "F++F++F+++++F-F++F"
# max_iter = 4
# fi = 0
# # dfi = 36
# dfi = [0, 2*np.pi, 1e-2]
# create_fractal(axiom, rule, max_iter, fi, dfi, is_animation=True)

# axiom = "F+F+F+F"
# rule = "FF+F+F+F+FF"
# max_iter = 4
# fi = 0
# # dfi = np.pi/2
# dfi = [0, 2*np.pi, 1e-2]
# create_fractal(axiom, rule, max_iter, fi, dfi, is_animation=True)