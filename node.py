class ParserNode:
    def __init__(self, t_data, t_type, m_data, m_type):
        self.m_data = m_data
        self.m_type = m_type
        self.t_data = t_data
        self.t_type = t_type
        self.children = []

    def add(self, obj):
        self.children.append(obj)

    def render(self):
        if len(self.children) == 0:
            if self.t_type == "gibberish":
                return self.t_data
            if self.t_type == "model":
                return ""
            if self.t_type == "model.name":
                return self.m_data
            if self.t_type == "prop":
                return ""
            if self.t_type == "prop.name":
                return self.m_data
            if self.t_type == "root":
                return ""
        else:
            temp = ""
            for child in self.children:
                temp += child.render()
            return temp
