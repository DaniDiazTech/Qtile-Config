from libqtile.config import Group


class CreateGroups:
    def __init__(self):
        self.group_names = ["B   ",
                            "D  ",
                            "T  ",
                            "V  ",
                            "M  ",
                            "C  ",
                            "E  "]

    def init_groups(self):
        """
        Return the groups of Qtile
        """
        #### First and last
        groups = [Group(name, layout="max") if name == self.group_names[0]
                  else Group(name, layout="floating")
                  if name == self.group_names[-1] else Group(name, layout="monadtall")
                  for name in self.group_names]
        return groups
