
class BaseClass:
    def to_string(self):
        items_part = "\n".join([f"\t {k}: {v}" for k, v in vars(self).items()])
        string = f"{self.__class__.__name__}(\n{items_part}\n)"
        return string



