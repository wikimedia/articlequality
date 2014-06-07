class Dict(dict):
    
    def __init__(self, *args, vivifier, **kwargs):
        super().__init__(*args, **kwargs)
        self.vivifier = vivifier
    
    def __getitem__(self, key):
        if key not in self:
            self[key] = self.vivifier(key)
        
        return super().__getitem__(key)
