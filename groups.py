from libqtile.config import Group
from icons import group_icons

class CreateGroups:
    group_names = group_icons 

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

