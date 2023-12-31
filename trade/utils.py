def size_calc(size):
    if size == "Simple":
        return 10
    elif size == "Portrait":
        return 20
    elif size == "Half Body":
        return 30
    elif size == "Full Body":
        return 40
    
def finish_calc(finish):
    if finish == "Rough":
        return 0
    elif finish == "Clean/Lined/Lineless":
        return 5
    
def color_calc(color):
    if color == "Uncolored":
        return 0
    elif color == "Rough":
        return 5
    elif color == "Clean Color/Painted":
        return 10
    
def shading_calc(shading):
    if shading == "Unshaded":
        return 0
    elif shading == "Minimal":
        return 5
    elif shading == "Fully Shaded":
        return 15
    
def background_calc(background):
    if background == "None":
        return 0
    elif background == "Pattern/Abstract":
        return 5
    elif background == "Props":
        return 10
    elif background == "Full Scene":
        return 20
    
#####

def get_none_handler(argument):
    if argument == None:
        return {}
    else:
        return argument