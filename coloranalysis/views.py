from django.shortcuts import render
from collections import Counter
from django.http import JsonResponse
import numpy as np
import json
import random
from .models import ShirtColor

 # Create your views here.




DRESS_COLORS = {
    'Monday': ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"],
    'Tuesday': ["ASH", "BROWN", "GREEN", "BROWN", "BLUE", "BLUE", "BLUE", "PINK", "PINK", "ORANGE", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "BLUE"],
    'Wednessday':["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "RED", "YELLOW", "ORANGE", "RED", "ORANGE", "RED", "BLUE", "BLUE", "WHITE", "BLUE", "BLUE", "WHITE", "WHITE"],
    'Thursday': ["BLUE", "BLUE", "GREEN", "WHITE", "BLUE", "BROWN", "PINK", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"],
    'Friday': ["GREEN", "WHITE", "GREEN", "BROWN", "BLUE", "BLUE", "BLACK", "WHITE", "ORANGE", "RED", "RED", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "WHITE"]
}

def save_color_data(color_count):
    """ Save color data in the database """
    for color, freq in color_count.items():
        obj, created = ShirtColor.objects.update_or_create(
            color=color,
            defaults={'frequency': freq}
        )
 
def home_page(request):

    return render(request,'base/index.html')


def analysis_check(request):
    #This line of code returns all colors in a single list
    all_colors = [color for colors in DRESS_COLORS.values() for color in colors]

    #This get the total number of colors in the list
    color_count = Counter(all_colors)

    most_frequent_color = max(color_count, key=color_count.get)
    highest_frequency = color_count[most_frequent_color]
    mean_color = most_frequent_color
    unique_colors, counts = np.unique(all_colors, return_counts=True)
    median_color = unique_colors[np.argsort(counts)[len(counts) // 2]]
    variance = np.var(counts)
    
    total_colors = len(all_colors)
    probability_red = color_count.get("RED", 0) / total_colors if total_colors else 0

    colors_json = json.dumps(list(color_count.keys()))  # Labels
    frequencies_json = json.dumps(list(color_count.values())) 
    context = {
       "colors": colors_json,
        "frequencies": frequencies_json,
        "mean_color": mean_color,
        "most_worn_color": most_frequent_color,
        "median_color": median_color,
        "variance": variance,
        'highest_frequency': highest_frequency,
        "probability_red": round(probability_red, 6)
    }
    return render(request, 'base/analysisresult.html', context)

def binary_page(request):
    binary_number = "".join(str(random.randint(0, 1)) for _ in range(4))
    base10_number = int(binary_number, 2)
    
    return render(request, 'base/binary.html', {"binary": binary_number, "base10": base10_number})

def fibonacci_sequence(request):
    fib_sequence = [0, 1]
    for _ in range(48): 
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return render(request, 'base/fibonacci.html', {'fib_sequence': fib_sequence})