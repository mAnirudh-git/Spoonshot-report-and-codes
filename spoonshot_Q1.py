from math import ceil
# reading file.
fl = open('article.txt', 'r')
# Manipulating data in file.
line1 = fl.readline().lower().split()
line2 = fl.readline().lower().split()
txt = line1 + line2
# removing few unnecessary words from the data.
norq = ['i','a', 'to', 'in', 'or','we', 'the', 'then','it','with','my','our', 'at', 'has','that','your','be', 'up','you', 'is','was', 'are', 'for', 'all', 'me', 'from', 'those', 'and', 'of','so', 'as', 'but', 'have', 'too', 'will', 'can']
for rm in norq:
    for i in range(50):
        if rm in txt:
            txt.remove(rm)
# Making an ingrediant list.
ing_list = ['Ambrette Seed', 'Apple Cinnamon Granola', 'Arizona Seasoning', 'Americano Coffee', 'Baby Abalone',
'Cadbury Double Decker Chocolate Bar', 'Campari Tomato', 'Celery Soup', 'Chia Meal', 'Crunch Bars', 'Cardamom',
'Giardiniera', 'Hog Maw', 'Mccormick Montreal Steak Seasoning', 'Muesli', 'Mulberry', 'Munch Chocolate', 'Murukku Packet',
'Mango', 'Organic Maize', 'Organic Peruvian Groundcherry', 'Organic Tartar Cream', 'Orange Extract', 'Pickled Cauliflower', 'Pork Chump Chops',
'Pork Lungs', 'Pork Tripe', 'Peanut Butter', 'Smokies Sausage', 'Snickers Spread', 'Strawberry Gelatin',
'Salmon', 'Tomato','Tamarind','Vegan Carob Chips','Vegan Chicken Strips','Vegan Chorizo',
'Vegan Marshmallow','Vegan Puff Pastry Sheet','Vegan Semisweet Chocolate Chips', 'Vegan White Cake','Vegetable Stock','Vinegar']
# Initialising rank list.
ranks = []
# Calculating ranks.
for a in ing_list:
    a = a.lower()
    a = a.split()
    rank = 0 # Rank initialization.
    for i in range(len(a)):
        for t in txt:
            if a[i] == t:
                rank+=1
    # Approximating ranks to its ceil.
    ranks.append(ceil(rank/len(a)))
print(ranks)