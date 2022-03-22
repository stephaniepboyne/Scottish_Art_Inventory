class Print:

    def __init__(self, title, artist, size, price, printing_cost, stock, image_print_pathway,id = None):
        self.title = title
        self.artist = artist
        self.size = size
        self.price = price 
        self.printing_cost = printing_cost
        self.stock = stock  
        self.image_print_pathway = image_print_pathway
        self.id = id 
    
    def calculate_markup(self):
        difference = self.price % self.printing_cost
        divide = self.printing_cost / difference 
        percent = 100 / divide 
        return percent
    

    
    