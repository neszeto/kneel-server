class Order(): 
    
    def __init__(self, id, metal_id, size_id, style_id, timestamp): 
        self.id = id
        self.metal_id = metal_id
        self.size_id = size_id
        self.style_id = style_id
        self.timestamp = timestamp
        self.metal = None
        self.size = None
        self.style = None