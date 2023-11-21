class PaginationHelper:

    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self):
        return len(self.collection)

    def page_count(self):
        return -(-len(self.collection) // self.items_per_page)

    def page_item_count(self, page_index):
        result = [self.collection[i:i+self.items_per_page] for i in range(0, len(self.collection), self.items_per_page)]
        if  len(result) == 0 or page_index > len(result)-1 or page_index < 0:
            return -1
        return len(result[page_index])
    def page_index(self, item_index):
        if item_index < 0 or item_index >= len(self.collection):
            return -1
        else:
            return item_index // self.items_per_page
