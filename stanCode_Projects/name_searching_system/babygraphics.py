"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000
DIVIDE = 0.56


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    x = GRAPH_MARGIN_SIZE + (width-2*GRAPH_MARGIN_SIZE)/len(YEARS)*year_index
    return x


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    x = GRAPH_MARGIN_SIZE
    y = GRAPH_MARGIN_SIZE
    canvas.create_line(x, y, CANVAS_WIDTH-x, y, width=LINE_WIDTH)
    canvas.create_line(x, CANVAS_HEIGHT-y, CANVAS_WIDTH - x, CANVAS_HEIGHT-y, width=LINE_WIDTH)
    for i in range(len(YEARS)):
        x1 = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x1, 0, x1, CANVAS_HEIGHT, width=LINE_WIDTH)
    for i in range (len(YEARS)):
        x2 = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_text(x2+TEXT_DX, CANVAS_HEIGHT-y,  text=YEARS[i], anchor=tkinter.NW)





def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid
    cn = 0
    for name in lookup_names:
        if name in name_data: # 下一個名字n要歸零
            n = 0
            rank_prev = 0
            year_prev = 0
            # 做好顏色變數
            if cn >= len(COLORS):
                cn = 0
                c = COLORS[cn]
            else:
                c = COLORS[cn]
            cn += 1
            for year in YEARS:
                # draw lines 先判斷rank 因為y位置
                x_name = get_x_coordinate(CANVAS_WIDTH, YEARS.index(year))

                if str(year) in name_data[name]: # 進名字裡面
                    rank = name_data[name][str(year)]
                    canvas.create_text(x_name + TEXT_DX, GRAPH_MARGIN_SIZE + int(rank)*DIVIDE, text=str(name) +' ' + str(rank), anchor=tkinter.NW, fill=c)
                else:
                    rank = None
                    canvas.create_text(x_name + TEXT_DX, CANVAS_HEIGHT - 1.8*GRAPH_MARGIN_SIZE, text=str(name) + ''+str(' *'), anchor=tkinter.NW, fill=c)
                if n >= 1:
                    # 考慮四種狀況
                    xx = get_x_coordinate(CANVAS_WIDTH, YEARS.index(year))
                    x_prev = get_x_coordinate(CANVAS_WIDTH, YEARS.index(year_prev))
                    if rank_prev is None:
                        if rank is None:
                            # 從底到底
                            canvas.create_line(x_prev, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, xx, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH, fill=c)

                        else:
                            # 從底到上\
                            canvas.create_line(x_prev, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, xx, GRAPH_MARGIN_SIZE+ int(rank)*DIVIDE, width=LINE_WIDTH, fill=c)
                    else:
                        if rank is None:
                            # 從上到底
                            canvas.create_line(x_prev, GRAPH_MARGIN_SIZE + int(rank_prev)*DIVIDE, xx, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH, fill=c)
                        else:
                            # 不觸底
                            canvas.create_line(x_prev, GRAPH_MARGIN_SIZE + int(rank_prev)*DIVIDE, xx, GRAPH_MARGIN_SIZE + int(rank)*DIVIDE, width=LINE_WIDTH, fill=c)

                n += 1  # 做完才更新
                # 前一項的rank year
                rank_prev = rank
                year_prev = year















            # main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
